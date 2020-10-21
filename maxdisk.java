import java.util.*;
class maxdisk { 
      static int maxDistinctNum(int[] arr, int n, int k) 
      { 
             HashMap<Integer, Integer> hm = new HashMap<>(); 
             PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder()); 
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
   
             for (Map.Entry<Integer, Integer> entry : hm.entrySet()) { 
                  pq.add(entry.getValue()); 
             } 
  
             while (k > 0) { 
                   int temp = pq.poll(); 
                   temp--;  
                   if (temp > 0) 
                       pq.add(temp); 
                   k--; 
             }  
             int count = 0; 
             while (pq.size() != 0) 
	     { 
                   pq.poll(); 
                   count++; 
             } 
  
             return count;
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
             System.out.println("Maximum distinct elements = " + maxDistinctNum(arr, n, k)); 
      } 
}  