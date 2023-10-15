#include <iostream>

using namespace std;

/*
Code for the following pattern
******
*    *
*    *
*    *
*    *
******
*/ 

int main(){
    
    int rows , columns;
    cout << "Enter rows and columns\n" ;
    cin >> rows >> columns ;

    for (int i=0 ; i<rows ; i++){
        for (int j=0 ; j<columns ; j++)
        if (i==0 || i == rows-1){
            cout << "*" ;
        }
        else {
            if (j==0 || j==columns-1)
                cout << "*" ;
            else {
                cout << " " ;
            }
        }
        cout << endl;
    }


    return 0;
}
