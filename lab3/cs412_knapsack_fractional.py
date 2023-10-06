
def main():
    weight = int(input())
    num_items = int(input())
    items = []
    for _ in range(num_items):
        items.append(tuple(map(int, input().split())))
    pass

if __name__ == '__main__':
    main()