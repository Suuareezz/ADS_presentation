#include<iostream>
#include<algorithm>
using namespace std;
void ins(int ar[],int n)
{
	int i,j,k;
	for(i=1;i<n;i++){
		k=ar[i];
		j=i-1;
		while(j>=0 && k<ar[j]){
			ar[j+1]=ar[j];
			j-=1;
			
		}
		ar[j+1]=k;
	}
}
int main()
{
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	
	ins(arr,n);
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
}
