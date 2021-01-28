# -*- coding: utf-8 -*-
import sys, getopt
import os



def main(argv):
    query_id = ''
    beta = ''
    scale = ''
    scale_t = ''
    
    try:
        opts, args = getopt.getopt(argv,"h:s:Q:B:",["scale=","Query=","Beta="])
    except getopt.GetoptError:
        print("ComputeES.py -s <scale:0.01/0.05/.../10> -Q <Query ID:1/2/../8> -B <Beta>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("ComputeES.py -s <scale:0.01/0.05/.../10> -Q <Query ID:1/2/../8> -B <Beta>")
            sys.exit()
        elif opt in ("-s", "--scale"):
            scale = arg
        elif opt in ("-Q", "--Query"):
            query_id = arg
        elif opt in ("-B","--Beta"):
            beta = arg
    
    if query_id not in ("1","2","3","4","5","6","7","8"):
        print("Invalid query id, please input 1~8")
        sys.exit() 
        
    if query_id in ("1","2","3"):
        if scale not in ("0.01","0.05","0.1","0.5","1","5","10"):
            print("Invalid scale, please input 0.01/0.05/0.1/0.5/1/5/10")
            sys.exit()
        if scale=="0.01":
            scale_t = "_0_01"
        if scale=="0.05":
            scale_t ="_0_05"
        if scale=="0.1":
            scale_t = "_0_1"
        if scale=="0.5":
            scale_t = "_0_5"
        if scale=="1":
            scale_t ="_1"
        if scale=="5":
            scale_t = "_5"
        if scale=="10":
            scale_t = "_10"
        
    cur_path=os.getcwd()
    cmd = ""
    if(query_id=="1" or query_id=="2"):
        cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 5 -P 10000 -B "+beta
    if(query_id=="3"):
        cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 6 -P 110000 -B "+beta
    if(query_id=="4"):
        cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 5 -P 00000 -B "+beta
    if(query_id=="5"):
        cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 3 -P 000 -B "+beta
    if(query_id=="6"):
        cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 4 -P 0000 -B "+beta
    if(query_id=="7"):
        cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 5 -P 00000 -B "+beta
    if(query_id=="8"):
        cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 4 -P 0000 -B "+beta
    shell = os.popen(cmd, 'r')
    res = shell.read()
    res = res.split()
    print(res[0])
    shell.close()



if __name__ == "__main__":
   main(sys.argv[1:])