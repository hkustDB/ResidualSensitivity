# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import psycopg2
import getopt
import math
import random

epsilon = 1
delta = 10**(-6)
database_name = ""
query_path = ""
private_relation_list_path = ""
noise_mechanism = 1
query_result = 0
residual_sensitivity = 0.0
final_result = 0
query = ""
private_relation_names = []
relation_names = []
relation_id_dic = {}
relation_num = 0
private_relation_num = 0
TE_dic= {}
edges = np.zeros((0,0))
attribute_in_edges = []
noised_result = 0.0

def ReadQuery():
    global query
    query_file = open(query_path,'r')
    for line in query_file.readlines():
        query = query+line
        if ";" in query:
            query = query.replace('\n'," ")
            break
        
def RunQuery(cur):
    global query_result
    cur.execute(query)
    query_result = int(cur.fetchone()[0])
    
def ReadRelationList():
    global private_relation_names
    private_relation_list_file = open(private_relation_list_path,'r')
    for line in private_relation_list_file.readlines():
        relation_name = line.replace('\n',"")
        private_relation_names.append(relation_name)
    
def ExtractQueryInfo(cur):
    global relation_num
    global private_relation_num
    global relation_names
    global relation_id_dic 
    global edges
    global attribute_in_edges
    parser_string = query.lower()
    parser_string = parser_string.replace(" from ","\n")
    parser_string = parser_string.replace(" where ","\n")
    parser_string = parser_string.replace(";","")
    parser_strings = parser_string.split("\n")
    relations_strings = parser_strings[1]
    conditions_strings = parser_strings[2]
    relations_strings = relations_strings.replace(","," ")
    relation_names_t = relations_strings.split()
    relation_num = len(relation_names_t)
    private_relation_num = len(private_relation_names)
    attributes_for_relation = []
    
    #Reorder the relations so public ones are in front
    name_id = 0
    for i in range(relation_num):
        if relation_names_t[i] not in private_relation_names:
            relation_id_dic[relation_names_t[i]] = name_id
            relation_names.append(relation_names_t[i])
            name_id+=1
    for i in range(relation_num):
        if relation_names_t[i] in private_relation_names:
            relation_id_dic[relation_names_t[i]] = name_id
            relation_names.append(relation_names_t[i])
            name_id+=1

    #Build the relation graph
    edges = np.zeros((relation_num,relation_num))
    attribute_in_edges = []
    for i in range(relation_num):
        attribute_in_edges.append({})
        for j in range(relation_num):
            attribute_in_edges[i][j] = []
        
    #Collect attribute information for each relation
    for i in range(relation_num):
        attri_query = "select column_name from information_schema.columns where table_name='"+relation_names[i]+"';"
        cur.execute(attri_query)
        res = cur.fetchall()
        t_list = []
        for j in range(len(res)):
            t_list.append(res[j][0])
        attributes_for_relation.append(t_list)
    conditions = conditions_strings.split(" and ")   
    for i in range(len(conditions)):
        terms = conditions[i].replace(" ","").split("=")
        left_relation = 0
        right_relation = 0
        if "." in terms[0]:
            left = terms[0].split(".")
            left_relation = left[0]
            left_attribute = left[1]
        else:
            left_attribute = terms[0]
            for j in range(relation_num):
                if left_attribute in attributes_for_relation[j]:
                    left_relation = relation_names[j]
                    break
        if "." in terms[1]:
            right = terms[1].split(".")
            right_relation = right[0]
            right_attribute = right[1]
        else:
            right_attribute = terms[1]
            for j in range(relation_num):
                if right_attribute in attributes_for_relation[j]:
                    right_relation = relation_names[j]
                    break
        edges[relation_id_dic[left_relation]][relation_id_dic[right_relation]] = 1
        edges[relation_id_dic[right_relation]][relation_id_dic[left_relation]] = 1
        attribute_in_edges[relation_id_dic[left_relation]][relation_id_dic[right_relation]].append(left_attribute)
        attribute_in_edges[relation_id_dic[right_relation]][relation_id_dic[left_relation]].append(right_attribute)  
    
