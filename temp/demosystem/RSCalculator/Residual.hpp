#ifndef Residual_hpp
#define Residual_hpp
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <fstream>

class Residual{
public:
    Residual(int n, std::string TE_file_name, std::string is_public, double beta);
    ~Residual();
    void RunResidual();
    //Return residual sensitivity
    double GetRes();
    //Return k that maximal exp^{-\betak}LSK
    int GetKWithRes();
    int* GetTE();
    bool* GetIsPublic();
    
private:
    //Private data
    //Results
    double res_;
    int k_with_res_;
    //TE's
    int* TE_;
    //Relation num
    int n_;
    //The file stored TE
    std::string TE_file_name_;
    //Indicate the public relation
    bool* is_public_;
    //Number of private relation
    int m_;
    //The num of types of E
    int num_E_;
    //The setting for beta;
    double beta_;
    //The maximum k should be considered: \hatk=(m-1)/\beta
    int max_k_;
    //The results
    double max_res_;
    int k_with_max_res_;
    //Below data are used in intermediate calculation
    int* tuple_dis_;
    //Consider the case T_{[n]-i}
    int deleted_id_;
    int first_id_;
    int second_id_;
    int candidate_k_[10000];
    int candidate_k_num_;
    int template_list_[10000];
    int template_list_num_;
    //Private functions
    //Read TE's from a file
    void ReadTE();
    //Calculate m: public relation num
    void CalM();
    void CallMaxRes();
    void CallMaxTE();
    void CallMaxTERec(int cur_id, int left_k);
    void CallMaxTEWithTupleDis(int left_k);
    double CalCoe(int cur_id, int first_value, int second_value,int E);
};
#endif /* Residual_hpp */

