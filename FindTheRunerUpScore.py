# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    maxNum = max(arr)

    while (maxNum in arr):
        arr.remove(maxNum)

    print(max(arr))
