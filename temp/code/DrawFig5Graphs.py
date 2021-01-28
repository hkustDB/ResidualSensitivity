# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sys
import getopt
import os
import math



def main(argv):
    try:
        opts, args = getopt.getopt(argv,"h:")
    except getopt.GetoptError:
        print("DrawFig6Graphs.py")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("DrawFig6Graphs.py")
            sys.exit()
            
    cur_path=os.getcwd()
    res_cau = np.zeros((3,7))
    ela_cau = np.zeros((3,7))
    res_lap = np.zeros((3,7))
    ela_lap = np.zeros((3,7))
    query_res = np.zeros((3,7))
    scale_list = ["0_01","0_05","0_1","0_5","1","5","10"]
    delta_list = [0.1**7,0.1**7/5,0.1**8,0.1**8/5,0.1**9,0.1**9/5,0.1**10]
    cmd = ""
    
    for i in range(3):
        query_id = str(i+1)
        for j in range(7):
            scale_t = scale_list[j]
            scale_t = "_"+scale_t
            epsilon = 0.8
            delta = delta_list[j]
            
            beta = str(epsilon/10)
            factor = 10
            if(query_id=="1" or query_id=="2"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 5 -P 10000 -B "+beta
            if(query_id=="3"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 6 -P 110000 -B "+beta
            shell = os.popen(cmd, 'r')
            res = shell.read()
            res = res.split()
            res_cau[i][j] = res[0]
            res_cau[i][j] = res_cau[i][j]*factor/epsilon
            shell.close()
            
            if(query_id=="1" or query_id=="2"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 5 -P 10000 -B "+beta
            if(query_id=="3"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 6 -P 110000 -B "+beta
            shell = os.popen(cmd, 'r')
            res = shell.read()
            res = res.split()
            ela_cau[i][j] = res[0]
            ela_cau[i][j] = ela_cau[i][j]*factor/epsilon
            shell.close()
            
            factor = 2
            beta = str(1.0*epsilon/math.log(2.0/delta)/2)
            if(query_id=="1" or query_id=="2"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 5 -P 10000 -B "+beta
            if(query_id=="3"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 6 -P 110000 -B "+beta
            shell = os.popen(cmd, 'r')
            res = shell.read()
            res = res.split()
            res_lap[i][j] = res[0]
            res_lap[i][j] = res_lap[i][j]*factor/epsilon*1.4
            shell.close()
            
            if(query_id=="1" or query_id=="2"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 5 -P 10000 -B "+beta
            if(query_id=="3"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 1 -Q "+query_id+" -I "+cur_path+"/../temp/mf_Q"+query_id+scale_t+".txt -n 6 -P 110000 -B "+beta
            shell = os.popen(cmd, 'r')
            res = shell.read()
            res = res.split()
            ela_lap[i][j] = res[0]
            ela_lap[i][j] = ela_lap[i][j]*factor/epsilon*1.4
            shell.close()
            
            query_res_path = cur_path+"/../temp/query_Q"+query_id+scale_t+".txt"
            query_res_in = open(query_res_path,'r')
            res = query_res_in.read()
            res = res.split()
            query_res[i][j] = res[0]
            
    eva_time=np.zeros((3,7))
    elastic_time=np.zeros((3,7))
    residual_time=np.zeros((3,7))
    fin = open(cur_path+"/../temp/fig5_runnningtime_info.txt",'r')
    j=0
    i = 0
    for line in fin.readlines():
        text=line.split()
        if j%3==0:
            eva_time[0][i] = text[0]
            eva_time[1][i] = text[1]
            eva_time[2][i] = text[2]
        elif j%3==1:
            elastic_time[0][i] = text[0]
            elastic_time[1][i] = text[1]
            elastic_time[2][i] = text[2]
        else:
            residual_time[0][i] = text[0]
            residual_time[1][i] = text[1]
            residual_time[2][i] = text[2]
            i+=1
        j+=1

    plt.rcParams['axes.facecolor']='white'
    fig, axes = plt.subplots(2,3, figsize=(26, 8))
    x=[0.01,0.05,0.1,0.5,1,5,10]
    
    axes[0,0].axhline(y=10000,ls="-",c=plt.cm.tab20c(19))
    axes[0,0].axhline(y=100000,ls="-",c=plt.cm.tab20c(19))
    axes[0,0].axhline(y=1000000,ls="-",c=plt.cm.tab20c(19))
    axes[0,0].axhline(y=10000000,ls="-",c=plt.cm.tab20c(19))
    axes[0,0].tick_params(axis='both', which='major', labelsize=15)
    axes[0,0].plot(x, res_cau[0],linewidth = 2.5, linestyle = '-.',label='R_Cau',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[0,0].plot(x, res_lap[0],linewidth = 2.5,linestyle = '-.',label='R_Lap',
        marker = 's',markersize = 8,color=plt.cm.tab20c(12),
        markeredgecolor=plt.cm.tab20c(12),markeredgewidth = 2,markerfacecolor='w')
    axes[0,0].plot(x, query_res[0],linewidth = 2.5,linestyle = ':',label='Query',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[0,0].plot(x, ela_cau[0],linewidth = 2.5, linestyle = '--',label='E_Cau',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[0,0].plot(x, ela_lap[0],linewidth = 2.5,linestyle = '--',label='E_Lap',
        marker = 'v',markersize = 8,color=plt.cm.tab20b(8),
        markeredgecolor=plt.cm.tab20b(8),markeredgewidth = 2,markerfacecolor='w')
    axes[0,0].set_yscale('log')
    axes[0,0].set_xscale('log')
    axes[0,0].set_title('q1',fontsize=23)
    axes[0,0].set_ylabel("Noise Level",fontsize=23)
    axes[0,0].legend(fontsize=11,ncol=2)
    
    axes[1,0].tick_params(axis='both', which='major', labelsize=15)
    axes[1,0].axhline(y=0.1,ls="-",c=plt.cm.tab20c(19))
    axes[1,0].axhline(y=1,ls="-",c=plt.cm.tab20c(19))
    axes[1,0].axhline(y=10,ls="-",c=plt.cm.tab20c(19))
    axes[1,0].axhline(y=100,ls="-",c=plt.cm.tab20c(19))
    axes[1,0].plot(x, residual_time[0],linewidth = 2.5, linestyle = '-.',label='Residual',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(0))
    axes[1,0].plot(x, eva_time[0],linewidth = 2.5,linestyle = ':',label='Query',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(9))
    axes[1,0].plot(x, elastic_time[0],linewidth = 2.5,linestyle = '--',label='Elastic',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[1,0].set_yscale('log')
    axes[1,0].set_xscale('log')
    axes[1,0].set_ylabel("Running Time(s)",fontsize=23)
    axes[1,0].set_xlabel("Scale",fontsize=23)
    axes[1,0].legend()
    
    axes[0,1].tick_params(axis='both', which='major', labelsize=15)
    axes[0,1].axhline(y=10000,ls="-",c=plt.cm.tab20c(19))
    axes[0,1].axhline(y=100000,ls="-",c=plt.cm.tab20c(19))
    axes[0,1].axhline(y=1000000,ls="-",c=plt.cm.tab20c(19))
    axes[0,1].axhline(y=10000000,ls="-",c=plt.cm.tab20c(19))
    axes[0,1].plot(x, res_cau[1],linewidth = 2.5, linestyle = '-.',label='R_Cau',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[0,1].plot(x, res_lap[1],linewidth = 2.5,linestyle = '-.',label='R_Lap',
        marker = 's',markersize = 8,color=plt.cm.tab20c(12),
        markeredgecolor=plt.cm.tab20c(12),markeredgewidth = 2,markerfacecolor='w')
    axes[0,1].plot(x, query_res[1],linewidth = 2.5,linestyle = ':',label='Query',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[0,1].plot(x, ela_cau[1],linewidth = 2.5, linestyle = '--',label='E_Cau',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[0,1].plot(x, ela_lap[1],linewidth = 2.5,linestyle = '--',label='E_Lap',
        marker = 'v',markersize = 8,color=plt.cm.tab20b(8),
        markeredgecolor=plt.cm.tab20b(8),markeredgewidth = 2,markerfacecolor='w')
    axes[0,1].set_yscale('log')
    axes[0,1].set_xscale('log')
    axes[0,1].set_title('q2',fontsize=23)
    axes[0,1].set_ylabel("Value",fontsize=23)
    axes[0,1].legend(fontsize=11,ncol=2)
    axes[1,1].tick_params(axis='both', which='major', labelsize=15)
    axes[1,1].axhline(y=0.1,ls="-",c=plt.cm.tab20c(19))
    axes[1,1].axhline(y=1,ls="-",c=plt.cm.tab20c(19))
    axes[1,1].axhline(y=10,ls="-",c=plt.cm.tab20c(19))
    axes[1,1].axhline(y=100,ls="-",c=plt.cm.tab20c(19))
    axes[1,1].plot(x, residual_time[1],linewidth = 2.5, linestyle = '-.',label='Residual',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(0))
    
    axes[1,1].plot(x, eva_time[1],linewidth = 2.5,linestyle = ':',label='Query',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(9))
    
    axes[1,1].plot(x, elastic_time[1],linewidth = 2.5,linestyle = '--',label='Elastic',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[1,1].set_yscale('log')
    axes[1,1].set_xscale('log')
    axes[1,1].set_xlabel("Scale",fontsize=23)
    axes[1,1].legend()
    
    axes[0,2].tick_params(axis='both', which='major', labelsize=15)
    axes[0,2].axhline(y=10000,ls="-",c=plt.cm.tab20c(19))
    axes[0,2].axhline(y=100000,ls="-",c=plt.cm.tab20c(19))
    axes[0,2].axhline(y=1000000,ls="-",c=plt.cm.tab20c(19))
    axes[0,2].axhline(y=10000000,ls="-",c=plt.cm.tab20c(19))
    axes[0,2].axhline(y=100000000,ls="-",c=plt.cm.tab20c(19))
    axes[0,2].axhline(y=1000000000,ls="-",c=plt.cm.tab20c(19))
    axes[0,2].axhline(y=10000000000,ls="-",c=plt.cm.tab20c(19))
    axes[0,2].plot(x, res_cau[2],linewidth = 2.5, linestyle = '-.',label='R_Cau',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[0,2].plot(x, res_lap[2],linewidth = 2.5,linestyle = '-.',label='R_Lap',
        marker = 's',markersize = 8,color=plt.cm.tab20c(12),
        markeredgecolor=plt.cm.tab20c(12),markeredgewidth = 2,markerfacecolor='w')
    axes[0,2].plot(x, query_res[2],linewidth = 2.5,linestyle = ':',label='Query',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[0,2].plot(x, ela_cau[2],linewidth = 2.5, linestyle = '--',label='E_Cau',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[0,2].plot(x, ela_lap[2],linewidth = 2.5,linestyle = '--',label='E_Lap',
        marker = 'v',markersize = 8,color=plt.cm.tab20b(8),
        markeredgecolor=plt.cm.tab20b(8),markeredgewidth = 2,markerfacecolor='w')
    axes[0,2].set_yscale('log')
    axes[0,2].set_xscale('log')
    axes[0,2].set_title('q3',fontsize=23)
    axes[0,2].legend(fontsize=11,ncol=2)
    axes[1,2].tick_params(axis='both', which='major', labelsize=15)
    axes[1,2].axhline(y=0.1,ls="-",c=plt.cm.tab20c(19))
    axes[1,2].axhline(y=1,ls="-",c=plt.cm.tab20c(19))
    axes[1,2].axhline(y=10,ls="-",c=plt.cm.tab20c(19))
    axes[1,2].axhline(y=100,ls="-",c=plt.cm.tab20c(19))
    axes[1,2].plot(x, residual_time[2],linewidth = 2.5, linestyle = '-.',label='Residual',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(0))
    axes[1,2].plot(x, eva_time[2],linewidth = 2.5,linestyle = ':',label='Query',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(9))
    axes[1,2].plot(x, elastic_time[2],linewidth = 2.5,linestyle = '--',label='Elastic',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[1,2].set_yscale('log')
    axes[1,2].set_xscale('log')
    axes[1,2].set_xlabel("Scale",fontsize=23)
    axes[1,2].legend()
    plt.savefig(cur_path+"/../figure/fig5.pdf")  
       
    
    
if __name__ == "__main__":
   main(sys.argv[1:])