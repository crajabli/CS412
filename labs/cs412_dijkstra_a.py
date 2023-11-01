from queue import PriorityQueue


def dijkstras(G, s, t):
    pq = PriorityQueue()
    pq.put((0, s))

    visited = set()
    while not pq.empty():
        dist, u = pq.get()
        
        if u == t:
            return dist


        if u not in visited:
            visited.add(u)
            for v in G[u]:
                pq.put((dist + G[u][v], v))

    return ("impossible")


def dijkstras2(G, s, t):
    dist = [float("inf")] * len(G)
    pred = [None] * len(G)
    visited = set()

    pq = PriorityQueue()
    pq.add((0, None, s))
    while not pq.empty():
        this_dist, parent, u = pq.get()
        if u not in visited:
            visited.add(u)
            dist[u] = this_dist
            pred[u] = parent
            for v in G[u]:
                pq.put((dist[u] + G[u][v], u, v))
    


def main():
    n, m, q = [int(x) for x in input().split()]

    G = {}

    for v in range(n):
        G[v] = {}

    for _ in range(m):
        u, v, w = [int(x) for x in input().split()]
        G[u][v] = w

    for _ in range(q):
        s, t = [int(x) for x in input().split()]
        print(dijkstras(G, s, t))



if __name__ == "__main__":
    main()