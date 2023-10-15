#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n;
	int l;
	cin >> n;
	int arr[n];
	/*n is number of integers*/
	for (int j = 0; j < n; ++j)
	{
		cin >> l;
		arr[j] = l;
	}
	int s = sizeof(arr)/sizeof(arr[0]);
	sort(arr, arr+s);
	/*for (int i=0; i<n; i++)
	{
	    cout << arr[i] << " ";
	}
	*/
	int count;
	count = 0;
	for (int i = 0; i < n; ++i)
	{
		for (int k = 0; k < n; k++)
		{
			if (arr[k+1]%arr[i]==0)
			{
				for (int ll = k; ll < n; ll++)
				{
					arr[ll] = arr[ll+1]
				}
			}
			else
			{
				count = count + 1;
			}
		}
	}
	for (int i=0; i<n; i++)
	{
	    cout << arr[i] << " ";
	}
	
}