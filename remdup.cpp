#include<bits/stdc++.h>
#include<unordered_map>
using namespace std;
char* dun(char *s,int n)
{
	unordered_map<char,int> og;
	int ins=0;
	for(int i=0;i<n;i++){
		if(og[s[i]]==0){
			s[ins++]=s[i];
			og[s[i]]++;
		}
	}
	return s;
}
int main()
{
	char s[]="geeksforgeeks";
	int n=sizeof(s)/sizeof(s[0]);
	cout<<dun(s,n);
	return 0;
}
