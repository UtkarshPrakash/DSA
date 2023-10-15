#include <iostream>

using namespace std;

int main(){
    
    int n ;
    cout << "Enter a size for Butterfly\n\n" ;
    // cin >> n ;
    n = 4 ;

    for (int i=0 ; i<n ; i++){
        for (int j=0 ; j<n*2 ; j++){
            if (j<=i)
                cout << "* ";
            else if (j <= 2*n-i-2) 
                cout << "- ";
            else 
                cout << "* ";
        }
        cout << endl;
    }

    for (int i=n-1 ; i>=0 ; i--){
        for (int j=0 ; j<n*2 ; j++){
            if (j<=i)
                cout << "* ";
            else if (j >= 2*(n-i)-1)
                cout << "* " ;
            else 
                cout << "- ";
        }
        cout << endl;
    }

    return 0;
}
