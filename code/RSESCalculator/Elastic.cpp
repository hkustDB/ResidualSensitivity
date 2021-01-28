#include "Elastic.hpp"
#include <iostream>
void Elastic::ReadMf(){
    std::ifstream mf_file(mf_file_name_);
    int from = 0;
    int to = 0;
    int mf = 0;
    while(mf_file>>from>>to>>mf){
        from_to_relations_[from][to] = mf;
    }
}

Elastic::Elastic(int n, std::string mf_file_name, double beta, int query_id){
    mf_file_name_=mf_file_name;
    n_=n;
    query_id_=query_id;
    beta_ = beta;
    from_to_relations_ = new double*[n];
    for(int i = 0; i<n; i++)
        from_to_relations_[i] = new double[n];
    for(int i = 0; i<n; i++)
        for(int j = 0; j<n; j++)
            from_to_relations_[i][j]=0;
    ReadMf();
}

Elastic::~Elastic(){
    if(from_to_relations_!=NULL){
        for(int i = 0; i<n_; i++)
            if(from_to_relations_[i]!=NULL){
                delete[] from_to_relations_[i];
                from_to_relations_[i] = NULL;
            }
        delete[] from_to_relations_;
        from_to_relations_ = NULL;
    }
}

double Elastic::CalLsk(int k){
    double res = 0;
    double t_res = 0;
    for(int i = 0; i<n_; i++){
        switch (query_id_) {
            case 1:
                t_res = CalLskForOneRelationQ1(i,k);
                break;
            case 2:
                t_res = CalLskForOneRelationQ2(i,k);
                break;
            case 3:
                t_res = CalLskForOneRelationQ3(i,k);
                break;
            case 4:
                t_res = CalLskForOneRelationQ4(i,k);
                break;
            case 5:
                t_res = CalLskForOneRelationQ5(i,k);
                break;
            case 6:
                t_res = CalLskForOneRelationQ6(i,k);
                break;
            case 7:
                t_res = CalLskForOneRelationQ7(i,k);
                break;
            case 8:
                t_res = CalLskForOneRelationQ8(i,k);
                break;
            default:
                break;
        }
        if(t_res>res)
            res = t_res;
    }
    return res;
}

void Elastic::RunElastic(){
    double max_res_at_k=0;
    double max_res=0;
    int k_max_res=0;
    int max_k = int(n_/beta_);
    for(int k = 0; k<=max_k; k++){
        max_res_at_k = CalLsk(k)*exp(-k*beta_);
        if(max_res_at_k>max_res){
            max_res = max_res_at_k;
            k_max_res = k;
        }
    }
    res_=max_res;
    k_with_res_ = k_max_res;
}

double** Elastic::GetFromToRelations(){
    return from_to_relations_;
}

double Elastic::GetRes(){
    return res_;
}

int Elastic::GetKWithRes(){
    return k_with_res_;
}

double Elastic::CalLskForOneRelationQ1(int delete_id,int k){
    double** relations = from_to_relations_;
    if(delete_id==0)
        return 0;
    else if(delete_id == 1)
        return (relations[0][1])*(relations[2][1]+k)*(relations[3][2]+k)*(relations[4][3]+k);
    else if(delete_id == 2)
        return (relations[0][1])*(relations[1][2]+k)*(relations[3][2]+k)*(relations[4][3]+k);
    else if(delete_id == 3)
        return (relations[0][1]) * (relations[1][2] + k)*(relations[2][3] + k)*(relations[4][3]+k);
    else return (relations[0][1]) * (relations[1][2] + k) * (relations[2][3] + k) * (relations[3][4] + k);
}

double Elastic::CalLskForOneRelationQ2(int delete_id,int k){
    double** relations = from_to_relations_;
    if(delete_id==0)
        return 0;
    else if(delete_id == 1)
        return (relations[0][1])*(relations[2][1]+k)*(relations[3][1]+k)*(relations[4][3]+k);
    else if(delete_id == 2)
        return (relations[0][1])*(relations[1][2]+k)*(relations[3][1]+k)*(relations[4][3]+k);
    else if(delete_id == 3)
        return (relations[0][1])* (relations[1][3] + k)*(relations[2][1]+k)*(relations[4][3]+k);
    else return (relations[0][1])* (relations[1][3] + k)*(relations[2][1]+k)*(relations[3][4]+k);
}

