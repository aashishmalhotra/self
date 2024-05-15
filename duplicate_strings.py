def duplicates(arr, n): 
    	# code here
    # repeated = []
    # for idx in range(n):
    #     front = idx+1
    #     for j in range(front.n):
    #         if arr[idx]==arr[j] not in repeated:
    #             repeated.append(arr[idx])
    # return repeated
    for i in range(0, n):
        index = arr[i] % n
        arr[index] += n

    # Now check which value
    # exists more
    # than once by dividing
    # with the size
    # of array
    for i in range(0, n):
        if (arr[i]/n) >= 2:
            print(i, end=" ")
    
    	   
arr = [0,3,1,2,1]
n = 4

duplicates(arr,n)

