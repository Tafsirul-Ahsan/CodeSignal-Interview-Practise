def rotateImage(a): 
    N = len(a[0]) 
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            temp = a[i][j] 
            a[i][j] = a[N - 1 - j][i] 
            a[N - 1 - j][i] = a[N - 1 - i][N - 1 - j] 
            a[N - 1 - i][N - 1 - j] = a[j][N - 1 - i] 
            a[j][N - 1 - i] = temp
            
  
# Function to print the matrix 
def printMatrix(a): 
    N = len(a[0])
    for i in range(N):
        print(a[i])
        

# Driver code 
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
rotateImage(a)
printMatrix(a)

