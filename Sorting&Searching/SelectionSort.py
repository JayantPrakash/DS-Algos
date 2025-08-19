def selection_sort(A):
    n = len(A)

    for i in range(n):
        min = i

        for inner in range(i+1,n):
            if A[inner] < A[min]:
                min = inner

        A[i], A[min] = A[min], A[i]        

    return A

A = [4,3,8,6,1,5]
A = [4,3]

print(selection_sort(A))

