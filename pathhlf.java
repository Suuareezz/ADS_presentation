import java.util.*;
public class pathhlf {
    
    static void pk(int m[][],int vis[][],int grp[][],n,int i,int j,int g)
    {   
        if(m[i][j]==1)
        {
            vis[i][j]=0;
            pk()
        }
        
        return 1;
    }
    public static void main(String[] args) {
        int n;
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        int main[][]=new int[n][n];
        int vis[][]=new int[n][n];
        int grp[][]=new int[n][n];
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                vis[i][j]=0;
                grp[i][j]=0;
            }
        }
        System.out.println("Enter matrix elts:");
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                main[i][j]=sc.nextInt();
            }
        }
        int cnt=pk(main,vis,grp,n,0,0);
    }   
}
