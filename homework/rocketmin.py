def bakeRocket(section, length):
    if (length % section[-1] == 0):
        return length // section[-1]
    
    minimum = float("inf")
    for i in section:
        count =  length // i
        minimum = min(minimum, count + bakeRocket(section[:-1], length % i))

    return minimum


def main():
    section = list(map(int, input().split()))
    length = int(input())
    num = bakeRocket(section, length)
    print(f"{num} rocket sections minimum")


if __name__ == '__main__':
    main()

