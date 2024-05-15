def getPairsCount(arr, n, k):
    # count=0                     # O(n)2
    # for i in range(n):
    #     for j in range(i+1,n):
    #         target_sum = arr[i]+arr[j]
    #         if target_sum==k:
    #             count+=1
    
    # return count

    count = 0
    num_freq = {}

    for num in arr:
        diff = k-num

        if diff in num_freq:
            count += num_freq[diff]

        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1
    return count

    
arr=[1,5,7,1]
k=6
n=4

a = getPairsCount(arr, n, k)
print(a)