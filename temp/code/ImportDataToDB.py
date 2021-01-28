# -*- coding: utf-8 -*-
import psycopg2
import sys, getopt
import os



def main(argv):
    dataset = ''
    scale = ''
    database_name = ''
    
    try:
        opts, args = getopt.getopt(argv,"hd:s:D:",["dataset=","scale=","Database="])
    except getopt.GetoptError:
        print("ImportDataToDB.py -d <dataset:TPCH/Facebook> -s <scale:0.01/0.05/.../10> -D <database name>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("ImportDataToDB.py -d <dataset:TPCH/Facebook> -s <scale:0.01/0.05/.../10> -D <database name>")
            sys.exit()
        elif opt in ("-d", "--dataset"):
            dataset = arg
        elif opt in ("-s", "--scale"):
            scale = arg
        elif opt in ("-D","--Database"):
            database_name = arg
    
    if dataset not in ("TPCH","Facebook"):
        print("Invalid dataset, please input TPCH/Facebook")
        sys.exit()
    if dataset=="TPCH":
        if scale not in ("0.01","0.05","0.1","0.5","1","5","10"):
            print("Invalid scale, please input 0.01/0.05/0.1/0.5/1/5/10")
            sys.exit()
    cur_path=os.getcwd()
    data_path = cur_path+"/../data"
    shell_path = cur_path+"/../dss/"
    
    if dataset=="TPCH":
        data_path = data_path+"/TPCH/scale_"
        if scale=="0.01":
            data_path = data_path+"0_01/"
        if scale=="0.05":
            data_path = data_path+"0_05/"
        if scale=="0.1":
            data_path = data_path+"0_1/"
        if scale=="0.5":
            data_path = data_path+"0_5/"
        if scale=="1":
            data_path = data_path+"1/"
        if scale=="5":
            data_path = data_path+"5/"
        if scale=="10":
            data_path = data_path+"10/"
    if dataset=="Facebook":
        data_path = data_path+"/Facebook/"

    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    if dataset=="TPCH":
        ddl = open(shell_path+"TPCH_dss.ddl",'r')
        code = ""
        for line in ddl.readlines():
            code = code+line
            if ";" in code:
                code = code.replace('\n'," ")
                cur.execute(code)
                code = ""
        
        import_data = open(shell_path+"TPCH_import.sh",'r')
        for line in import_data.readlines():
            code = code+line
            if ";" in code:
                code = code.replace('\n'," ")
                code = code.replace('$$$/',data_path)
                cur.execute(code)
                code = ""
        
        ri = open(shell_path+"TPCH_dss.ri",'r')
        code = ""
        for line in ri.readlines():
            code = code+line
            if ";" in code:
                code = code.replace('\n'," ")
                cur.execute(code)
                code = ""
                
    if dataset=="Facebook":
        ddl = open(shell_path+"Facebook_dss.ddl",'r')
        code = ""
        for line in ddl.readlines():
            code = code+line
            if ";" in code:
                code = code.replace('\n'," ")
                cur.execute(code)
                code = ""
        
        import_data = open(shell_path+"Facebook_import.sh",'r')
        for line in import_data.readlines():
            code = code+line
            if ";" in code:
                code = code.replace('\n'," ")
                code = code.replace('$$$/',data_path)
                cur.execute(code)
                code = ""
        
        ri = open(shell_path+"Facebook_dss.ri",'r')
        code = ""
        for line in ri.readlines():
            code = code+line
            if ";" in code:
                code = code.replace('\n'," ")
                cur.execute(code)
                code = ""
    con.commit()
    con.close()
    
    
    
if __name__ == "__main__":
   main(sys.argv[1:])