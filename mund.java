import java.util.*;
class mund
{
    static Scanner sc;
    public static void main(String []args) {
        int n;
        sc=new Scanner(System.in);
        n=sc.nextInt();
        int arr[][]=new int[n][2];
        ArrayList<Integer> al=new ArrayList<Integer>();
        int c=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<2;j++)
            {
                arr[i][j]=c;
                c++;
            }
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<2;j++)
            {
                if(!al.contains(arr[i][j]))
                {
                    al.add(arr[i][j]);
                }
                System.out.print(arr[i][j]);
            }
            System.out.println("");
        }
        System.out.println(al);

    }
}