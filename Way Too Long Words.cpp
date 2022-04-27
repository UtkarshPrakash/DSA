#include <iostream>
using namespace std;
int main(){
    int t; string s; string ans;
    cin >> t;
    for (int k=0; k<t; k++){
        cin >> s;
        if (s.length()>10){
            ans = s[0];
            ans += to_string(s.length()-2);
            ans += s[s.length()-1];
			cout << ans << endl;
        }
        else
            cout << s << endl;
    }
    return 0;
}