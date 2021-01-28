# -*- coding: utf-8 -*-
import psycopg2
import sys, getopt
import os



def main(argv):    
    query_id = ''
    database_name = ''
    scale = ''
    scale_t = ''
    
    try:
        opts, args = getopt.getopt(argv,"hD:s:Q:",["Database=","scale=","Query="])
    except getopt.GetoptError:
        print("CollectQueryResult.py -D <Database name> -s <scale:0.01/0.05/.../10> -Q <Query ID:1/2/../8>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("CollectQueryResult.py -D <Database name> -s <scale:0.01/0.05/.../10> -Q <Query ID:1/2/../8>")
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
    query_path = cur_path+"/../query/query_result/Q"+query_id+".sh"
    res_output_path = cur_path+"/../temp/query_Q"+query_id
    
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
        res_output_path = res_output_path+"_"+scale_t
    res_output_path = res_output_path+".txt"
    
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    queries = open(query_path,'r')
    result = open(res_output_path,'w')
            
    query= "" 
    mf_id = 0
    res = 0
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
            if "drop" in query:
                query= ""
                continue;
            if "Drop" in query:
                query= ""
                continue; 
            if "DROP" in query:
                query= ""
                continue;
            query= ""
            res = cur.fetchone()
            res = int(res[0])
            mf_id += 1
    con.commit()
    con.close() 
    result.write(str(res))


    
if __name__ == "__main__":
   main(sys.argv[1:])