import java.util.*;
class finl{
    static int find(int x,int aa[])
    {
        while(x!=aa[x])
        {
            x=aa[x];
        }
        return x;
    }
    static void union(int x,int y,int aa[],int bb[])
    {
        if(y!=x)
        {
            aa[y]=x;
            bb[x]=bb[x]+bb[y];
            bb[y]=0;
        }
    }
    static int findmax(int bb[],int n)
    {
        int max=0;
        for(int i=1;i<2*n+1;i++)
        {
            if(bb[i]>1 && bb[i]>max)
            {>
                max=bb[i];
            }
        }
        return max;
    }
    static int findmin(int bb[],int n)
    {
        int min=2*n;
        for(int i=1;i<2*n+1;i++)
        {
            if(bb[i]>1 && bb[i]<min)
            {
                min=bb[i];
            }
        }
        return min;
    }
    public static void main(String []args)
    {
        Scanner sf=new Scanner(System.in);
        int a,b,x,y;
        int n=sf.nextInt();
        int arr[]=new int[2*n+1];
        int brr[]=new int[2*n+1];
        for(int i=1;i<2*n+1;i++)
        {
            arr[i]=i;
            brr[i]=1;
        }
        for(int i=0;i<n;i++)
        {
            a=sf.nextInt();
            b=sf.nextInt();
            x=find(a,arr);
            y=find(b,arr);
            union(x,y,arr,brr);
        }
        System.out.print(findmax(brr,n)+" "+findmin(brr,n));
    }
}