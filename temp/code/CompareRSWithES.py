# -*- coding: utf-8 -*-
import sys, getopt
import os
import numpy as np



def main(argv):
    try:
        opts, args = getopt.getopt(argv,"h:")
    except getopt.GetoptError:
        print("CompareRSWithRSWithES.py")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("CompareRSWithRSWithES.py")
            sys.exit()
    cur_path=os.getcwd()
    
    residual = np.zeros((8,7))
    elastic = np.zeros((8,7))
    ratio = np.zeros((8,7))
    query_res = np.zeros((8))
    cmd = ""
    
    for i in range(8):
        query_id = str(i+1)
        for j in range(7):
            beta = str(0.01*2**j)
            cmd = "python "+cur_path+"/ComputeRS.py -s 1 -Q "+query_id+" -B "+beta
            shell = os.popen(cmd, 'r')
            res = shell.read()
            res = res.split()
            residual[i][j] = res[0]
            shell.close()
            cmd = "python "+cur_path+"/ComputeES.py -s 1 -Q "+query_id+" -B "+beta
            shell = os.popen(cmd, 'r')
            res = shell.read()
            res = res.split()
            elastic[i][j] = res[0]
            shell.close()
            ratio[i][j] = elastic[i][j]/residual[i][j]
            query_res_path = ""
            if i<3:
                query_res_path = cur_path+"/../temp/query_Q"+query_id+"_1.txt"
            else:
                query_res_path = cur_path+"/../temp/query_Q"+query_id+".txt"
            query_results = open(query_res_path,'r')
            res = query_results.read();
            res = res.split()
            query_res[i] = res[0]
    
    for i in range(8):
        print("Query"+str(i+1))
        print("Query Result Size: "+str(query_res[i]))
        print("Residual Sensitivity:")
        print("Max: "+str(max(residual[i])))
        print("Min: "+str(min(residual[i])))
        print("Elastic Sensitivity:")
        print("Max: "+str(max(elastic[i])))
        print("Min: "+str(min(elastic[i])))
        print("ES/RS:")
        print("Max: "+str(max(ratio[i])))
        print("Min: "+str(min(ratio[i])))
        print("Avg: "+str(np.mean(ratio[i])))
  
    
    
if __name__ == "__main__":
   main(sys.argv[1:])
    