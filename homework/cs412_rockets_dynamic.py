

def build_rocket(sections, length):
    rocketTable = [(float("inf")) * (length + 1) for _ in range(len(sections) + 1)]

    for i in range(len(sections) + 1):
        rocketTable[i][0] = 0

    for i in range(1, len(sections) + 1):
        for j in range(1, length + 1):
            for k in range(i):
                x = j // sections[k]
                y = j % sections[k]
                rocketTable[i][j] = min(rocketTable[k][y] + x, rocketTable[i][j] + x)
    print(rocketTable)
    minSections = [0] * len(sections)
    total = length

    while total != 0:
        index = len(sections)
        for i in range(len(sections)):
            if rocketTable[i][total] <= rocketTable[index][total] and sections[i - 1] <= total:
                index = i
        sections = total // sections[index - 1]
        total = sections * sections[index - 1]
        minSections[index - 1] = sections
    
    return minSections


def main():
    rocket_section = list(map(int, input().split()))
    length = int(input())
    minimum = [0] * len(rocket_section)
    sections = build_rocket(rocket_section, length)

    for i in range(len(sections)):
        print(f"{sections[i]} of length {rocket_section[i]}")
    print(f"{sum(sections)} rocket sections minimum")


if __name__ == '__main__':
    main()