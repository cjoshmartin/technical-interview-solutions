#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdio.h>

//wanted output( without the newlines however):
/* '1ANV-23BA-BKLL-07642LL135KDA4C7',
    'Reprint',
    ,,
    ,,
    ,,
    '=17067',
    '=17067',
    ,,
    'HI',
    'I',
    'E',
    'RB',
    0,
    ,,
    1,
    0,
    1,
    ,,
    1,
    0,
    1,
    0,
    0,
    0,
    0
    */

int main() {
    size_t position =0;
    std::string tester;
    std::string spliter = ","; // splits at the charator
    std::string outputstring;

    std::cin >> tester; // takes in the string
    while((position = tester.find(spliter))!= std::string::npos ){ 
        std::string token =tester.substr(0,position); // splits the string after "," then stores them in  token
        if(!token.compare("")){ // check to see if there is an extra ","
           outputstring += "NULL,";
        }
        else if(!(token.find_first_not_of( "0123456789" ) == string::npos)){ // if it is NOT a digit [0-9] then it is a string and  quotations need to be added
            outputstring += "'" + token +"',";
        }
        else{ //else it is number and just add a ","
        outputstring += token + ",";
        }
        tester.erase(0,position +spliter.length()); // delete the part of the string that was alright processed
    }
    std::cout << outputstring.substr(0,outputstring.length() -1)<<"\n"; //the substr removes the last ","

    return 0;

  }
