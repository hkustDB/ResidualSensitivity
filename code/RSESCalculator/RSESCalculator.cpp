#include "Residual.hpp"
#include "Elastic.hpp"
using namespace std;

void PrintUserBooklet(string program_name)
{
    cerr << "***********************************************************************************************\n"
        << "* ESRSCalculator: Calculating Elastic sensitivity/Residual sensitivity   *\n"
        << "* version: 1.0                                                                                 *\n"
        << "* For SIGMOD 2021 Paper Demo                                                  *\n"
        << "************************************************************************************************\n";
    cerr << "USAGE: " << program_name << " -T -I -Q -n -P -B\n";
    cerr << "GLOBAL OPTIONS:\n";
    cerr << "\t-T INT: Sensitivity type, Residual sensitivity(0), Elastic sensitivity(1).\n";
    cerr << "\t-I STRING: The input file of TE/mf.\n";
    cerr << "\t-Q INT: The query ID.(Necessary for Elastic sensitivity.)\n";
    cerr << "\t-n INT: The relation number.\n";
    cerr << "\t-P STRING: The public relation indicator.\n";
    cerr << "\t-B DOUBLE: The setting for parameter beta.\n";
}

//Main function.
int main(int argc, char** argv)
{
    int sensitivity_type = 0;
    string input_file_name = "";
    int query_id = 0;
    int n = 0;
    string is_public = "";
    double beta = 0;
    
    if (argc<10)
    {
        PrintUserBooklet(string(argv[0]));
        return 0;
    }

    //Read the parameters one by one.
    int i = 0;
    while (i < argc)
    {
        if (string(argv[i]) == string("-T"))
        {
            i++;
            sensitivity_type = atoi(*(argv + i));
        }
        if (string(argv[i]) == string("-I"))
        {
            i++;
            input_file_name = string(*(argv + i));
        }
        if (string(argv[i]) == string("-Q"))
        {
            i++;
            query_id = atoi(*(argv + i));
        }
        if (string(argv[i]) == string("-n"))
        {
            i++;
            n = atoi(*(argv + i));
        }
        if (string(argv[i]) == string("-P"))
        {
            i++;
            is_public = string(*(argv + i));
        }
        if (string(argv[i]) == string("-B"))
        {
            i++;
            beta = atof(*(argv + i));
        }
        i++;
    }
    if(sensitivity_type!=0&&sensitivity_type!=1)
    {
        cerr << "ERROR:" << endl;
        cerr << "Invalid sensitivity type." << endl;
        PrintUserBooklet(string(argv[0]));
        return 0;
    }
    if(input_file_name=="")
    {
        cerr << "ERROR:" << endl;
        cerr << "The input file is wrong." << endl;
        PrintUserBooklet(string(argv[0]));
        return 0;
    }
    if(sensitivity_type==1)
        if(query_id<1||query_id>9)
        {
            cerr << "ERROR:" << endl;
            cerr << "Invalid query id." << endl;
            PrintUserBooklet(string(argv[0]));
            return 0;
        }
    if(n<1)
    {
        cerr << "ERROR:" << endl;
        cerr << "Invalid relation number." << endl;
        PrintUserBooklet(string(argv[0]));
        return 0;
    }
    if(is_public=="")
    {
        cerr << "ERROR:" << endl;
        cerr << "Invalid public indicator." << endl;
        PrintUserBooklet(string(argv[0]));
        return 0;
    }
    if(beta<=0)
    {
        cerr << "ERROR:" << endl;
        cerr << "Invalid beta." << endl;
        PrintUserBooklet(string(argv[0]));
        return 0;
    }
    if(sensitivity_type==0){
        Residual residual(n,input_file_name,is_public,beta);
        double res;
        int res_k;
        residual.RunResidual();
        res = residual.GetRes();
        res_k = residual.GetKWithRes();
        std::cout<<std::fixed<<res<<"   "<<res_k<<std::endl;
    }
    else{
        Elastic elastic(n,input_file_name,beta,query_id);
        double res;
        int res_k;
        elastic.RunElastic();
        res = elastic.GetRes();
        res_k = elastic.GetKWithRes();
        std::cout<<std::fixed<<res<<"   "<<res_k<<std::endl;
    }
    return 0;
}
