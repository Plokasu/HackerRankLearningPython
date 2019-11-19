if __name__ == '__main__':
    s = input()
    has_alph_num = False
    has_alpha = False
    has_digits = False
    has_lower = False
    has_upper = False

    for char in s:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        
        if char.isalpha():
            has_alph_num = True
            has_alpha = True
        elif char.isdigit():
            has_alph_num = True
            has_digits = True

    print("True" if has_alph_num else "False")
    print("True" if has_alpha else "False")
    print("True" if has_digits else "False")
    print("True" if has_lower else "False")
    print("True" if has_upper else "False")
