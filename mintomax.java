import java.util.*;
class mintomax
{ 
	static void MaxHeapify(int a[], int i, int n) 
	{ 
		int l = 2*i + 1; 
		int r = 2*i + 2; 
		int largest = i; 
		if (l < n && a[l] > a[i]) 
			largest = l; 
		if (r < n && a[r] > a[largest]) 
			largest = r; 
		if (largest != i) 
		{ 
			
			int temp = a[i]; 
			a[i] = a[largest]; 
			a[largest] = temp; 
			MaxHeapify(a, largest, n); 
		} 
	} 
	static void convertMaxHeap(int a[], int n)
	{ 
		
		for (int i = (n-2)/2; i >= 0; --i) 
			MaxHeapify(a, i, n); 
        }

	
	static void printArray(int a[], int size) 
	{ 
		for (int i = 0; i < size; ++i) 
			System.out.print(a[i]+" "); 
	} 
	
	
	public static void main (String[] args) 
	{ 
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
		int[]  a=new int[n];
		for(int i=0;i<n;i++)
		{
			a[i]=s.nextInt();
		} 

		convertMaxHeap(a,n); 

		System.out.println("Max Heap:"); 
		printArray(a, n); 
	} 
}