"""
    name:  Chingiz Rajabli

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
  
           Comments here on your code and submission.
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def main():
    n = int(input())
    for _ in range(n):
        word = input()
        print(palindrome(word))


def palindrome(word):
    length = len(word)
    results = [None] * length

    def count_palindrome(index):
        if index >= len(word) - 1:
            return 1
        
        if results[index] is None:   
            count = 0
            for i in range(len(word) - index):
                if is_palindrome(word[index:index + i + 1]):
                    count += count_palindrome(index + i + 1)
            results[index] = count
        return results[index]
    
    return count_palindrome(0)


def is_palindrome(word):
    return word == word[::-1]
    

if __name__ == '__main__':
    main()