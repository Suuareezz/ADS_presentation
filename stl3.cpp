#include<bits/stdc++.h>
#include <algorithm> 
#include <iostream>
#include<vector>
using namespace std;
int main()
{
	int a[] = {1, 5, 8, 9, 6, 7, 3, 4, 2, 0,5};
	int ARR_SIZE=sizeof(a)/sizeof(a[0]);
	vector<int> arr(a,a+ARR_SIZE);
	reverse(arr.begin(),arr.end());
	for(int i=0;i<arr.size();i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
	cout<<*max_element(arr.begin(),arr.end())<<endl;
	cout<<*min_element(arr.begin(),arr.end())<<endl;
	cout<<accumulate(arr.begin(),arr.end(),9)<<endl;
	cout<<count(arr.begin(),arr.end(),5)<<endl;
	//cout<<any_of(a,a+6, []int(){return x>=0});
	arr.erase(unique(arr.begin(),arr.end()),arr.end());
	for(int i=0;i<arr.size();i++)
	{
		cout<<arr[i]<<" ";
	}
/*	auto int* p=lower_bound(arr.begin(),arr.end(),5);
	auto int* q=upper_bound(arr.begin(),arr.end(),5);
	cout<<p-arr.begin()<<endl;
	cout<<q-arr.begin()<<endl;
	cout<<endl;
	*/
	return 0;
}
