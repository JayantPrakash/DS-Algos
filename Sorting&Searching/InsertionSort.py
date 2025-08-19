def insertion_sort(A):

    if len(A) < 2:
        return A
    
    for i in range(1, len(A)):

        curr_elem = A[i]
        j = i - 1

        while j >= 0 and curr_elem < A[j]:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = curr_elem

    return A      


A = [8,2,4,9,3,6]

print(insertion_sort(A))
