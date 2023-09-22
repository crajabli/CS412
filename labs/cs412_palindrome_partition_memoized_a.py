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
    results = {}
    def count_palindrome(word):
        if (len(word) <= 1):
            return 1
        if word not in results:
            count = 0
            for i in range(len(word)):
                if is_palindrome(word[:i + 1]):
                    count += count_palindrome(word[i + 1:])
            results[word] = count
        return results[word]
    
    return count_palindrome(word)




def is_palindrome(word):
    return word == word[::-1]
    

if __name__ == '__main__':
    main()