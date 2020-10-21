#include<iostream>
using namespace std;
int main()
{
	string s="qpaaaaadaaaaadprq",ans="";
	int i=0;
	while(s[i]){
		if(s[i]!=s[i+1])
		{
			ans+=s[i];
			i++;
		}
		if(s[i+1] && s[i+1]==s[i]){
			while(s[i+1] && s[i+1]==s[i])
			{
				i++;
			}
			
		}
	}
	cout<<ans;
	return 0;
}
