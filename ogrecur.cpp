#include<iostream>
#include<stack>
using namespace std;
int main()
{
	string s="qpaaaaadaaaaadprq",ans="";
	stack<char> st;
	st.push(s[0]);
	int i=1;
	while(i!=s.length()){
	
	if(s[i]==st.top())
	{
		while(st.top()==s[i]){
			st.pop();
			st.push(s[i]);
			i++;
		}
		st.pop();
		
	}
	else{
		cout<<"push"<<s[i]<<endl;
		st.push(s[i]);
		i++;
	}
}
	while (!st.empty()) 
    { 
        cout<< st.top(); 
        st.pop(); 
    } 
    cout << '\n'; 

	
	return 0;
}
