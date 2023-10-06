"""
    name:  Chingiz Rajabli

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
  
           Comments here on your code and submission.
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
# the Big O of the algorithm is little less than O(n^2) as the second for loop would always get smaller


def main():
    n = int(input())
    for _ in range(n):
        word = input()
        print(palindrome(word))


def palindrome(word):
    results = [0] * (len(word) + 1)
    results[-1] = 1

    for i in range(len(word) - 1, -1, -1):
        for j in range(i + 1, len(word) + 1):
            if is_palindrome(word[i:j]):
                results[i] += results[j]
        
    return results[0]

    
    
    

def is_palindrome(word):
    return word == word[::-1]
    

if __name__ == '__main__':
    main()