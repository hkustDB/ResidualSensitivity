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
    res_cau = np.zeros((8,8))
    ela_cau = np.zeros((8,8))
    res_lap = np.zeros((8,8))
    ela_lap = np.zeros((8,8))
    query_res = np.zeros(8)
    cmd = ""
    for i in range(8):
        scale_t = ""
        if i<3:
            scale_t = "_1"
        query_id = str(i+1)
        query_res_path = cur_path+"/../temp/query_Q"+query_id+scale_t+".txt"
        query_res_in = open(query_res_path,'r')
        res = query_res_in.read()
        res = res.split()
        query_res[i] = res[0]
        
        for j in range(8):
            epsilon = 0.1*2**j
            delta = 0
            beta = str(epsilon/10)
            factor = 10
            if(query_id=="1" or query_id=="2"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 5 -P 10000 -B "+beta
            if(query_id=="3"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 6 -P 110000 -B "+beta
            if(query_id=="4"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 5 -P 00000 -B "+beta
            if(query_id=="5"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 3 -P 000 -B "+beta
            if(query_id=="6"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 4 -P 0000 -B "+beta
            if(query_id=="7"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 5 -P 00000 -B "+beta
            if(query_id=="8"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 4 -P 0000 -B "+beta
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
            ela_cau[i][j] = res[0]
            ela_cau[i][j] = ela_cau[i][j]*factor/epsilon
            shell.close()
            
            factor = 2
            if i<3 or i==7:
                delta = pow(0.1,9);
            else:
                delta = pow(0.1,7);
            beta = str(1.0*epsilon/math.log(2.0/delta)/2)
            if(query_id=="1" or query_id=="2"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 5 -P 10000 -B "+beta
            if(query_id=="3"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 6 -P 110000 -B "+beta
            if(query_id=="4"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 5 -P 00000 -B "+beta
            if(query_id=="5"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 3 -P 000 -B "+beta
            if(query_id=="6"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 4 -P 0000 -B "+beta
            if(query_id=="7"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 5 -P 00000 -B "+beta
            if(query_id=="8"):
                cmd = cur_path+"/RSESCalculator/RSESCalculator -T 0 -Q "+query_id+" -I "+cur_path+"/../temp/TE_Q"+query_id+scale_t+".txt -n 4 -P 0000 -B "+beta
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
            ela_lap[i][j] = res[0]
            ela_lap[i][j] = ela_lap[i][j]*factor/epsilon*1.4
            shell.close()
         
    level1=1
    level2=0.1   
    x=[0.1,0.2,0.4,0.8,1.6,3.2,6.4,12.8]
    fig, axes = plt.subplots(2,4, figsize=(36, 12))
    axes[0,0].axhline(y=level2*query_res[0],ls="-",c='black',alpha=0.39)
    axes[0,0].axhline(y=level1*query_res[0],ls="-",c='black',alpha=0.39)
    axes[0,0].tick_params(axis='both', which='major', labelsize=15)
    axes[0,0].set_facecolor("white")
    axes[0,0].axhspan(level2*query_res[0], level1*query_res[0], facecolor=plt.cm.tab20c(19), alpha=0.39,label='Utility')
    axes[0,0].axhspan(0,level2*query_res[0], facecolor=plt.cm.tab20c(18), alpha=0.39,label='High Utility')
    axes[0,0].plot(x, res_cau[0],linewidth = 3, linestyle = '-',label='R_Cau',
        marker = 'o',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(12))
    axes[0,0].plot(x, res_lap[0],linewidth = 3, linestyle = '-',label='R_Lap',
        marker = 's',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(13))
    axes[0,0].plot(x, ela_cau[0],linewidth = 3, linestyle = '-',label='E_Cau',
        marker = 'v',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(18))
    axes[0,0].plot(x, ela_lap[0],linewidth = 3, linestyle = '-',label='E_Lap',
        marker = '^',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(19))
    axes[0,0].set_yscale('log')
    axes[0,0].set_xscale('log')
    axes[0,0].set_title('q1',fontsize=23)
    axes[0,0].set_ylabel("Noise Level",fontsize=23)
    axes[0,0].legend(bbox_to_anchor=(0.06, 0.35, 1, 1),fontsize=19,ncol=3, facecolor="white")



    axes[0,1].axhline(y=level2*query_res[1],ls="-",c='black',alpha=0.39)
    axes[0,1].axhline(y=level1*query_res[1],ls="-",c='black',alpha=0.39)
    axes[0,1].set_facecolor("white")
    axes[0,1].tick_params(axis='both', which='major', labelsize=15)
    axes[0,1].axhspan(level2*query_res[1], level1*query_res[1], facecolor=plt.cm.tab20c(19), alpha=0.39,label='Utility')
    axes[0,1].axhspan(0,level2*query_res[1], facecolor=plt.cm.tab20c(18), alpha=0.39,label='High Utility')
    axes[0,1].plot(x, res_cau[1],linewidth = 3, linestyle = '-',label='R_Cau',
        marker = 'o',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(12))
    axes[0,1].plot(x, res_lap[1],linewidth = 3, linestyle = '-',label='R_Lap',
        marker = 's',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(13))
    axes[0,1].plot(x, ela_cau[1],linewidth = 3, linestyle = '-',label='E_Cau',
        marker = 'v',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(18))
    axes[0,1].plot(x, ela_lap[1],linewidth = 3, linestyle = '-',label='E_Lap',
        marker = '^',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(19))
    axes[0,1].set_yscale('log')
    axes[0,1].set_xscale('log')
    axes[0,1].set_title('q2',fontsize=23)



    axes[0,2].axhline(y=level2*query_res[2],ls="-",c='black',alpha=0.39)
    axes[0,2].axhline(y=level1*query_res[2],ls="-",c='black',alpha=0.39)
    axes[0,2].set_facecolor("white")
    axes[0,2].tick_params(axis='both', which='major', labelsize=15)
    axes[0,2].axhspan(level2*query_res[2], level1*query_res[2], facecolor=plt.cm.tab20c(19), alpha=0.39,label='Utility')
    axes[0,2].axhspan(0,level2*query_res[2], facecolor=plt.cm.tab20c(18), alpha=0.39,label='High Utility')
    axes[0,2].plot(x, res_cau[2],linewidth = 3, linestyle = '-',label='R_Cau',
        marker = 'o',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(12))
    axes[0,2].plot(x, res_lap[2],linewidth = 3, linestyle = '-',label='R_Lap',
        marker = 's',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(13))
    axes[0,2].plot(x, ela_cau[2],linewidth = 3, linestyle = '-',label='E_Cau',
        marker = 'v',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(18))
    axes[0,2].plot(x, ela_lap[2],linewidth = 3, linestyle = '-',label='E_Lap',
        marker = '^',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(19))
    axes[0,2].set_yscale('log')
    axes[0,2].set_xscale('log')
    axes[0,2].set_title('q3',fontsize=23)



    axes[0,3].axhline(y=level2*query_res[3],ls="-",c='black',alpha=0.39)
    axes[0,3].axhline(y=level1*query_res[3],ls="-",c='black',alpha=0.39)
    axes[0,3].set_facecolor("white")
    axes[0,3].tick_params(axis='both', which='major', labelsize=15)
    axes[0,3].axhspan(level2*query_res[3], level1*query_res[3], facecolor=plt.cm.tab20c(19), alpha=0.39,label='Utility')
    axes[0,3].axhspan(0,level2*query_res[3], facecolor=plt.cm.tab20c(18), alpha=0.39,label='High Utility')
    axes[0,3].plot(x, res_cau[3],linewidth = 3, linestyle = '-',label='R_Cau',
        marker = 'o',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(12))
    axes[0,3].plot(x, res_lap[3],linewidth = 3, linestyle = '-',label='R_Lap',
        marker = 's',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(13))
    axes[0,3].plot(x, ela_cau[3],linewidth = 3, linestyle = '-',label='E_Cau',
        marker = 'v',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(18))
    axes[0,3].plot(x, ela_lap[3],linewidth = 3, linestyle = '-',label='E_Lap',
        marker = '^',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(19))
    axes[0,3].set_yscale('log')
    axes[0,3].set_xscale('log')
    axes[0,3].set_title('q4',fontsize=23)



    axes[1,0].axhline(y=level2*query_res[4],ls="-",c='black',alpha=0.39)
    axes[1,0].axhline(y=level1*query_res[4],ls="-",c='black',alpha=0.39)
    axes[1,0].set_facecolor("white")
    axes[1,0].tick_params(axis='both', which='major', labelsize=15)
    axes[1,0].axhspan(level2*query_res[4], level1*query_res[4], facecolor=plt.cm.tab20c(19), alpha=0.39,label='Utility')
    axes[1,0].axhspan(0,level2*query_res[4], facecolor=plt.cm.tab20c(18), alpha=0.39,label='High Utility')
    axes[1,0].plot(x, res_cau[4],linewidth = 3, linestyle = '-',label='R_Cau',
        marker = 'o',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(12))
    axes[1,0].plot(x, res_lap[4],linewidth = 3, linestyle = '-',label='R_Lap',
        marker = 's',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(13))
    axes[1,0].plot(x, ela_cau[4],linewidth = 3, linestyle = '-',label='E_Cau',
        marker = 'v',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(18))
    axes[1,0].plot(x, ela_lap[4],linewidth = 3, linestyle = '-',label='E_Lap',
        marker = '^',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(19))
    axes[1,0].set_yscale('log')
    axes[1,0].set_xscale('log')
    axes[1,0].set_title('q5',fontsize=23)
    axes[1,0].set_ylabel("Noise Level",fontsize=23)
    axes[1,0].set_ylim([10, 5*10**7])
    axes[1,0].set_xlabel("value of \u03B5",fontsize=23)


    axes[1,1].axhline(y=level2*query_res[5],ls="-",c='black',alpha=0.39)
    axes[1,1].axhline(y=level1*query_res[5],ls="-",c='black',alpha=0.39)
    axes[1,1].set_facecolor("white")
    axes[1,1].tick_params(axis='both', which='major', labelsize=15)
    axes[1,1].axhspan(0,level2*query_res[5], facecolor=plt.cm.tab20c(18), alpha=0.39,label='High Utility')
    axes[1,1].axhspan(level2*query_res[5], level1*query_res[5], facecolor=plt.cm.tab20c(19), alpha=0.39,label='Utility')
    axes[1,1].plot(x, res_cau[5],linewidth = 3, linestyle = '-',label='R_Cau',
        marker = 'o',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(12))
    axes[1,1].plot(x, res_lap[5],linewidth = 3, linestyle = '-',label='R_Lap',
        marker = 's',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(13))
    axes[1,1].plot(x, ela_cau[5],linewidth = 3, linestyle = '-',label='E_Cau',
        marker = 'v',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(18))
    axes[1,1].plot(x, ela_lap[5],linewidth = 3, linestyle = '-',label='E_Lap',
        marker = '^',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(19))
    axes[1,1].set_yscale('log')
    axes[1,1].set_xscale('log')
    axes[1,1].set_title('q6',fontsize=23)
    axes[1,1].set_ylim([100, 2.5*10**10])
    axes[1,1].set_xlabel("value of \u03B5",fontsize=23)


    axes[1,2].axhline(y=level2*query_res[6],ls="-",c='black',alpha=0.39)
    axes[1,2].axhline(y=level1*query_res[6],ls="-",c='black',alpha=0.39)
    axes[1,2].set_facecolor("white")
    axes[1,2].tick_params(axis='both', which='major', labelsize=15)
    axes[1,2].axhspan(5000,level2*query_res[6], facecolor=plt.cm.tab20c(18), alpha=0.39,label='High Utility')
    axes[1,2].axhspan(level2*query_res[6], level1*query_res[6], facecolor=plt.cm.tab20c(19), alpha=0.39,label='Utility')
    axes[1,2].plot(x, res_cau[6],linewidth = 3, linestyle = '-',label='R_Cau',
        marker = 'o',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(12))
    axes[1,2].plot(x, res_lap[6],linewidth = 3, linestyle = '-',label='R_Lap',
        marker = 's',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(13))
    axes[1,2].plot(x, ela_cau[6],linewidth = 3, linestyle = '-',label='E_Cau',
        marker = 'v',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(18))
    axes[1,2].plot(x, ela_lap[6],linewidth = 3, linestyle = '-',label='E_Lap',
        marker = '^',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(19))
    axes[1,2].set_yscale('log')
    axes[1,2].set_xscale('log')
    axes[1,2].set_title('q7',fontsize=23)
    axes[1,2].set_ylim([5000, 1.5*10**13])
    axes[1,2].set_xlabel("value of \u03B5",fontsize=23)


    axes[1,3].axhline(y=level2*query_res[7],ls="-",c='black',alpha=0.39)
    axes[1,3].axhline(y=level1*query_res[7],ls="-",c='black',alpha=0.39)
    axes[1,3].set_facecolor("white")
    axes[1,3].tick_params(axis='both', which='major', labelsize=15)
    axes[1,3].axhspan(0,level2*query_res[7], facecolor=plt.cm.tab20c(18), alpha=0.39,label='High Utility')
    axes[1,3].axhspan(level2*query_res[7], level1*query_res[7], facecolor=plt.cm.tab20c(19), alpha=0.39,label='Utility')
    axes[1,3].plot(x, res_cau[7],linewidth = 3, linestyle = '-',label='R_Cau',
        marker = 'o',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(12))
    axes[1,3].plot(x, res_lap[7],linewidth = 3, linestyle = '-',label='R_Lap',
        marker = 's',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(13))
    axes[1,3].plot(x, ela_cau[7],linewidth = 3, linestyle = '-',label='E_Cau',
        marker = 'v',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(18))
    axes[1,3].plot(x, ela_lap[7],linewidth = 3, linestyle = '-',label='E_Lap',
        marker = '^',markersize = 11,markeredgecolor='black',color=plt.cm.tab20(19))
    axes[1,3].set_yscale('log')
    axes[1,3].set_xscale('log')
    axes[1,3].set_title('q8',fontsize=23)
    axes[1,3].set_xlabel("value of \u03B5",fontsize=23)
    axes[1,3].set_ylim([4.6, 1.8*10**10])
    plt.savefig(cur_path+"/../figure/fig6.pdf")        
    
    
    
if __name__ == "__main__":
   main(sys.argv[1:])
