#include<iostream>
using namespace std;
int main(){
	int x;
	cin >> x;
	int temp;
	for (int i=2; i<x; i+=2){
		temp = x-i;
		if (temp%2==0){
			cout << "YES";
			return 0;
		}
	}
	cout << "NO";
	return 0;
}