# -*- coding: utf-8 -*-
import psycopg2
import sys, getopt
import os



TE_dic = {}
E_list = []
TE_from = {}



def SolveQ1():
    E_list.append("10000")
    E_list.append("11000")
    E_list.append("10100")
    E_list.append("10010")
    E_list.append("10001")
    E_list.append("11100")
    E_list.append("11010")
    E_list.append("11001")
    E_list.append("10110")
    E_list.append("10101")
    E_list.append("10011")
    E_list.append("11110")
    E_list.append("11101")
    E_list.append("11011")
    E_list.append("10111")
    TE_from["11010"] = ["11000","10010"]
    TE_from["11001"] = ["11000","10001"]
    TE_from["10101"] = ["10000","10100","10001"]
    TE_from["11101"] = ["11100","10001"]
    TE_from["11011"] = ["11000","10011"]
    
    

def SolveQ2():
    E_list.append("10000")
    E_list.append("11000")
    E_list.append("10100")
    E_list.append("10010")
    E_list.append("10001")
    E_list.append("11100")
    E_list.append("11010")
    E_list.append("11001")
    E_list.append("10110")
    E_list.append("10101")
    E_list.append("10011")
    E_list.append("11110")
    E_list.append("11101")
    E_list.append("11011")
    E_list.append("10111")
    TE_from["11001"] = ["11000","10001"]
    TE_from["10101"] = ["10000","10100","10001"]
    TE_from["11101"] = ["11100","10001"]
    
    
    
def SolveQ3():
    E_list.append("110000")
    E_list.append("111000")
    E_list.append("110100")
    E_list.append("110010")
    E_list.append("110001")
    E_list.append("111100")
    E_list.append("111010")
    E_list.append("111001")
    E_list.append("110110")
    E_list.append("110101")
    E_list.append("110011")
    E_list.append("111110")
    E_list.append("111101")
    E_list.append("111011")
    E_list.append("110111")
    TE_from["111010"] = ["111000","110010"]
    TE_from["110101"] = ["110100","110001"]
    
  
    
def SolveQ4():
    E_list.append("10000")
    E_list.append("01000")
    E_list.append("00100")
    E_list.append("00010")
    E_list.append("00001")
    E_list.append("11000")
    E_list.append("10100")
    E_list.append("10010")
    E_list.append("10001")
    E_list.append("01100")
    E_list.append("01010")
    E_list.append("01001")
    E_list.append("00110")
    E_list.append("00101")
    E_list.append("00011")
    E_list.append("11100")
    E_list.append("11010")
    E_list.append("11001")
    E_list.append("10110")
    E_list.append("10101")
    E_list.append("10011")
    E_list.append("01110")
    E_list.append("01101")
    E_list.append("01011")
    E_list.append("00111")
    E_list.append("11110")
    E_list.append("11101")
    E_list.append("11011")
    E_list.append("10111")
    E_list.append("01111")
    TE_from["10100"] = ["10000","00100"]
    TE_from["10010"] = ["10000","00010"]
    TE_from["10001"] = ["10000","00001"]
    TE_from["01010"] = ["01000","00010"]
    TE_from["01001"] = ["01000","00001"]
    TE_from["00101"] = ["00100","00001"]
    TE_from["11010"] = ["11000","00010"]
    TE_from["11001"] = ["11000","00001"]
    TE_from["10110"] = ["10000","00110"]
    TE_from["10101"] = ["10000","00100","00001"]
    TE_from["10011"] = ["10000","00011"]
    TE_from["01101"] = ["01100","00001"]
    TE_from["01011"] = ["01000","00011"]
    TE_from["11101"] = ["11100","00001"]
    TE_from["11011"] = ["11000","00011"]
    TE_from["10111"] = ["10000","00111"]
    TE_dic["00000"] = 1
    
    
    
def SolveQ5():
    E_list.append("100")
    E_list.append("010")
    E_list.append("001")
    E_list.append("110")
    E_list.append("101")
    E_list.append("011")
    TE_dic["000"] = 1
    
    
    
def SolveQ6():
    E_list.append("1000")
    E_list.append("0100")
    E_list.append("0010")
    E_list.append("0001")
    E_list.append("1100")
    E_list.append("1010")
    E_list.append("1001")
    E_list.append("0110")
    E_list.append("0101")
    E_list.append("0011")
    E_list.append("1110")
    E_list.append("1101")
    E_list.append("1011")
    E_list.append("0111")  
    TE_from["1010"] = ["1000","0010"]
    TE_from["0101"] = ["0100","0001"]
    TE_dic["0000"] = 1
    
 

