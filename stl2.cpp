#include<bits/stdc++.h>
#include<algorithm>
using namespace std;
struct node{
	int str,end;
};
bool micomp(node x,node y){
	return (x.str>y.str);
y}
int main()
{
	node arr[]={{6,8},{1,9},{2,4},{4,7}};
	int n=sizeof(arr)/sizeof(arr[0]);
	sort(arr,arr+n,micomp);
	cout << "Intervals sorted by start time : \n"; 
    for (int i=0; i<n; i++) 
       cout << "[" << arr[i].str << "," << arr[i].end<< "] ";
	return 0;
}
