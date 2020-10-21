#include<iostream>
using namespace std;
int fibo(int n){
	if(n<=1){
		return 1;
	}
	return fibo(n-1)+fibo(n-2);
}
int main()
{
	int n=5;
	int fic[n];
//	cout<<fibo(5-1);
fic[0]=1;
fic[1]=1;
for(int i=2;i<n;i++){
	fic[i]=fic[i-1]+fic[i-2];
}
cout<<fic[n-1];
	return 0;
}
