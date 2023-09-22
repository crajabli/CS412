

def build_rocket(sections, length, minimum):
    if (length % sections[-1] == 0):
        minimum[-1] = length // sections[-1]
        return minimum
    
    minimum_section = [float("inf")]

    for i in range(len(sections)):
        minimum_copy = minimum.copy()
        count = length // sections[i]
        minimum_copy[i] = count
        
        parallel_copy = build_rocket(sections[:-1], length % sections[i], minimum_copy[:-1])

        for j in range(len(parallel_copy)):
            minimum_copy[j] += parallel_copy[j]

        if (sum(minimum_copy)) < sum(minimum_section):
            minimum_section = minimum_copy
        
    return minimum_section


def main():
    rocket_section = list(map(int, input().split()))
    length = int(input())
    minimum = [0] * len(rocket_section)
    sections = build_rocket(rocket_section, length, minimum)

    for i in range(len(sections)):
        print(f"{sections[i]} of length {rocket_section[i]}")
    print(f"{sum(sections)} rocket sections minimum")


if __name__ == '__main__':
    main()