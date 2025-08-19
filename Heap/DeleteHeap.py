def delete_heap(A,n):
    i = 0
    j = 1
    val = A[0]
    A[i],A[n] = A[n],A[i]
    while (j<n-1):
        if A[j] < A[j+1]:
            j += 1
        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]
            i = j    
            j = 2*j + 1
        else:
            break     
    return val

A = [40,35,30,15,10,25,5]

print(delete_heap(A,len(A)-1))

