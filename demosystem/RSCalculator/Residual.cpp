#include "Residual.hpp"

Residual::Residual(int n, std::string TE_file_name, std::string is_public, double beta){
    n_ = n;
    beta_ = beta;
    TE_file_name_ = TE_file_name;
    num_E_ = pow(2,n_);
    TE_ = new int[num_E_];
    for(int i = 0; i<num_E_;i++)
        TE_[i] = 0;
    is_public_ = new bool[n_];
    tuple_dis_ = new int[n_];;
    for(int i = 0; i<n_; i++){
        tuple_dis_[i] = 0;
        is_public_[i] = false;
    }
    if(is_public.length()!=n_)
        std::cerr<<"The length of indicator for public relations is not equal to number of relations"<<std::endl;
    for(int i = 0; i<n_; i++){
        if(is_public[i]=='0')
            is_public_[i]=0;
        else
            is_public_[i]=1;
    }
    ReadTE();
}

void Residual::ReadTE(){
    std::ifstream TE_file(TE_file_name_);
    int E = 0;
    int TE = 0;
    while(TE_file>>E>>TE){
        TE_[E] = TE;
    }
}

Residual::~Residual(){
    if(TE_!=NULL){
        delete[] TE_;
        TE_=NULL;
    }
    if(is_public_!=NULL){
        delete[] is_public_;
        is_public_=NULL;
    }
    if(tuple_dis_!=NULL){
        delete[] tuple_dis_;
        tuple_dis_=NULL;
    }
}

void Residual::CalM(){
    m_ = 0;
    for(int i = 0; i<n_; i++)
        if(is_public_[i]==false)
            m_++;
}

double Residual::GetRes(){
    return res_;
}

int Residual::GetKWithRes(){
    return k_with_res_;
}

int* Residual::GetTE(){
    return TE_;
}

bool* Residual::GetIsPublic(){
    return is_public_;
}

void Residual::RunResidual(){
    CalM();
    max_k_ = (m_-1)/(beta_);
    CallMaxRes();
    res_ = max_res_;
    k_with_res_ = k_with_max_res_;
}

void Residual::CallMaxRes(){
    max_res_ = 0;
    k_with_max_res_ = 0;
    //Calculate max \hatT_{[n]-i}
    for(int i = 0; i<n_; i++)
        if(is_public_[i]==false){
            deleted_id_ = i;
            CallMaxTE();
        }
}

void Residual::CallMaxTE(){
    for(int i = 0; i<n_; i++)
        tuple_dis_[i] = 0;
    int left_relation_num = m_-1;
    first_id_ = 0;
    second_id_ = 0;
    for(int i = 0; i<n_; i++)
        if(is_public_[i]==false && i!=deleted_id_){
            if(left_relation_num==2)
                first_id_=i;
            if(left_relation_num==1)
                second_id_=i;
            left_relation_num--;
        }
    CallMaxTERec(0,max_k_);
}

void Residual::CallMaxTERec(int cur_id, int left_k){
    if(cur_id==first_id_)
        CallMaxTEWithTupleDis(left_k);
    else if(cur_id==deleted_id_ || is_public_[cur_id])
        CallMaxTERec(cur_id+1, left_k);
    else
        for(int i = 0; i<=left_k; i++){
            tuple_dis_[cur_id]=i;
            CallMaxTERec(cur_id+1, left_k-i);
        }
}

