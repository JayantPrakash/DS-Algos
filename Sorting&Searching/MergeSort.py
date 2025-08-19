def merge_sort(A, start, end):

    if start >= end:
        return
    
    mid = int((start + end)/2)

    merge_sort(A, start, mid)
    merge_sort(A, mid +1, end)

    mlist = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if A[i] <= A[j]:
            mlist.append(A[i])
            i += 1
        elif A[i] > A[j]:
            mlist.append(A[j])
            j += 1

    while i <= mid:
        mlist.append(A[i])
        i += 1

    while j <= end:
        mlist.append(A[j])
        j += 1

    A[start:end + 1] = mlist

    return A     


A = [6,4,3,8,1,5,2,7]

print(merge_sort(A,0,len(A)-1))
