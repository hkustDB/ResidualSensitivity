#ifndef Elastic_hpp
#define Elastic_hpp
#include <fstream>
#include <cstring>
#include <cmath>

class Elastic{
public:
    Elastic(int n, std::string mf_file_name, double beta, int query_id);
    void RunElastic();
    double** GetFromToRelations();
    double GetRes();
    int GetKWithRes();
    ~Elastic();
private:
    double CalLsk(int k);
    void ReadMf();
    double CalLskForOneRelationQ1(int delete_id,int k);
    double CalLskForOneRelationQ2(int delete_id,int k);
    double CalLskForOneRelationQ3(int delete_id,int k);
    double CalLskForOneRelationQ4(int delete_id,int k);
    double CalLskForOneRelationQ5(int delete_id,int k);
    double CalLskForOneRelationQ6(int delete_id,int k);
    double CalLskForOneRelationQ7(int delete_id,int k);
    double CalLskForOneRelationQ8(int delete_id,int k);
    double** from_to_relations_;
    double res_;
    int k_with_res_;
    double beta_;
    std::string mf_file_name_;
    //relation number
    int n_;
    int query_id_;
};
#endif /* Elastic_hpp */
