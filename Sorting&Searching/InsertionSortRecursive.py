def insertion_sort(A,n):

    if n < 1:
        return 

    insertion_sort(A, n - 1)    

    curr_elem = A[n]
    j = n - 1

    while j >= 0 and curr_elem < A[j]:
        A[j+1] = A[j]
        j -= 1

    A[j+1] = curr_elem

    return A    


A = [8,2,4,9,3,6]

print(insertion_sort(A,len(A)-1))
