import java.util.*;
class six { 
      static void maxDistinctNum(int[] arr, int n, int k) 
      { 
             HashMap<Integer, Integer> hm = new HashMap<>(); 
             for (int i = 0; i < n; i++) { 
                  if(hm.containsKey(arr[i])) { 
                       int val = hm.get(arr[i]); 
                       val++; 
                       hm.remove(arr[i]); 
                       hm.put(arr[i], val); 
                    } 
  
                  else  
                      hm.put(arr[i], 1); 
             } 
   
             System.out.println(hm);
             int max=0;
             for(int i=0;i<k;i++)
             {
                 max=0;
                for (Map.Entry<Integer, Integer> entry : hm.entrySet()) { 
                  if(entry.getValue()>max)
                  {
                      max=entry.getKey();
                  }  
                 } 
                System.out.println(" "+max); 
                hm.remove(max);
                 
             }
             
      } 
      public static void main(String args[]) 
      { 
             int[] arr = new int[20]; 
             int n,k;
	     Scanner in = new Scanner(System.in);
             System.out.println("Enter n:");
	     n = in.nextInt();
	     System.out.println("Enter K:");
	     k = in.nextInt();
	     System.out.println("Enter the array elements:");
	     for(int i=0;i<n;i++)
	     {
		arr[i] = in.nextInt();
	     }
             maxDistinctNum(arr, n, k);
      } 
}  