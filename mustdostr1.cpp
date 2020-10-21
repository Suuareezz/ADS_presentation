#include<bits/stdc++.h>
using namespace std;
string rev(string te){
    int n=te.length();
    for(int i=0;i<n/2;i++){
        swap(te[i],te[n-i-1]);
    }
    return te;
}
int main() {
    string s="strike.like.you.very.mush";
    string a="",res="";
    for(int i=s.length()-1;i>=0;i--){
        
        if(s[i]!='.'){
            a+=s[i];
        }
        else{
            
            res=res+rev(a)+".";
            a="";
        }
    }
    cout<<res;
    int k=0;
    while(s[k]!='.'){
        cout<<s[k];
        k++;
    }
}
