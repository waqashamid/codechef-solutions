# Authored by: Waqas Hamid
# Github: waqashamid
# Kaggle: waqashamid
# Contact: waqas7hamid@gmail.com
# Problem: https://www.codechef.com/problems/ERROR

def main():

    T = int(input())
    for i in range(T):
        str = input()
        if str.find("010")!=-1 or str.find("101")!=-1:
            print("Good")
        else:
            print("Bad")

if __name__ == '__main__':
    main()