def CompTEs(cur_E,cur_id,cur):
    if cur_id==relation_num:
        CompTE(cur_E,cur)
    else:
        CompTEs(cur_E+"0",cur_id+1,cur)
        CompTEs(cur_E+"1",cur_id+1,cur)

def CompTE(cur_E,cur):
    global TE_dic
    zero_num = 0
    for i in range(len(cur_E)):
        if cur_E[i]=="0":
            zero_num+=1
    if zero_num==0:
        return
    left_part = "select max(count) from ("
    right_part = ") as t;"
    residual_query = ""
    
    left_relations_num = relation_num-zero_num
    ind_not_considered = np.ones(relation_num)
    TE = 1
    
    #Separate the relations into several connected part
    while left_relations_num>0:
        party = []
        neighbors = []
        
        ind_new = True
        while ind_new:
            ind_new = False
            for i in range(relation_num):
                if ind_not_considered[i]==1 and cur_E[i]=="1":
                    if len(party)==0:
                        party.append(i)
                        left_relations_num-=1
                        ind_not_considered[i]=0
                        ind_new = True
                        for j in range(relation_num):
                            if edges[i][j]==1:
                                neighbors.append(j)
                    if i in neighbors:
                        party.append(i)
                        left_relations_num-=1
                        ind_not_considered[i]=0
                        ind_new = True
                        for j in range(relation_num):
                            if edges[i][j]==1:
                                neighbors.append(j)
            
        attributes = []
        for i in range(relation_num):
            for j in range(relation_num):
                if (i in party) and (j not in party) and edges[i][j] == 1:
                    for k in range(len(attribute_in_edges[i][j])):
                        attributes.append(relation_names[i]+"."+attribute_in_edges[i][j][k])
                    
        select_conditions = []
        for i in range(relation_num):
            for j in range(relation_num):
                if i>j:
                    if (i in party) and (j in party) and edges[i][j] == 1:
                        for k in range(len(attribute_in_edges[i][j])):
                            select_conditions.append(relation_names[i]+"."+attribute_in_edges[i][j][k]+"="+relation_names[j]+"."+attribute_in_edges[j][i][k])

        first_part = "select "
        for attribute in attributes:
            first_part = first_part+attribute+", "
        first_part=first_part+"count(*) "
        
        second_part = "from "
        first_one = True
        for relation_id in party:
            if first_one:
                second_part=second_part+relation_names[relation_id]
                first_one=False
            else:
                second_part=second_part+", "+relation_names[relation_id]
        second_part = second_part+" "
        
        third_part = "where "
        first_one = True
        for select_condition in select_conditions:
            if first_one:
                third_part=third_part+select_condition
                first_one=False
            else:
                third_part=third_part+" and "+select_condition
        third_part = third_part+" "
        
        fourth_part = "group by "
        first_one = True
        for attribute in attributes:
            if first_one:
                fourth_part=fourth_part+attribute
                first_one=False
            else:
                fourth_part=fourth_part+", "+attribute
                
        residual_query = left_part+first_part+second_part
        if len(party)>1:
            residual_query = residual_query+third_part
        residual_query = residual_query+fourth_part+right_part
        cur.execute(residual_query)
        TE_t = cur.fetchone()
        TE_t = int(TE_t[0])
        TE*=TE_t
    TE_dic[cur_E] = TE

def OutputTEs(TE_output_path):
    TE_results = open(TE_output_path,'w')
    for E in TE_dic.keys():
        intE = int(E,2)
        intE = intE+1-1
        TE_results.write(str(intE)+" "+str(TE_dic[E])+"\n")
    TE_results.close()

def CalRS(cur_path,beta):
    global residual_sensitivity
    ind_P = ""
    for i in range(relation_num-private_relation_num):
        ind_P = ind_P+"1"
    for i in range(private_relation_num):
        ind_P = ind_P+"0"
    cmd = cur_path+"/RSCalculator/RSCalculator -n "+str(int(relation_num))+" -P "+ind_P+" -B "+str(beta)
    cmd = cmd+" -I "+cur_path+"/TE.txt"
    shell = os.popen(cmd, 'r')
    res = shell.read()
    res = res.split()
    residual_sensitivity = float(res[0])
    shell.close()

