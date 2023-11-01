def railroad(cities):
    count = len(cities)
    city_connections = {i:{j:calculate_distance(cities[i], cities[j]) for j in range(count) if j != i} for i in range(count)}
    visited_cities = [False] * count

    return greedy_dfs(visited_cities, city_connections, 0)


def greedy_dfs(visited, connections, start):
    cost = 0
    while -1:        
        if visited.count(False) == 1:
            break

        visited[start] = True
        
        shortest_track = float("inf")
        next_city = -1
        for city in [connections[c] for c in range(len(visited)) if visited[c] == True]:            
            unvisited = [key for key in city if visited[key] == False]
            for stop in unvisited:
                if city[stop] < shortest_track:
                    shortest_track = city[stop]
                    next_city = stop
        
        cost += shortest_track + greedy_dfs(visited, connections, next_city)
        
    return cost


def calculate_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5


def main():
    n = int(input())
    cities = []
    for _ in range(n):
        x, y = map(float, input().split())
        cities.append((x, y))
    cost = railroad(cities)
    print(f"${cost:.1f}M")


if __name__ == "__main__":
    main()

 
