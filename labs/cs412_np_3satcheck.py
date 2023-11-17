import itertools


def check_3sat(x1, x2, x3):
    return (x1 or x2 or x3) and (not x1 or x2 or x3) and (x1 or not x2 or x3) and (x1 or x2 or not x3) and \
        (not x1 or not x2 or x3) and (not x1 or x2 or not x3) and (x1 or not x2 or not x3) and (not x1 or not x2 or not x3)


def check_3sat_bad(x1, x2, x3):
    return (x1 or x2 or x3) and (not x1 or x2 or x3) and (x1 or not x2 or x3) and (x1 or x2 or not x3) and \
        (not x1 or not x2 or x3) and (not x1 or x2 or not x3) and (x1 or not x2 or not x3)

def main():
    it = itertools.product([True, False], repeat=3)
    for x1, x2, x3 in it:
        print(check_3sat_bad(x1, x2, x3))

        
    


if __name__ == '__main__':
    main()