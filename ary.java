import java.util.*;
public class ary {
    static int find(int a,int[] arrr,int[] brrr,int n)
    {
        for(int i=0;i<n;i++)
        {
            if(arrr[i]==a)
            {
                return brrr[i];
            }
        }
        return -1;
    }
    static void union(int u,int v,int[] ar,int[] br,int n)
    {
        int x=find(u,ar,br,n);
        int y=find(v,ar,br,n);
        int small=x>y?y:x;
        if(small==x)
        {
            for(int i=0;i<n;i++)
            {
                if(br[i]==y)
                {
                    br[i]=small;
                }
            }
        }
        else{
            for(int i=0;i<n;i++)
            {
                if(br[i]==x)
                {
                    br[i]=small;
                }
            }
        }
        
    }
   
            
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        int uv,u,v;
        System.out.println("Enter number of elts:");
        int n=sc.nextInt();
        int arr[]=new int[n];
        int brr[]=new int[n];
        for(int i=0;i<n;i++)
        {
            System.out.println("Enter element:");
            arr[i]=sc.nextInt();
            brr[i]=i;
        }
        
        for(int i=0;i<n;i++)
        {
            System.out.println(arr[i]+"-"+brr[i]);
        }
        System.out.println("Enter the number of links");
        int nn=sc.nextInt();
        
        for(int i=0;i<nn;i++)
        {
            System.out.println("enter two elts:");
            u=sc.nextInt();
            v=sc.nextInt();
            union(u,v,arr,brr,n);
        }
        
        for(int i=0;i<n;i++)
        {
            System.out.println(arr[i]+"-"+brr[i]);
        }
    
}
    
}
