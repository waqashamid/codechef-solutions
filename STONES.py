# Authored by: Waqas Hamid
# Github: waqashamid
# Kaggle: waqashamid
# Contact: waqashamid722@gmail.com


def count_jewel_stones():

    T = int(input())
    while T:
        J =input().strip()
        S =input().strip()
        count = 0
        for i in range(len(S)):
            if S[i] in J:
                count += 1
        print(count)
        T -= 1

if __name__=='__main__':
    count_jewel_stones()