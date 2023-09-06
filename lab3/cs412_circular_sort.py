"""
    name:  Chingiz Rajabli

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
              https://stackoverflow.com/q/19798480
  
           Comments here on your code and submission.
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    in_list = list(map(int, input().split()))
    search_item = int(input())
    print(find(in_list, search_item))


def find (in_list, search_item):
    middle = int (len(in_list) / 2)
    
    if in_list[middle] == search_item:
        return middle
    elif len(in_list) == 0:
        return -1
    else:
        if in_list[middle] <= search_item and in_list[-1] >= search_item:
            return find(in_list[middle : len(in_list)], search_item) + middle
        else:
            return find(in_list[0: middle], search_item)
    
    


if __name__ == "__main__":
    main()