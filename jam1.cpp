#include <bits/stdc++.h> 
using namespace std; 
int main()
{
	int n,m;
	cin>>n>>m;
	int a[n][m];
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<3;j++)
		{
			cin>>a[i][j];
			
		}
	}
	int (*p)[m]=a;
	cout<<a<<endl;
	cout<<&a[0]<<endl;
	cout<<*a<<endl;
	cout<<a[0]<<endl;
	cout<<a[0][0]<<endl;
	cout<<*(*(a+1))<<endl;
	cout<<*(*a+1)<<endl;
	
	
	
	return 0;
}
