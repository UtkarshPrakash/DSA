#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int sum = 0;
	
	if (n>4)
	{
		if ((n-1)%4==0 || (n-2)%4==0)
		{
			cout << 1;
		}
		else{
			cout << 0;
		}
	}
	else if (n<=4 && n>1)
	{
		for (int i = 0; i < n+1; ++i)
		{
			sum = sum + i;
		}
		if (sum%2==0)
		{
			cout << 0;
		}
		else
		{
			cout << 1;
		}

	}
	else if (n==1)
	{
		cout << 1;
	}
	return 0;
}