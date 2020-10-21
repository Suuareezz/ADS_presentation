#include <iostream> 
#include <iterator> 
#include <map> 

  
using namespace std; 
  
int main() 
{ 
	map<int,int> gquiz1;
	int a[]={1,2,3,4,5,6,7,8,9};
	/*gquiz1.insert(pair<int, int>(1, 40)); 
    gquiz1.insert(pair<int, int>(2, 30)); 
    gquiz1.insert(pair<int, int>(3, 60)); 
    gquiz1.insert(pair<int, int>(4, 20)); 
    gquiz1.insert(pair<int, int>(5, 50)); 
    gquiz1.insert(pair<int, int>(6, 50)); */
     
	for(int i=0;i<10;i+=2){
		//gquiz1.insert(pair<int, int>(a[i],a[i+1));
		gquiz1.insert(pair<int, int>(a[i],a[i+1]));
	}
	map <int ,int > :: iterator itr;
	for(itr=gquiz1.begin();itr!=gquiz1.end();itr++){
		cout<<itr->first<<"\t"<<itr->second<<endl;
	}
	cout<<"\n";
	return 0;
}
