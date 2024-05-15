#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&difficulty[]=0&category[]=Arrays&sortBy=submissions
arr = [6,1,2,8,3,4,7,10,5]
n=9
def find(arr,n):
    arr = sorted(arr)
    for i in range(n):
        for j in range(i+1,n):
            diff = arr[j] - arr[i]
            continue
            else:
                res = arr[j]+1
                if res<arr[n-1]:
                    print(res)
find(arr,n)