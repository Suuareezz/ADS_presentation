// CPP program to illustrate 
// concept of Virtual Functions 

#include <iostream> 
using namespace std; 

class base { 
public: 
	virtual void print() 
	{ 
		cout << "print base class" << endl; 
	} 

	void show() 
	{ 
		cout << "show base class" << endl; 
	} 
}; 

class derived : public base { 
public: 
	void print() 
	{ 
		cout << "print derived class" << endl; 
	} 

	void show() 
	{ 
		cout << "show derived class" << endl; 
	} 
}; 

int main() 
{ 
	base bptr; 
	derived *d; 
	d=&bptr; 

	// virtual function, binded at runtime 
	d->print(); 

	// Non-virtual function, binded at compile time 
	d->show(); 
} 

