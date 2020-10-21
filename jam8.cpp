// C++ program for function overloading 
#include <bits/stdc++.h> 

using namespace std; 
class Geeks 
{ 
	int real,img;
	
	public: 
	Geeks(int r=0,int i=0){
		real=r;
		img=i;
	}
	Geeks operator + (Geeks &obj){
		Geeks res;
		res.real=real+obj.real;
		res.img=img+obj.img;
		return res;
	}
	void print(){
		cout<<real<<endl;
		cout<<img<<endl;
		
	}
	
	
}; 

int main() { 
	
	Geeks obj1(1,3),cc(2,5);
	Geeks o3=obj1+cc;
	o3.print(); 
	
	return 0; 
} 

