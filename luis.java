import java.util.*;
class node
{
    int parent;
    int elt;
    node(int p,int e)
    {
        parent=p;
        elt=e;
    }
}
class luis
{
    static int find(int x,node a[])
    {
        if(a[x].parent==x)
        {
            return a[x].parent;
        }
        return find(a[x].parent,a);
    }
    static void union(int x,int y,node a[])
    {
        a[y].parent=a[x].elt;
    }
    public static void main(String args[])
    {
        int n;
        Scanner sc=new Scanner(System.in);
        System.out.print("enter number of elements : ");
        n=sc.nextInt();
        node a[]=new node[n];
        System.out.println("enter elements : ");
        for(int i=0;i<n;i++)
        {
            int x;
            x=sc.nextInt();
            a[i]=new node(x,x);
        }
        int uv;
        System.out.print("enter the no of relations : ");
        uv=sc.nextInt();
        System.out.println("enter the relations : ");
        for(int i=0;i<uv;i++)
        {
            int x,y;
            x=sc.nextInt();
            y=sc.nextInt();
            int ab,bc;
            ab=find(x,a);
            bc=find(y,a);
            union(ab,bc,a);
        }    
        System.out.println("Output:");
        for(int i=0;i<n;i++)
        {
            System.out.print(a[i].elt+" ");
            System.out.println(a[i].parent);
        }

    }
}
