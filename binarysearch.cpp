#include<iostream>
#include<algorithm>
using namespace std;
int bins(int a[],int l,int r,int x){
	if(r>=l)
	{
		int mid=l+(r-l)/2;
		if(a[mid]==x)	{
			return mid;
		}
		if(a[mid]>x){
			return bins(a,l,mid-1,x);
		}
		if(a[mid]>x){
			return bins(a,mid+1,r,x);
		}
		
	}
	return -1;
}
int main()
{
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	sort(arr,arr+n);
	int x;
	cin>>x;
	cout<<bins(arr,0,n-1,x);
	return 0;
}
