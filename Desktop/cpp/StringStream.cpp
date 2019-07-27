#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str)
{
    vector<int> object;
    stringstream ss(str);
    int temp;
    char ch;
    while(ss >> temp)
    {
        object.push_back(temp);
        ss>>ch;
    }
    return object;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}

