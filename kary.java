import java.util.*;
import java.lang.*;
class kary
{
	static Scanner s;
	static boolean check(int[] tree,int n,int k)
	{
		int l,r,ui;
		for(int i=0;i<n;i++)
		{
			if(tree[i]!=-1)
			{
                                ArrayList<Integer> al=new ArrayList();
                                for(int j=1;j<=k;j++)
                                {
                                    al.add(tree[2*i+j]);
                                }
                                ui=al.size();
                                for(int valu:al)
                                {
                                    if(valu<tree[i])
                                    {
                                        ui=ui-1;
                                    }
                                }
                                if(ui!=0)
                                {
                                    return false;
                                }
                                    
			}
			else
			{
				while(i<n)
				{
					if(tree[i]!=-1)
						return false;
					i++;
				}
			}
		}
		return true;
	}
	public static void main(String args[])
	{
		int n,a,k,max,j;
		s=new Scanner(System.in);
		System.out.println("Enter the num of nodes in Binary Tree");
		n=s.nextInt();
                System.out.println("Enter K-ary");
		k=s.nextInt();
		max=1+(int)Math.pow(k,n);
		int tree[]=new int[max+1];
		int chois;
		for(int i=0;i<=max;i++)
			tree[i]=-1;
		for(int i=0;i<n;i++)
		{
			System.out.println("Enter the element");
			a=s.nextInt();
			if(tree[0]==-1)
			{
				tree[0]=a;
				System.out.println("Inserted as Root");
			}
			else
			{
				int x=0;
				while(tree[x]!=-1){                                                    
                                    System.out.println("Which child to  "+String.valueOf(tree[x]));
                                    j=s.nextInt();
                                    j=j-1;
				    x=k*x+j;
                                    x++;
                                }
				System.out.println("Inserted!!!");
				tree[x]=a;                                                       
			}
		}
		if(check(tree,max,k)==true)
			System.out.println("Heap");
		else
			System.out.println("Not a Heap");

	}
}