#include <bits/stdc++.h>
#include <vecto>

using namespace std;

int main(){
    int num;
    cin >> num;
    int rev_num= 0;
    while (num>1){
        rev_num = rev_num*10 + num%10;
        num /= 10;        
    }
    cout << rev_num;
}