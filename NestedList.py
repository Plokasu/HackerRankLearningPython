# https://www.hackerrank.com/challenges/nested-list/problem
def sortScore(obj):
    return obj[1], obj[0]

if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])

    arr.sort(key=sortScore)
    
    minScore = min(x[1] for x in arr)
    
    list2 = []

    for n in arr:
        if n[1] == minScore:
            arr.remove(n)

    minScore = min(x[1] for x in arr)

    for n in arr: 
        if n[1] == minScore:
            print(n[0])
