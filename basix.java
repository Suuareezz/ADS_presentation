import java.util.*;
import java.lang.*;
class basix
{
	static Scanner s;
	static int lchild(int i)
	{
		return 2*i+1;
	}
	static int rchild(int i)
	{
		return 2*i+2;
	}
	static int parent(int i)
	{
		return (i-1)/2;
	}
	static int max(int a,int b,int c)
	{
		if(a>b && a>c)
			return a;
		if(b>c && b>a)
			return b;
		return c;
	}
	static boolean check(int[] tree,int n)
	{
		int l,r;
		for(int i=0;i<n;i++)
		{
			if(tree[i]!=-1)
			{
				l=tree[lchild(i)];
				r=tree[rchild(i)];
				if(max(l,r,tree[i])!=tree[i])
					return false;
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
		int n,a,max;
		s=new Scanner(System.in);
		System.out.println("Enter the num of nodes in Binary Tree");
		n=s.nextInt();
		max=1+(int)Math.pow(2,n);
		int tree[]=new int[max];
		int chumma;
		for(int i=0;i<max;i++)
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
					System.out.println("Left(1) or Right(2) of "+String.valueOf(tree[x]));
					chumma=s.nextInt();
					if(chumma==1)
						x=lchild(x);
					else
						x=rchild(x);
				}
				System.out.println("Inserted!!!");
				tree[x]=a;
			}
		}
		if(check(tree,max)==true)
			System.out.println("Heap");
		else
			System.out.println("Not a Heap");

	}
}