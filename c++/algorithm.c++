#include<iostream>
using namespace std;

int main(){

    char ch[10] = "Amit Wala";
    char* c = ch;
    cout << ch << endl;
    cout << *c << endl;
    cout << c + 1 << endl;

    return 0;
}