double Elastic::CalLskForOneRelationQ3(int delete_id,int k){
    double** relations = from_to_relations_;
    double max_res=0;
    double t_res = 0;
    if(delete_id==0||delete_id == 1)
        max_res=0;
    else if(delete_id == 2){
        max_res = (relations[3][2]+k)*(relations[4][3]+k)*(relations[5][4]+k)*(relations[1][5]);
        t_res = (relations[3][2]+k)*(relations[4][3]+k)*(relations[5][4]+k)*(relations[1][2]);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[3][2]+k)*(relations[4][3]+k)*(relations[5][1]+k)*(relations[1][2]);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[3][2]+k)*(relations[4][5]+k)*(relations[5][1]+k)*(relations[1][2]);
        if(t_res>max_res)
            max_res = t_res;
        t_res =(relations[3][4]+k)*(relations[4][5]+k)*(relations[5][1]+k)*(relations[1][2]);
        if(t_res>max_res)
            max_res = t_res;
    }
    else if(delete_id == 3){
        max_res = (relations[4][3]+k)*(relations[5][4]+k)*(relations[1][5])*(relations[2][1]+k);
        t_res = (relations[4][3]+k)*(relations[5][4]+k)*(relations[1][5])*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
            t_res = (relations[4][3]+k)*(relations[5][4]+k)*(relations[1][2])*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
            t_res = (relations[4][3]+k)*(relations[5][1]+k)*(relations[1][2])*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
            t_res = (relations[4][5]+k)*(relations[5][1]+k)*(relations[1][2])*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else if(delete_id == 4){
        max_res = (relations[5][4]+k)*(relations[1][5])*(relations[2][1]+k)*(relations[3][2]+k);
        t_res =(relations[5][4]+k)*(relations[1][5])*(relations[2][1]+k)*(relations[3][4]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res =(relations[5][4]+k)*(relations[1][5])*(relations[2][3]+k)*(relations[3][4]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res =(relations[5][4]+k)*(relations[1][2])*(relations[2][3]+k)*(relations[3][4]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res =(relations[5][1]+k)*(relations[1][2])*(relations[2][3]+k)*(relations[3][4]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else{
        max_res = (relations[1][5])*(relations[2][1]+k)*(relations[3][2]+k)*(relations[4][3]+k);
        t_res = (relations[1][5])*(relations[2][1]+k)*(relations[3][2]+k)*(relations[4][5]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[1][5])*(relations[2][1]+k)*(relations[3][4]+k)*(relations[4][5]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[1][5])*(relations[2][3]+k)*(relations[3][4]+k)*(relations[4][5]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[1][2])*(relations[2][3]+k)*(relations[3][4]+k)*(relations[4][5]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    return max_res;
}

double Elastic::CalLskForOneRelationQ4(int delete_id,int k){
    double** relations = from_to_relations_;
    if(delete_id==0)
        return (relations[1][0]+k)*(relations[2][1]+k)*(relations[3][2]+k)*(relations[4][3]+k);
    else if(delete_id == 1)
        return (relations[0][1]+k)*(relations[2][1]+k)*(relations[3][2]+k)*(relations[4][3]+k);
    else if(delete_id == 2)
        return (relations[0][1]+k)*(relations[1][2]+k)*(relations[3][2]+k)*(relations[4][3]+k);
    else if(delete_id == 3)
        return (relations[0][1]+k)*(relations[1][2]+k)*(relations[2][3]+k)*(relations[4][3]+k);
    else
        return (relations[0][1]+k)*(relations[1][2]+k)*(relations[2][3]+k)*(relations[3][4]+k);
}

double Elastic::CalLskForOneRelationQ5(int delete_id,int k){
    double** relations = from_to_relations_;
    double max_res=0;
    double t_res = 0;
    if(delete_id==0){
        max_res = (relations[1][0]+k)*(relations[2][1]+k);
        t_res = (relations[1][0]+k)*(relations[2][0]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[1][2]+k)*(relations[2][0]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else if(delete_id == 1){
        max_res = (relations[2][1]+k)*(relations[0][2]+k);
        t_res = (relations[2][1]+k)*(relations[0][1]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[2][0]+k)*(relations[0][1]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else{
        max_res = (relations[0][2]+k)*(relations[1][0]+k);
        t_res = (relations[0][2]+k)*(relations[1][2]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[0][1]+k)*(relations[1][2]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    return max_res;
}

double Elastic::CalLskForOneRelationQ6(int delete_id,int k){
    double** relations = from_to_relations_;
    double max_res=0;
    double t_res = 0;
    if(delete_id==0){
        max_res = (relations[1][0]+k)*(relations[2][1]+k)*(relations[3][2]+k);
        t_res = (relations[1][0]+k)*(relations[2][1]+k)*(relations[3][0]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[1][0]+k)*(relations[2][3]+k)*(relations[3][0]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[1][2]+k)*(relations[2][3]+k)*(relations[3][0]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else if(delete_id == 1){
        max_res = (relations[2][1]+k)*(relations[3][2]+k)*(relations[0][3]+k);
        t_res = (relations[2][1]+k)*(relations[3][2]+k)*(relations[0][1]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[2][1]+k)*(relations[3][0]+k)*(relations[0][1]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[2][3]+k)*(relations[3][0]+k)*(relations[0][1]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else if(delete_id == 2){
        max_res = (relations[3][2]+k)*(relations[0][3]+k)*(relations[1][0]+k);
        t_res = (relations[3][2]+k)*(relations[0][3]+k)*(relations[1][2]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[3][2]+k)*(relations[0][1]+k)*(relations[1][2]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[3][0]+k)*(relations[0][1]+k)*(relations[1][2]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else{
        max_res = (relations[0][3]+k)*(relations[1][0]+k)*(relations[2][1]+k);
        t_res = (relations[0][3]+k)*(relations[1][0]+k)*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[0][3]+k)*(relations[1][2]+k)*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[0][1]+k)*(relations[1][2]+k)*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    return max_res;
}

double Elastic::CalLskForOneRelationQ7(int delete_id,int k){
    double** relations = from_to_relations_;
    double max_res=0;
    double t_res = 0;
    if(delete_id==0){
        max_res = (relations[1][0]+k)*(relations[2][1]+k)*(relations[3][2]+k)*(relations[4][3]+k);
        t_res = (relations[1][0]+k)*(relations[2][1]+k)*(relations[3][2]+k)*(relations[4][0]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[1][0]+k)*(relations[2][1]+k)*(relations[3][4]+k)*(relations[4][0]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[1][0]+k)*(relations[2][3]+k)*(relations[3][4]+k)*(relations[4][0]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[1][2]+k)*(relations[2][3]+k)*(relations[3][4]+k)*(relations[4][0]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else if(delete_id == 1){
        max_res = (relations[2][1]+k)*(relations[3][2]+k)*(relations[4][3]+k)*(relations[0][4]+k);
        t_res = (relations[2][1]+k)*(relations[3][2]+k)*(relations[4][3]+k)*(relations[0][1]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[2][1]+k)*(relations[3][2]+k)*(relations[4][0]+k)*(relations[0][1]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[2][1]+k)*(relations[3][4]+k)*(relations[4][0]+k)*(relations[0][1]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[2][3]+k)*(relations[3][4]+k)*(relations[4][0]+k)*(relations[0][1]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else if(delete_id == 2){
        max_res = (relations[3][2]+k)*(relations[4][3]+k)*(relations[0][4]+k)*(relations[1][0]+k);
        t_res = (relations[3][2]+k)*(relations[4][3]+k)*(relations[0][4]+k)*(relations[1][2]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[3][2]+k)*(relations[4][3]+k)*(relations[0][1]+k)*(relations[1][2]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[3][2]+k)*(relations[4][0]+k)*(relations[0][1]+k)*(relations[1][2]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[3][4]+k)*(relations[4][0]+k)*(relations[0][1]+k)*(relations[1][2]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else if(delete_id == 3){
        max_res = (relations[4][3]+k)*(relations[0][4]+k)*(relations[1][0]+k)*(relations[2][1]+k);
        t_res = (relations[4][3]+k)*(relations[0][4]+k)*(relations[1][0]+k)*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[4][3]+k)*(relations[0][4]+k)*(relations[1][2]+k)*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[4][3]+k)*(relations[0][1]+k)*(relations[1][2]+k)*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[4][0]+k)*(relations[0][1]+k)*(relations[1][2]+k)*(relations[2][3]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    else{
        max_res = (relations[0][4]+k)*(relations[1][0]+k)*(relations[2][1]+k)*(relations[3][2]+k);
        t_res = (relations[0][4]+k)*(relations[1][0]+k)*(relations[2][1]+k)*(relations[3][4]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[0][4]+k)*(relations[1][0]+k)*(relations[2][3]+k)*(relations[3][4]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[0][4]+k)*(relations[1][2]+k)*(relations[2][3]+k)*(relations[3][4]+k);
        if(t_res>max_res)
            max_res = t_res;
        t_res = (relations[0][1]+k)*(relations[1][2]+k)*(relations[2][3]+k)*(relations[3][4]+k);
        if(t_res>max_res)
            max_res = t_res;
    }
    return max_res;
}

double Elastic::CalLskForOneRelationQ8(int delete_id,int k){
    double** relations = from_to_relations_;
    if(delete_id==0)
        return (relations[1][0]+k)*(relations[2][0]+k)*(relations[3][0]+k);
    else if(delete_id == 1)
        return (relations[0][1]+k)*(relations[2][0]+k)*(relations[3][0]+k);
    else if(delete_id == 2)
        return (relations[0][2]+k)*(relations[1][0]+k)*(relations[3][0]+k);
    else
        return (relations[0][3]+k)*(relations[1][0]+k)*(relations[2][0]+k);
}

