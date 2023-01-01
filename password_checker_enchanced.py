"""Basic Password checker script"""

def check_strength(passwd: str) -> bool:
    """A strong password must be at least 8 characters long
       and must contain a lower case letter, an upper case letter,
       and at least 3 digits.
       Returns True if passwd meets these criteria, otherwise returns False.
       """
    # check password length; return False if too short
    if len(passwd) < 8:
        return False

    # check password for uppercase, lowercase and numeric chars
    hasupper = False
    haslower = False
    digitcount = 0
    
    for c in passwd:
        if c.isupper():
            hasupper = True
        elif c.islower():
            haslower = True
        elif c.isdigit() or c.isnumeric():
            digitcount += 1
    if hasupper and haslower and digitcount >= 3:
        return True
    else:
        return False
    
def main():
    check = False
    while not check:
        passwd = input('Enter your password to check its strength: ')
        result = check_strength(passwd)
        if result:
            print(f'[*] Password {passwd} is strong')
            check = True
        else:
            print(f'[*] Password {passwd} is NOT strong. Try again')
            check 

if __name__ == '__main__':
    main()
