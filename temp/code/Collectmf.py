# -*- coding: utf-8 -*-
import psycopg2
import sys, getopt
import os



from_to_relations = []
mfs = []
reuse = {}



def SolveQ1():
    from_to_relations.append([0,1])
    from_to_relations.append([1,0])
    from_to_relations.append([1,2])
    from_to_relations.append([2,1])
    from_to_relations.append([2,3])
    from_to_relations.append([3,2])
    from_to_relations.append([3,4])
    from_to_relations.append([4,3])
    
    
    
def SolveQ2():
    from_to_relations.append([0,1])
    from_to_relations.append([1,2])
    from_to_relations.append([1,0])
    from_to_relations.append([1,3])
    from_to_relations.append([2,1])
    from_to_relations.append([3,1])
    from_to_relations.append([3,4])
    from_to_relations.append([4,3])
    
    
    
def SolveQ3():
    from_to_relations.append([0,1])
    from_to_relations.append([1,0])
    from_to_relations.append([1,2])
    from_to_relations.append([1,5])
    from_to_relations.append([2,1])
    from_to_relations.append([2,3])
    from_to_relations.append([3,2])
    from_to_relations.append([3,4])
    from_to_relations.append([4,3])
    from_to_relations.append([4,5])
    from_to_relations.append([5,4])
    from_to_relations.append([5,1])
    reuse[3] = 2



def SolveQ4():
    from_to_relations.append([0,1])
    from_to_relations.append([1,0])
    from_to_relations.append([1,2])
    from_to_relations.append([2,1])
    from_to_relations.append([2,3])
    from_to_relations.append([3,2])
    from_to_relations.append([3,4])
    from_to_relations.append([4,3])
    

    
def SolveQ5():
    from_to_relations.append([0,2])
    from_to_relations.append([0,1])
    from_to_relations.append([1,0])
    from_to_relations.append([1,2])
    from_to_relations.append([2,1])
    from_to_relations.append([2,0])


    
def SolveQ6():
    from_to_relations.append([0,3])
    from_to_relations.append([0,1])
    from_to_relations.append([1,0])
    from_to_relations.append([1,2])
    from_to_relations.append([2,1])
    from_to_relations.append([2,3])
    from_to_relations.append([3,2])
    from_to_relations.append([3,0])



def SolveQ7():
    from_to_relations.append([0,4])
    from_to_relations.append([0,1])
    from_to_relations.append([1,0])
    from_to_relations.append([1,2])
    from_to_relations.append([2,1])
    from_to_relations.append([2,3])
    from_to_relations.append([3,2])
    from_to_relations.append([3,4])
    from_to_relations.append([4,3])
    from_to_relations.append([4,0])



def SolveQ8():
    from_to_relations.append([0,1])
    from_to_relations.append([0,2])
    from_to_relations.append([0,3])
    from_to_relations.append([1,0])
    from_to_relations.append([2,0])
    from_to_relations.append([3,0])
  
    
    
def main(argv):
    query_id = ''
    database_name = ''
    scale = ''
    scale_t = ''
    
    try:
        opts, args = getopt.getopt(argv,"hD:s:Q:",["Database=","scale=","Query="])
    except getopt.GetoptError:
        print("Collectmf.py -D <Databse name> -s <scale:0.01/0.05/.../10> -Q <Query ID:1/2/../8>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Collectmf.py -D <Databse name> -s <scale:0.01/0.05/.../10> -Q <Query ID:1/2/../8>")
            sys.exit()
        elif opt in ("-Q", "--Query"):
            query_id = arg
        elif opt in ("-s", "--scale"):
            scale = arg
        elif opt in ("-D","--Database"):
            database_name = arg
    
    if query_id not in ("1","2","3","4","5","6","7","8"):
        print("Invalid query id, please input 1~8")
        sys.exit() 
    cur_path=os.getcwd()
    query_path = cur_path+"/../query/mf/Q"+query_id+"_mf.sh"
    mf_output_path = cur_path+"/../temp/mf_Q"+query_id
    if query_id in ("1","2","3"):
        if scale not in ("0.01","0.05","0.1","0.5","1","5","10"):
            print("Invalid scale, please input 0.01/0.05/0.1/0.5/1/5/10")
            sys.exit()
        if scale=="0.01":
            scale_t = "0_01"
        if scale=="0.05":
            scale_t ="0_05"
        if scale=="0.1":
            scale_t = "0_1"
        if scale=="0.5":
            scale_t = "0_5"
        if scale=="1":
            scale_t ="1"
        if scale=="5":
            scale_t = "5"
        if scale=="10":
            scale_t = "10"
        mf_output_path = mf_output_path+"_"+scale_t
        
    mf_output_path = mf_output_path+".txt"
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    queries = open(query_path,'r')
    mf_results = open(mf_output_path,'w')
    
    if query_id=="1":
        SolveQ1()
    if query_id=="2":
        SolveQ2()
    if query_id=="3":
        SolveQ3()
    if query_id=="4":
        SolveQ4()
    if query_id=="5":
        SolveQ5()
    if query_id=="6":
        SolveQ6()
    if query_id=="7":
        SolveQ7()
    if query_id=="8":
        SolveQ8()
        
    query= "" 
    reuse_list = list(reuse.keys())
    mf_id = 0
    for line in queries.readlines():
        query = query+line
        if ";" in query:
            query = query.replace('\n'," ")
            cur.execute(query)
            if "create" in query:
                query= ""
                continue;
            if "Create" in query:
                query= ""
                continue; 
            if "CREATE" in query:
                query= ""
                continue;
            while mf_id in reuse_list:
                mf = mfs[reuse[mf_id]]
                mfs.append(mf)
                mf_id +=1
            query= ""
            mf = cur.fetchone()
            mf = int(mf[0])
            mfs.append(mf)
            mf_id += 1
    con.commit()
    con.close() 

    for i in range(len(from_to_relations)):
        from_to = from_to_relations[i]
        mf = mfs[i]
        mf_results.write(str(from_to[0])+" "+str(from_to[1])+" "+str(mf)+"\n")
    
    
    
if __name__ == "__main__":
   main(sys.argv[1:])