def SolveQ7():
    E_list.append("10000")
    E_list.append("01000")
    E_list.append("00100")
    E_list.append("00010")
    E_list.append("00001")
    E_list.append("11000")
    E_list.append("10100")
    E_list.append("10010")
    E_list.append("10001")
    E_list.append("01100")
    E_list.append("01010")
    E_list.append("01001")
    E_list.append("00110")
    E_list.append("00101")
    E_list.append("00011")
    E_list.append("11100")
    E_list.append("11010")
    E_list.append("11001")
    E_list.append("10110")
    E_list.append("10101")
    E_list.append("10011")
    E_list.append("01110")
    E_list.append("01101")
    E_list.append("01011")
    E_list.append("00111")
    E_list.append("11110")
    E_list.append("11101")
    E_list.append("11011")
    E_list.append("10111")
    E_list.append("01111")
    TE_from["10100"] = ["10000","00100"]
    TE_from["10010"] = ["10000","00010"]
    TE_from["01010"] = ["01000","00010"]
    TE_from["01001"] = ["01000","00001"]
    TE_from["00101"] = ["00100","00001"]
    TE_from["11010"] = ["11000","00010"]
    TE_from["10110"] = ["10000","00110"]
    TE_from["10101"] = ["10001","00100"]
    TE_from["01101"] = ["01100","00001"]
    TE_from["01011"] = ["01000","00011"]
    TE_dic["00000"] = 1
    


def SolveQ8():
    E_list.append("1000")
    E_list.append("0100")
    E_list.append("0010")
    E_list.append("0001")
    E_list.append("1100")
    E_list.append("1010")
    E_list.append("1001")
    E_list.append("0110")
    E_list.append("0101")
    E_list.append("0011")
    E_list.append("1110")
    E_list.append("1101")
    E_list.append("1011")
    E_list.append("0111") 
    TE_dic["0000"] = 1 

    
    
def main(argv):
    query_id = ''
    database_name = ''
    scale = ''
    scale_t = ''
    
    try:
        opts, args = getopt.getopt(argv,"hD:s:Q:",["Database=","scale=","Query="])
    except getopt.GetoptError:
        print("CollectTE.py -D <Database name> -s <scale:0.01/0.05/.../10> -Q <Query ID:1/2/../8>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("CollectTE.py -D <Database name> -s <scale:0.01/0.05/.../10> -Q <Query ID:1/2/../8>")
            sys.exit()
        elif opt in ("-Q", "--Query"):
            query_id = arg
        elif opt in ("-s", "--cale"):
            scale = arg
        elif opt in ("-D","--Database"):
            database_name = arg
    
    if query_id not in ("1","2","3","4","5","6","7","8"):
        print("Invalid query id, please input 1~8")
        sys.exit() 
    cur_path=os.getcwd()
    query_path = cur_path+"/../query/TE/Q"+query_id+"_TE.sh"
    clean_path = cur_path+"/../query/TE/Q"+query_id+"_TE_clean.sh"
    TE_output_path = cur_path+"/../temp/TE_Q"+query_id
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
        TE_output_path = TE_output_path+"_"+scale_t
        
    TE_output_path = TE_output_path+".txt"
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    queries = open(query_path,'r')
    clean_queries = open(clean_path,'r')
    TE_results = open(TE_output_path,'w')
    
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
    pass_E_list = list(TE_from.keys())
    E_id = 0
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
            query= ""
            TE = cur.fetchone()
            TE = int(TE[0])
            E = E_list[E_id]
            while E in pass_E_list:
                from_list = TE_from[E]
                res = 1
                for E_t in from_list:
                    res =res*TE_dic[E_t]
                TE_dic[E] = res
                E_id += 1
                E = E_list[E_id]
            TE_dic[E] = TE
            E_id += 1
    
    for line in clean_queries.readlines():
        query = query+line
        if ";" in query:
            query = query.replace('\n'," ")
            cur.execute(query)
            query= ""
    con.commit()
    con.close()
    
    for E in TE_dic.keys():
        intE = int(E,2)
        intE = intE+1-1
        TE_results.write(str(intE)+" "+str(TE_dic[E])+"\n")
 
    
    
if __name__ == "__main__":
   main(sys.argv[1:])


