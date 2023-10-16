# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def main():
    pass


def solution(A):
    A = list(set([x for x in A if x > 0]))
    A.sort()
    if len(A) == 0:
        return 1
    
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1
    
    return A[-1] + 1

if __name__ == '__main__':
    main()