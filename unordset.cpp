
#include <bits/stdc++.h> 
using namespace std; 

int main() 
{ 
	int arr[] = { 3, 2, 1, 3, 3, 5, 3 }; 
	int n=7;
	set<int> st(arr,arr+n);
	vector<int> obj;
	//cout << "Number of times 3 appears : "	<< count(arr, arr + n, 3); 
	//set <int> :: iterator itr;
	for(int i=0;i<n;i++)
		cout<<arr[i]<<" ";
	cout<<endl;
	set <int> :: iterator itr;
	for(itr=st.begin();itr!=st.end();itr++){
		obj.push_back(count(arr,arr+n,*itr));
	}
	vector <int> :: iterator itr1;
	for(itr=st.begin(),itr1=obj.begin();itr!=st.end()&&itr1!=obj.end();itr++,itr1++){
		cout<<(*itr)<<"->"<<(*itr1)<<endl;
	}
	cout<<endl;
	

	return 0; 
} 

