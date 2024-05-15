#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&difficulty[]=0&category[]=Arrays&sortBy=submissions

def subArraySum(arr, n, s): 
#        #Write your code here
    
    for i in range(n):
        current_sum = arr[i]
        
        if current_sum==12:
            print(i," ")
            return 
        else:
            for j in range(i+1,n):
                current_sum = arr[j]
                if current_sum==sum:
                    print(i, j)
                    return
        return -1
            
if __name__ == "__main__":
    arr = [15,2,4,8,9,5,10,23]
    n = len(arr)
    sum = 23
    subArraySum(arr, n, sum)
      