void Residual::CallMaxTEWithTupleDis(int left_k){
    double a = CalCoe(0, 0, 0, 0);
    double b = CalCoe(0, 0, 1, 0);
    double c = CalCoe(0, 1, 0, 0);
    double d = CalCoe(0, 1, 1, 0);
    int assigned_k = max_k_ - left_k;
    int H = left_k;
    double t_double = 0;
    int x1 = 0;
    int x2 = 0;
    candidate_k_num_ = 0;
    int left =0;
    int right = H;
    int step = int((right-left)/20)+1;
    int t_iter = left;
    double tar_max;
    double t_res;
    int k_tar_max;
    int t_k;
    int max_res_for_each_k=0;
    int t_max_res_for_each_k = 0;
    while(step>5){
        template_list_num_=0;
        t_iter = left;
        while(t_iter<=right){
            template_list_[template_list_num_++]=t_iter;
            t_iter+=step;
        }
        tar_max = 0;
        k_tar_max = 0;
        for(int i=0; i<template_list_num_;i++){
            t_k = template_list_[i];
            if(t_k>right)
                continue;
            max_res_for_each_k = 0;
            t_double = (a * t_k + b - c)*1.0 / 2 / a;
            x1 = int(t_double);
            x2 = x1+1;
            max_res_for_each_k = b * t_k + d;
            if(c * t_k + d > max_res_for_each_k)
                max_res_for_each_k = c * t_k + d;
            if(0<x1&&x1<t_k){
                t_max_res_for_each_k = a * x1 * (t_k - x1) + b * x1 + c * (t_k - x1) + d;
                if (t_max_res_for_each_k > max_res_for_each_k)
                    max_res_for_each_k = t_max_res_for_each_k;
            }
            if(0<x2&&x2<t_k){
                t_max_res_for_each_k = a * x2 * (t_k - x2) + b * x2 + c * (t_k - x2) + d;
                if (t_max_res_for_each_k > max_res_for_each_k)
                    max_res_for_each_k = t_max_res_for_each_k;
            }
            t_res = exp(-beta_* (t_k + assigned_k)) * max_res_for_each_k;
            if (t_res > tar_max){
                tar_max = t_res;
                k_tar_max = t_k;
            }
        }
        left = std::max(left,k_tar_max-step);
        right = std::min(right,k_tar_max+step);
        step = int((right-left)/20)+1;
    }
    t_iter = left;
    while(t_iter<=right){
        candidate_k_[candidate_k_num_++]=t_iter;
        t_iter++;
    }
    tar_max = 0;
    k_tar_max = 0;
    for(int i=0; i<candidate_k_num_;i++){
        t_k = candidate_k_[i];
        max_res_for_each_k = 0;
        t_double = (a * t_k + b - c)*1.0 / 2 / a;
        x1 = int(t_double);
        x2 = x1+1;
        max_res_for_each_k = b * t_k + d;
        if(c * t_k + d > max_res_for_each_k)
            max_res_for_each_k = c * t_k + d;
        if(0<x1&&x1<t_k){
            t_max_res_for_each_k = a * x1 * (t_k - x1) + b * x1 + c * (t_k - x1) + d;
            if (t_max_res_for_each_k > max_res_for_each_k)
                max_res_for_each_k = t_max_res_for_each_k;
        }
        if(0<x2&&x2<t_k){
            t_max_res_for_each_k = a * x2 * (t_k - x2) + b * x2 + c * (t_k - x2) + d;
            if (t_max_res_for_each_k > max_res_for_each_k)
                max_res_for_each_k = t_max_res_for_each_k;
        }
        t_res = exp(-beta_* (t_k + assigned_k)) * max_res_for_each_k;
        if (t_res > tar_max){
            tar_max = t_res;
            k_tar_max = t_k+assigned_k;
        }
    }
    if(tar_max>max_res_){
        max_res_ = tar_max;
        k_with_max_res_ = k_tar_max;
    }
}

double Residual::CalCoe(int cur_id, int first_value, int second_value,int E){
    if(cur_id>=n_)
        return TE_[E];
    if(is_public_[cur_id])
        return CalCoe(cur_id+1,first_value,second_value,E*2+1);
    if(cur_id==deleted_id_)
        return CalCoe(cur_id+1,first_value,second_value,E*2);
    if(cur_id==first_id_)
        return CalCoe(cur_id+1, first_value, second_value, E*2+first_value);
    if(cur_id==second_id_)
        return CalCoe(cur_id+1, first_value, second_value, E*2+second_value);
    return CalCoe(cur_id+1,first_value,second_value,E*2)*tuple_dis_[cur_id]+CalCoe(cur_id+1,first_value,second_value,E*2+1);
}
