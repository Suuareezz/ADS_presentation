import java.util.*;
public class fastun {
    static int findwt(int a,int[] arrr,int[] crrr,int n)
    {
        for(int i=0;i<n;i++)
        {
            if(arrr[i]==a)
            {
                return crrr[i];              
            }
        }
        return -1;
    }
    static int findpar(int a,int[] arrr,int[] brrr,int n)
    {
        for(int i=0;i<n;i++)
        {
            if(arrr[i]==a)
            {
                if(brrr[i]==arrr[i])
                {
                    return brrr[i];
                }
                else{
                    return findpar(brrr[i],arrr,brrr,n);
                }
                                
            }
        }
        return -1;
    }
    static void union(int u,int v,int[] ar,int[] br,int[] cr,int n)
    {
        int x=findpar(u,ar,br,n);
        int y=findpar(v,ar,br,n);
        int xw=findwt(x,ar,cr,n);
        int yw=findwt(y,ar,cr,n);  
        if(xw>=yw)
        {
            for(int i=0;i<n;i++)
            {
                if(y==ar[i])
                {
                    br[i]=x;
                    for(int j=0;j<n;j++)
                    {
                        if(ar[j]==x)
                        {
                            cr[j]+=cr[i];
                        }
                    }
                    for(int k=0;k<n;k++)
                    {
                        if(br[k]==br[i])
                        {
                            br[k]=x;
                        }
                    }
                }
            }
        }
        else{
            for(int i=0;i<n;i++)
            {
                if(x==ar[i])
                {
                    br[i]=y;
                    for(int j=0;j<n;j++)
                    {
                        if(ar[j]==y)
                        {
                            cr[j]+=cr[i];
                        }
                    }
                    for(int k=0;k<n;k++)
                    {
                        if(br[k]==br[i])
                        {
                            br[k]=y;
                        }
                    }
                }
            }   
        }
    }
    static void print(int[] arr,int[] brr,int[] crr,int n)
    {
        for(int i=0;i<n;i++)
        {
            System.out.print(arr[i]);            
        }
        System.out.println("");
        for(int i=0;i<n;i++)
        {           
            System.out.print(brr[i]);
         
        }
        System.out.println("");
        for(int i=0;i<n;i++)
        {

            System.out.print(crr[i]);
            
        }
    }
            
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        int uv,u,v;
        System.out.println("Enter number of elts:");
        int n=sc.nextInt();
        int arr[]=new int[n];
        int brr[]=new int[n];
        int crr[]=new int[n];
        
        for(int i=0;i<n;i++)
        {
            System.out.println("Enter element:");
            arr[i]=sc.nextInt();
            brr[i]=i;
            crr[i]=1;
        }
        print(arr,brr,crr,n);
        
        System.out.println("");
        System.out.println("Enter the number of links");
        int nn=sc.nextInt();
        
        for(int i=0;i<nn;i++)
        {
            System.out.println("enter two elts:");
            u=sc.nextInt();
            v=sc.nextInt();
            union(u,v,arr,brr,crr,n);
            print(arr,brr,crr,n);
        }
        
    
}
    
}
