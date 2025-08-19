import random
def quick_sort(A, start, end):
    if start >= end:
        return
    
    rand_index = random.randint(start, end)

    A[rand_index], A[start] = A[start], A[rand_index]
    smaller = start
    pivot = A[start]

    for bigger in range(start+1, end+1):
        if A[bigger] <= pivot:
            smaller += 1
            A[smaller], A[bigger] = A[bigger], A[smaller]

    A[smaller], A[start] = A[start], A[smaller]

    quick_sort(A, start, smaller - 1)
    quick_sort(A, smaller + 1, end)     
    
    return A


A = [4,2,8,7,1,3,5,6]
print(quick_sort(A,0, len(A)-1))
