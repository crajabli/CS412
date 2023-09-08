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

        

def find(in_list, search_item):
    middle = int(len(in_list) / 2)
    
    if (in_list[middle] == search_item):
        return middle

    if (middle - 1 >= 0 and in_list[middle - 1] == search_item):
        return middle - 1
    
    if (middle + 1 < len(in_list) and in_list[middle + 1] == search_item):
        return middle + 1

    if (middle == 0 or len(in_list) <= 2):
        return -1   
    
    if (in_list[middle + 1] < in_list[-1]):
        if (search_item >= in_list[middle + 1] and search_item <= in_list[-1]):
            result = find(in_list[middle:], search_item)
            return -1 if result == -1 else middle + result 
        else:
            return find(in_list[:middle], search_item)
    else:
        if (search_item >= in_list[0] and search_item <= in_list[middle]):
            return find(in_list[:middle], search_item)
        else:
            result = find(in_list[middle:], search_item)
            return -1 if result == -1 else middle + result


if __name__ == "__main__":
    main()