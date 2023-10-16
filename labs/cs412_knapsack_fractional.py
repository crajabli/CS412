"""
    name:  Chingiz Rajabli

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
  
           Comments here on your code and submission.
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def main():
    items = []
    max_bag_size = int(input())
    for item in range(int(input())):
        items.append(tuple(input().split()))
    items = list(map(lambda x: (x[0], int(x[1]), int(x[2])), items))
    taken_items = sack(items, max_bag_size)
    print(" ".join(f"{item[0]}({item[1]:.2f}, {item[2]:.2f})" for item in taken_items))
    print(sum(item[1] for item in taken_items))

def sack(items, weight):
    sorted_items = sorted(items, key=lambda x: x[1] / x[2])
    sorted_items.reverse()
    taken_items = []

    for item in sorted_items:
        if weight >= item[2]:
            taken_items.append(item)
            weight -= item[2]
        else:
            ratio = weight / item[2]
            taken_items.append((item[0], item[1] * ratio, item[2] * ratio))
            break
    return taken_items


if __name__ == '__main__':
    main()


"""
1. fractional knapsack problem is easier to solve as we just sort the items based on their weight
to value ratio and then take as much as we can from the most valuable item and then move on to the next
and if we cant fit it we just take the fraction of it as much as we can fit in the bag

2.I dont think it would work correctly as in the 0/1 knapsack problem we are trying to maximize the value
and we have cant just be greedy and take whatever has most value to weight ratio 

3.lets say we just have 11 space ring 100 5 gold 50 10 silver 50 5
in normal knap sack we would have taken ring and gold and in fractional we would have taken ring and gold and silver

"""