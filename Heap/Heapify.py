def heapify(A,n):
    # first non element is n/2 - 1, if n is total no of elements
    for i in range((n//2) -1, -1, -1):
        j = 2*i + 1    
        while (j<n):
            if A[j] < A[j+1]:
                j += 1
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
                i = j    
                j = 2*j + 1
            else:
                break     
    return A

A = [40,11,30,35,10,25,5]
A = [40,45,30,35,10,25,5]

print(heapify(A,len(A)-1))