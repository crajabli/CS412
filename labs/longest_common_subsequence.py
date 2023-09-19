def lcs(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    if s1[m] == s2[n]:
        return 1 + lcs(s1, s2, m - 1, n - 1)
    else:
        t1 = lcs(s1, s2, m, n - 1)
        t2 = lcs(s1, s2, m - 1, n)
        return max(t1, t2)

def main():
    s1 = input()
    s2 = input()
    print(lcs(s1, s2, len(s1) - 1, len(s2) - 1))

if __name__ == '__main__':
    main()