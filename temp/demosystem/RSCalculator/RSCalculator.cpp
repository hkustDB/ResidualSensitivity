#include "Residual.hpp"
using namespace std;

void PrintUserBooklet(string program_name)
{
    cerr << "***********************************************************************************************\n"
        << "* RSCalculator: Calculating residual sensitivity *\n"
        << "* version: 1.0                                                                                 *\n"
        << "* For SIGMOD 2021 Paper Demo                                                  *\n"
        << "************************************************************************************************\n";
    cerr << "USAGE: " << program_name << "-n -P -B -I\n";
    cerr << "GLOBAL OPTIONS:\n";
    cerr << "\t-n INT: The relation number.\n";
    cerr << "\t-P STRING: The public relation indicator.\n";
    cerr << "\t-B DOUBLE: The setting for parameter beta.\n";
    cerr << "\t-I STRING: The input file of TE.\n";
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
    
    //Read the parameters one by one.
    int i = 0;
    while (i < argc)
    {
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
        if(string(argv[i]) == string("-h"))
        {
            PrintUserBooklet(string(argv[0]));
            return 0;
        }
        if(string(argv[i]) == string("-I"))
        {
            i++;
            input_file_name = string(*(argv + i));
        }
        i++;
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
    Residual residual(n,input_file_name,is_public,beta);
    double res;
    int res_k;
    residual.RunResidual();
    res = residual.GetRes();
    res_k = residual.GetKWithRes();
    std::cout<<std::fixed<<res<<"   "<<res_k<<std::endl;
    return 0;
}