def LapNoise():
    a = random.uniform(0,1)
    b = math.log(1/(1-a))
    c = random.uniform(0,1)
    if c>0.5:
        return b
    else:
        return -b
    
def CauchyCum(x):
    a = 1/4/math.sqrt(2)*(math.log(abs(2*x**2+2*math.sqrt(2)*x+2))+2*math.atan(math.sqrt(2)*x+1))
    a += 1/4/math.sqrt(2)*(-math.log(abs(2*x**2-2*math.sqrt(2)*x+2))+2*math.atan(math.sqrt(2)*x-1))
    return a

def CauNoise():
    a = random.uniform(0,math.pi/2/math.sqrt(2))
    left = 0
    right = 6000
    mid = 1.0*(left+right)/2
    while(abs(CauchyCum(mid)-a)>0.000001):
        if CauchyCum(mid)>a:
            right = mid
        else:
            left = mid
        mid = 1.0*(left+right)/2
    c = random.uniform(0,1)
    if c>0.5:
        return mid
    else:
        return -mid

def main(argv):
    global epsilon
    global delta
    global database_name
    global query_path
    global private_relation_list_path
    global noise_mechanism
    
    try:
        opts, args = getopt.getopt(argv,"h:e:d:D:Q:P:N:",["Epsilon=","Delta=","Database=","QueryPath","PrivateListPath","NoiseMechanism"])
    except getopt.GetoptError:
        print("RunDemoSystem.py -e <epsilon> -d <Delta> -D <database name> -Q <query file path> -P <private list path> -N <noise mechanism: 0(Laplace)/1(Cauchy)>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("RunDemoSystem.py -e <epsilon> -d <Delta> -D <database name> -Q <query file path> -P <private list path -N <noise mechanism: 0(Laplace)/1(Cauchy)>")
            sys.exit()
        elif opt in ("-e", "--Epsilon"):
            epsilon = float(arg)
        elif opt in ("-d", "--Delta"):
            delta= float(arg)
        elif opt in ("-D", "--Database"):
            database_name = arg
        elif opt in ("-Q","--QueryPath"):
            query_path = arg
        elif opt in ("-P","--PrivateListPath"):
            private_relation_list_path = arg
        elif opt in ("-N","--NoiseMechanism"):
            noise_mechanism = arg
        
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    cur_path= os.path.dirname(os.path.abspath(__file__))
    
    if noise_mechanism not in ("0","1"):
        print("Invalid noise model: 0(Laplace)/1(Cauchy)")
        sys.exit() 
    
    if epsilon <= 0:
        print("Invalid epsilon")
        sys.exit() 
        
    if noise_mechanism==0 and delta <= 0:
        print("Invalid delta")
        sys.exit() 
        
    #Compute beta
    if noise_mechanism==0:
        beta = epsilon/2/math.log(2/epsilon)
    else:
        beta = epsilon/10
        
    #Read query
    ReadQuery()
    #Run the query
    RunQuery(cur)
    #Read the list of private relations
    ReadRelationList()
    #Extract the information from query
    ExtractQueryInfo(cur)
    #Compute TEs
    cur_E = ""
    for i in range(relation_num-private_relation_num):
        cur_E = cur_E+"1"
    CompTEs(cur_E,relation_num-private_relation_num,cur)
    #Output the TEs
    OutputTEs(cur_path+"/TE.txt")
    #Calculate RS
    CalRS(cur_path,beta)
    if noise_mechanism ==0:
        noised_result = query_result+residual_sensitivity*2/epsilon*LapNoise()
    else:
        noised_result = query_result+residual_sensitivity*10/epsilon*CauNoise()
    #Delete tempoaray file
    cmd = "rm "+cur_path+"/TE.txt"
    shell = os.popen(cmd, 'r')
    shell.close()
    print(noised_result)
    
if __name__ == "__main__":
   main(sys.argv[1:])
   
   
