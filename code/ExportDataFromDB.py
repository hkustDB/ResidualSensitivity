# -*- coding: utf-8 -*-
import psycopg2
import sys, getopt
import os



def main(argv):
    dataset = ''
    database_name = ''
    
    try:
        opts, args = getopt.getopt(argv,"hd:D:",["dataset=","Database="])
    except getopt.GetoptError:
        print("ExportDataFromDB.py -d <dataset:TPCH/Facebook> -D <database name>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("ExportDataFromDB.py -d <dataset:TPCH/Facebook> -D <database name>")
            sys.exit()
        elif opt in ("-D","--Database"):
            database_name = arg
        elif opt in ("-d","--dataset"):
            dataset = arg
    
    if dataset not in ("TPCH","Facebook"):
        print("Invalid dataset, please input TPCH/Facebook")
        sys.exit()
    cur_path=os.getcwd()
    shell_path = cur_path+"/../dss/"
    
    con = psycopg2.connect(database=database_name)
    cur = con.cursor()
    
    clean_file = shell_path+dataset+"_clean.sh"
    clean_queries = open(clean_file,'r')
    
    code = ""
    for line in clean_queries.readlines():
        code = code+line
        if ";" in code:
            code = code.replace('\n'," ")
            cur.execute(code)
            code = ""

    con.commit()
    con.close()
   
    
    
if __name__ == "__main__":
   main(sys.argv[1:])