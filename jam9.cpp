#include<iostream>
using namespace std;
int main()
{
	int* p=new int;
	(*p)=5;
	int k=(*p);
	cout<<k<<endl;
	return 0;
}
