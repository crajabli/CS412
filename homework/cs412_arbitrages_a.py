

def bellman_ford(G):
    pass


def main():
    m = int(input())

    G = {}

    for v in range(m):
        G[v] = {}

    for _ in range(m):
        cIn, cOut, rate = [int(x) for x in input().split()]
        G[cIn][cOut] = rate
    
    print(bellman_ford(G))



if __name__ == "__main__":
    main()