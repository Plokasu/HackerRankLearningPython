def swap_case(s):
    retStr = ""
    for char in s:
        if char.isupper():
            retStr += char.lower()
        else:
            retStr += char.upper()
    return retStr

def swap_case1(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
