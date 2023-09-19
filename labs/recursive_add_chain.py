def recursive_add_chain(AC, n):
    if AC[-1] == n:
        return len(AC)
    if AC[-1] > n:
        return float("inf")
    bestcase = float("inf")
    for i in AC:
        new_AC = AC.copy()
        new_AC.append(AC[-1]ti)
        bestcase = min(bestcase, recursive_add_chain(new_AC, n))
    return bestcase

def main():
    addition_chain = (1, 2, 3, 5, 10, 20, 23, 46, 92, 184, 187, 374)
    n = int(input())
    recursive_add_chain(addition_chain, n)
    pass

if __name__ == '__main__':
    main()