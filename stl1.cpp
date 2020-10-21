#include<iostream>
#include<algorithm>
using namespace std;
void show(int *arr,int size)
{
	for(int i=0;i<size;i++){
		cout<<arr[i]<<" ";
	}
	cout<<endl;
	
}
void change(int *arr,int size){
	arr[0]=100;
}

void change2(int arr[],int size){
	arr[0]=100;
}
int comp(const void* x,const void* y){
	const int* a=(int*)x;
	const int* b=(int*)y;
	if(*a>*b){
		return 1;
	}
	else if(*a<*b){
		return -1;
	}
	else{
		return 0;
	}
}
int main()
{
	
	//cin>>n;
	//int *a;
	int a[] = {1, 5, 8, 9, 6, 7, 3, 4, 2, 0};
	int ARR_SIZE=sizeof(a)/sizeof(a[0]);
/*	a=new int[n];
	for(int j=0;j<n;j++)
	{
		cin>>a[j];
	}
	*/
	
	int key=9;
	int* p1 = (int*)std::bsearch(&key, a, ARR_SIZE, sizeof(a[0]), comp); 

    if (p1) 
        std::cout << key << " found at position " << (p1 - a) << '\n'; 
    else
        std::cout << key << " not found\n"; 
	
	
	sort(a,a+ARR_SIZE,greater<int>());
	show(a,ARR_SIZE);
	
	return 0;
	
}
