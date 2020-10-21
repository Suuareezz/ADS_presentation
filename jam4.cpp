#include<iostream>
using namespace std;
int gcd(int a , int b)
{
	if (b==0){
		return a;
	}
	return gcd(b,a%b);
}
int main()
{
	int arr[5]={1,2,3,4,5,7,8,9,10,11,12};
	int d=gcd(12,3);
	for(int j=0;j<d;j++)
	{
		int y=arr[j];
		for(int i=j;i<12/3;i+=d)
		{
			arr[i]=arr[i+d];
		}
		arr[i+1]
	}
	
	
	return 0;
}
