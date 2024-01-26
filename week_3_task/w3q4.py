#4. Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
def amd():
    x = str(input("enter a password: "))
    y = str(input("re enter the password: "))
    return password(x, y)


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


def password(a, b):
    if a in BAD_PASSWORDS:
        print("this password is bad, please choose another")

    else:
        if 8 <= len(a) <= 12:
            if a == b:
                print("password set")
            else:
                print("error setting the password")
        else:
            print("inapproprite password")


amd()