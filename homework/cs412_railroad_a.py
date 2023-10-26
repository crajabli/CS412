def railroad():
    pass

def dfs_label(graph, v, labels, currentLabel):
    bag = [v]
    while bag: # while bag is not empty
        u = bag.pop()
        if labels[u] == -1:
            labels[u] = currentLabel
            for w in graph[u]:
                bag.append(w)


def calculate_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5


def main():
    for _ in range (int(input())):
            x, y = input().split()
    


if __name__ == "__main__":
    main()