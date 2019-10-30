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

    for n in range(0, len(arr)):
        if arr[n][1] != minScore:
            list2.append(arr[n])    

    minScore = min(x[1] for x in list2)

    for n in range(0, len(list2)): 
        if list2[n][1] == minScore:
            print(list2[n][0])
