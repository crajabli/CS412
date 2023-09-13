def main():
    n = int(input())
    for _ in range(n):
        word = input()
        count_palindrome(word)


def count_palindrome(word):
    count = 0
    if (len(word) == 1):
        return 1
    
    for i in range(len(word)):
        if is_palindrome(word[:i+1]):
            count += 1
    
    count += count_palindrome(word[1:])

    return count

def is_palindrome(word):
    return word == word[::-1]
    

if __name__ == '__main__':
    main()