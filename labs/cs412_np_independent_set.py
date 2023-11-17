# Write a program that accepts a description of an undirected graph G and a list of vertices and verifies (in polynomial time) that the list of vertices is indeed an independent set).  

# Here is some example input:

# 4
# 0 1
# 1 0 3 
# 2
# 3 1
# 0 3 2
# The first line tells you how many vertices are in the graph G.  The lines that follow contain the edge list for edge vertex.  Finally, a proposed independent set is listed.  Your program should output TRUE if the set listed in an independent set or FALSE if it is not an independent set (for example, 0 1 should not be an independent set).  

def check_independent_set(graph, independent_set):
    for v in independent_set:
        if len(graph[v]) < 1:
            return False
        for u in graph[v]:
            if u in independent_set:
                return False
    return True


def main():
    ver_count = int(input())
    G = {}

    for _ in range(ver_count):
        edges = input().split(" ", 1)
        G[int(edges[0])] = [int(x) for x in edges[1].split()] if len(edges) > 1 else []

    print(G)

    ind_set = [int(v) for v in input().split()]
    print(ind_set)
    print(check_independent_set(G, ind_set))
    

if __name__ == '__main__':
    main()