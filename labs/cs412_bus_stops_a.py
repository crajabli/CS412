"""
    name:  Chingiz Rajabli

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
  
           Comments here on your code and submission.
"""

def bus(routes, start, end):
    stack = []
    visited = []
    def dfs(current_stop):
        stack.append(current_stop)
        visited.append(current_stop)
        if current_stop == end: return True
        for stop in routes[current_stop]:
            if stop not in visited:
                if dfs(stop): return True
                stack.remove(stop)
        return False
    if dfs(start): return stack
    else: return []

    

def main():
    routes = {}
    for _ in range(int(input())):
        u, v = input().split()
        routes[u] = routes.get(u, set())
        routes[u].add(v)

        routes[v] = routes.get(v, set())
        routes[v].add(u)

    start, stop = input().split()
    route = bus(routes, start, stop)
    if len(route) == 0: print("no route possible")
    else: print(" ".join(route))

if __name__ == "__main__":
    main()