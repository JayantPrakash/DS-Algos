def insert(A, n):
    temp = A[n]
    i = n
    while(i > 0 and temp > A[int(i/2)]):
        A[i] = A[int(i/2)]
        i = int(i/2)
    A[i] = temp    

    return A

def delete_heap(A,n):
    i = 0
    j = 1
    val = A[0]
    #swap first and last element
    A[i],A[n] = A[n],A[i]
    # check if it is n-1 as j+1 will make it out of index
    while (j<n-1):
        # find which child is greater
        if A[j] < A[j+1]:
            j += 1
        # whichever child is greater is compared with current elem
        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]
            i = j    
            j = 2*j + 1
        # It is at right place
        else:
            break     
    return val


def heapSort(A):
    for i in range(1, len(A)):
        insert(A,i)

    #range is from len-1 to 1
    for i in range(len(A)-1,0,-1):
        delete_heap(A,i)
    return A    

A = [40,45,30,35,10,25,5]

print(heapSort(A))

