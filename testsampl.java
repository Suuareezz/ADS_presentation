
public class testsampl {
    static void mul(int[] th)
    {
        th[0]=12;
        
    }
    public static void main(String[] args) {
        int ar[]=new int[2];
        ar[0]=1;
        ar[1]=2;
        mul(ar);
        System.out.println(ar[0]);
    }
}
