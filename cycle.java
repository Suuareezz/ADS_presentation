import java.util.*;
class nnode
{
    int parent;
    int element;
    nnode(int p,int e)
    {
        parent=p;
        element=e;
    }
}
class cycle
{
    static int find(int x,nnode a[])
    {
        if(a[x].parent!=x)
        {
            find(a[x].parent,a);
        }
        return a[x].parent;
    }
    static void union(int x,int y,nnode a[])
    {
        a[y].parent=a[x].element;
    }
    public static void main(String args[])
    {
        int n;
        Scanner in=new Scanner(System.in);
        System.out.print("enter the number of elements : ");
        n=in.nextInt();
        nnode a[]=new nnode[n];
        System.out.println("enter the elements : ");
        for(int i=0;i<n;i++)
        {
            int x;
            x=in.nextInt();
            a[i]=new nnode(x,x);
        }
        int r;
        System.out.print("enter the no of relations : ");
        r=in.nextInt();
        System.out.println("enter the relations : ");
        for(int i=0;i<r;i++)
        {
          
            int x,y;
            x=in.nextInt();
            y=in.nextInt();
            int fx,fy;
            fx=find(x,a);
            fy=find(y,a);
            if(fx!=fy)
            {
                union(fx,fy,a);
            }
            else
            {
                System.out.println("cycle is detected at "+x+" and "+y);
            }
            
        }
        System.out.println("Output: ");
        for(int i=0;i<n;i++)
        {
            System.out.print(a[i].element+" ");
            System.out.println(a[i].parent);
        }

    }
}
