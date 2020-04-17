#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

int main() {
    int size;
    int input;
    int i = 0;
    vector<int> sequence;
    cin >> size;
    while (i++ != size){
        cin >> input;
        sequence.push_back(input);
    } 
    if(sequence.size() == 1) return 1;
    vector<int> v(sequence.size()-1);
    for(int i=1;i<sequence.size();i++){
      v[i-1] = sequence[i] - sequence[i-1];
    }
    int ii=0;
    while( ii < v.size() && v[ii] == 0)
    ii++;
    if(ii == v.size()) return 1;
    int dir = v[ii];
    int flag = dir;
    int len = 2;
    for(int i=ii+1;i<v.size();i++){
      if(v[i] * dir < 0){
        dir *= -1;  
        len++;
      }
    }
    if(flag >= 0){
        cout<<len;
    }
    else {
        cout<<len-1;
    }
    return 0;
}