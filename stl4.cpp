#include<iterator>
#include<set>
#include<iostream>
using namespace std;
void disp(multiset<int> ms){
	multiset<int> :: iterator itr;
	for(itr=ms.begin();itr!=ms.end();itr++){
		cout<<*itr<<" ";
	}
	cout<<endl;
}
int main()
{
	multiset<int> ms;
	ms.insert(40);
	ms.insert(30);
	ms.insert(50);
	ms.insert(70);
	ms.insert(20);
	ms.insert(10);
	disp(ms);
	ms.erase(ms.begin(),ms.find(20));
	disp(ms);
	
	
	return 0;
}
