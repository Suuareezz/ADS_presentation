import java.util.*;
class maxk
{ 
	static void Heapify(int a[], int i, int n) 
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
			Heapify(a, largest, n); 
		} 
	} 
	static void convertMaxHeap(int a[], int n,int k) 
	{ 
		
		for (int i = (n-2)/2; i >= 0; --i) 
			Heapify(a, i, n); 
          
        }
        static void kay(int a[],int n,int k)
        {
                System.out.println("First "+k+" largest elements");
                   for(int i=n-1;i>n-k-1;i--)
                {    System.out.println(a[0]);
                     int temp = a[i]; 
			a[i] = a[0]; 
			a[0] = temp; 
			Heapify(a, 0, i); 
	}
        }
	
	static void printArray(int a[], int size) 
	{ 
		for (int i = size-1; i >=0; --i) 
			System.out.print(a[i]+" "); 
	} 
	
	
	public static void main (String[] args) 
	{ 
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
                int k=s.nextInt();
		int[]  a=new int[n];
		for(int i=0;i<n;i++)
		{
			a[i]=s.nextInt();
		} 

		convertMaxHeap(a,n,k); 
                kay(a,n,k); 

		System.out.println("Max Heap:"); 
		printArray(a, n); 
                System.out.println("");
	} 
}