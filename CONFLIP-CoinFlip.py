# Authored by: Waqas Hamid
# Github: waqashamid
# Kaggle: waqashamid
# Contact: waqas7hamid@gmail.com

import psyco
psyco.full()

import math
def main():
    t = int(input())
    while t:
        g = int(input())
        while g:
            i, n, q = map(int, input().strip().split())
            if n%2 == 0:
                print(math.floor(n/2))
            else:
                if q == i:
                    print(math.floor(n/2))
                else:
                    print(math.ceil(n/2))
            g-=1
        t-=1


if __name__=='__main__':
    main()
