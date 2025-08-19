def bubble_sort(A):
    n = len(A)

    for start in range(n):
        for i in range(n-1,start,-1):
            if A[i-1] > A[i]:
                A[i], A[i-1] = A[i-1], A[i]  

              
    return A

A = [4,3,8,6,1,5]
A = [4,3]
A = [4]
A = []
print(bubble_sort(A))

