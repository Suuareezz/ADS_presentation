#include <iostream> 
#include <boost/math/common_factor.hpp> 

using namespace std; 

int main() 
{ 
	int n,m;
	cin>>n>>m;
	cout << boost::math::lcm(n,m);
	return 0; 
} 

