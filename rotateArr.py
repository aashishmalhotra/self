def rotateArr(A,D,N):
    temp = []
    for ele in range(D,N):
        temp.append(A[ele])
        # print("f",temp)
    for first in range(0,D):
        temp.append(A[first])
        # print("s",temp)

        A = temp
        return A

N = 10
D = 2
A = [2,4,6,8,10,12,14,16,18,20]

print(rotateArr(A,D,N))