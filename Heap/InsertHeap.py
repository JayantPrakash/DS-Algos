def insert(A, n):
    temp = A[n]
    i = n
    while(i > 0 and temp > A[int(i/2)]):
        A[i] = A[int(i/2)]
        i = int(i/2)
    A[i] = temp    

    return A

A = [40,35,15,30,10,12,6,5,19]

print(insert(A,len(A)-1))



