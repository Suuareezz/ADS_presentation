def diagonalDifference(arr):
    su=0
    se=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            
            if(i==j):
                print(i,j)
                su=su+arr[i][j]
            if(i+j==len(arr)-1):
                print(i,j)
                se=se+arr[i][j]
    return abs(se-su)

arr=[[11,2,4],[4,5,6],[10,8,-12]]
print(diagonalDifference(arr))
for(int k=0;k<n;k++)
{
    for(int i=n-1;i>0;i++)
    {
        cout<<" ";
    }
    for(int j=k+1;j>0;j--)
    {
        cout<<"#";
    }
    cout<<endl;
}
