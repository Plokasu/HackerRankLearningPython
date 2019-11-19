if __name__ == '__main__':
    N = int(input())

    myList = []

    while N > 0:
        command = input().split(" ")

        if len(command) > 1:
            command[1] = int(command[1])
        if len(command) > 2:
            command[2] = int(command[2])

        if command[0] == "insert": 
            myList.insert(command[1], command[2])
        elif command[0] == "print":
            print(myList)
        elif command[0] == "remove":
            myList.remove(command[1])
        elif command[0] == "append":
            myList.append(command[1])
        elif command[0] == "sort":
            myList.sort()
        elif command[0] == "pop":
            myList.pop()
        elif command[0] == "reverse":
            myList.reverse()
        
        N -= 1
