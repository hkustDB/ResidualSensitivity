# -*- coding: utf-8 -*-
import sys, getopt
import os
import subprocess
import numpy as np
import time



repeat_times = 10
query_time = np.zeros(8)
mf_time = np.zeros(8)
TE_time = np.zeros(8)
ela_time = np.zeros(8)
res_time = np.zeros(8)
ela_time_total = np.zeros(8)
res_time_total = np.zeros(8)



def main(argv):
    database_name = ''
    try:
        opts, args = getopt.getopt(argv,"hD:",["Database="])
    except getopt.GetoptError:
        print("CompareRunningTime.py -D <Database name>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Compare -D <Database name>")
            sys.exit()
        elif opt in ("-D","--Database"):
            database_name = arg
            
    cur_path=os.getcwd()
    cmd = "python "+cur_path+"/ImportDataToDB.py -d TPCH -s 1 -D "+database_name
    subprocess.run(cmd, shell=True)
    for i in range(3):
        query_id = str(i+1)
        cmd = "python "+cur_path+"/CollectTE.py -s 1 -Q "+query_id+" -D "+database_name
        start = time.time()
        for j in range(repeat_times):
            shell = os.popen(cmd, 'r')
            shell.read()
            shell.close()
        end=time.time()
        TE_time[i] = end-start
        TE_time[i]/=repeat_times

        start = time.time()
        cmd = "python "+cur_path+"/Collectmf.py -s 1 -Q "+query_id+" -D "+database_name
        for j in range(repeat_times):
            shell = os.popen(cmd, 'r')
            shell.read()
            shell.close()
        end=time.time()
        mf_time[i] = end-start
        mf_time[i]/=repeat_times
        
        start = time.time()
        cmd = "python "+cur_path+"/CollectQueryResult.py -s 1 -Q "+query_id+" -D "+database_name
        for j in range(repeat_times):
            shell = os.popen(cmd, 'r')
            shell.read()
            shell.close()
        end=time.time()
        query_time[i] = end-start
        query_time[i]/=repeat_times
    cmd = "python "+cur_path+"/ExportDataFromDB.py -d TPCH -D "+database_name
    subprocess.run(cmd, shell=True)
    
    cmd = "python "+cur_path+"/ImportDataToDB.py -d Facebook -D "+database_name
    subprocess.run(cmd, shell=True)
    
    for i in range(5):
        query_id = str(i+4)
        cmd = "python "+cur_path+"/CollectTE.py -Q "+query_id+" -D "+database_name
        start = time.time()
        for j in range(repeat_times):
            shell = os.popen(cmd, 'r')
            shell.read()
            shell.close()
        end=time.time()
        TE_time[i+3] = end-start
        TE_time[i+3]/=repeat_times

        start = time.time()
        cmd = "python "+cur_path+"/Collectmf.py -Q "+query_id+" -D "+database_name
        for j in range(repeat_times):
            shell = os.popen(cmd, 'r')
            shell.read()
            shell.close()
        end=time.time()
        mf_time[i+3] = end-start
        mf_time[i+3]/=repeat_times
        
        start = time.time()
        cmd = "python "+cur_path+"/CollectQueryResult.py -Q "+query_id+" -D "+database_name
        for j in range(repeat_times):
            shell = os.popen(cmd, 'r')
            shell.read()
            shell.close()
        end=time.time()
        query_time[i+3] = end-start
        query_time[i+3]/=repeat_times
    cmd = "python "+cur_path+"/ExportDataFromDB.py -d Facebook -D "+database_name
    subprocess.run(cmd, shell=True)
    
    for i in range(8):
        query_id = str(i+1)
        beta = str(0.01*2**j)
        
        start = time.time()
        for j in range(7):
            cmd = "python "+cur_path+"/ComputeRS.py -s 1 -Q "+query_id+" -B "+beta
            for j in range(repeat_times):
                shell = os.popen(cmd, 'r')
                shell.read()
                shell.close()
        end=time.time()
        res_time[i] = end - start
        res_time[i] /= (7*repeat_times)
        
        start = time.time()
        for j in range(7):
            cmd = "python "+cur_path+"/ComputeES.py -s 1 -Q "+query_id+" -B "+beta
            for j in range(repeat_times):
                shell = os.popen(cmd, 'r')
                shell.read()
                shell.close()
        end=time.time()
        ela_time[i] = end - start
        ela_time[i] /= (7*repeat_times)
    
    for i in range(8):
        print("Query"+str(i+1))
        print("The Running Time for Residual Sensitivity: "+str(TE_time[i]+query_time[i]+res_time[i]))
        print("The Running Time for Elastic Sensitivity: "+str(mf_time[i]+query_time[i]+ela_time[i]))
    

        
if __name__ == "__main__":
   main(sys.argv[1:])
