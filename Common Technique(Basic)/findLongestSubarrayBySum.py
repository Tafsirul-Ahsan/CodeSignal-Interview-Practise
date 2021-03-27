def findLongestSubarrayBySum(arr,n,s): 
    
    for i in range(n): 
        curr_sum = arr[i] 
      
        j = i + 1
        while j <= n: 
          
            if curr_sum == s: 
                print("[" + str(i+1) + "," + str(j) + "]")
                  
                return 1
                  
            if curr_sum > s or j == n: 
                break
              
            curr_sum = curr_sum + arr[j] 
            j += 1
  
   

arr = [1, 2, 3, 7, 5]
n = len(arr)
s = 12
  
findLongestSubarrayBySum(arr,n,s) 
