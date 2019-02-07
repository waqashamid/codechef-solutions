# Authored by: Waqas Hamid
# Github: waqashamid
# Kaggle: waqashamid
# Contact: waqashamid722@gmail.com

def gcd(a, b):
    if (a == b):
        return a
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)

def lcm(a, b):
    return (a * b) / gcd(a, b)

def calculate_winning_chances():

    T = int(input())
    while T:
        N, A, B, K = map(int, input().strip().split())
        ans = int(N/A) + int(N/B) - 2*(int(N/lcm(A, B)))
        if ans >= K:
            print("Win")
        else:
            print("Lose")
        T -= 1

if __name__=='__main__':
    calculate_winning_chances()