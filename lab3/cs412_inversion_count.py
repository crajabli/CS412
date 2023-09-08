"""
   MergeSort
   coded by Bowers from Jeff Erickson's pseudocode
"""


def mergesort(A):
    inversion_count = 0
    if len(A) > 1:
        # Get the mid point
        m = len(A) // 2

        # Get the left and right halves
        left, right = A[:m], A[m:]

        # sort the left and right halves
        inversion_count += mergesort(left)
        inversion_count += mergesort(right)

        # Copy the sorted left and right halves back to A. 
        for i in range(m):
            A[i] = left[i]
        for j in range(m, len(A)):
            A[j] = right[j - m]
        
        # Run the merge operation on A
        inversion_count += merge(A, m)
    return inversion_count


def merge(A, m):
    inversion_count = 0
    i, j = 0, m
    n = len(A)
    B = [0 for _ in range(n)]
    for k in range(n):
        if j >= n:
            B[k] = A[i]
            i += 1
        elif i >= m:
            B[k] = A[j]
            j += 1
        elif A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
            inversion_count += 1
    for k in range(n):
        A[k] = B[k]
    return inversion_count


def main():
    in_list = list(map(int, input().split()))
    inversion = mergesort(in_list)
    print(inversion)


if __name__ == "__main__":
    main()
