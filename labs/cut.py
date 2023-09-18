from functools import cache as cache

@cache
def log_cut(L):
    global price
    if L == 0:
        return 0
    if L == 1:
        return price[L]
    
    best_price = float("-inf")
    for log_length in price:
        if L - log_length >= 0:
            this_price = price[log_length] + log_cut(L - log_length)
        best_price = max(best_price, this_price)
    
    return best_price
    


def main():
    global price
    price = {
        1: 1,
        2: 4,
        3: 3,
        4: 3,
        5: 3,
    }
    print(log_cut(int(input())))

if __name__ == '__main__':
    main()