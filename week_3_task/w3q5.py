#5. Modify your program a final time so that it executes until the user successfully
# chooses a password. That is, if the password chosen fails any of the checks, the
# program should return to asking for the password the first time.
def amd():
    while True:
        x = str(input("enter a password: "))
        y = str(input("re enter the password: "))
        output = password(x, y)
        print(output)
        if output == "PASSWORD SET":
            break


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


def password(a, b):
    if a in BAD_PASSWORDS:
        return "THIS PASSWORD IS A BAD PASSWORD, CHOOSE ANOTHER PASSWORD"
    elif len(a) < 8 or len(b) > 12:
        return "INAPPROPRIATE LENGTH"
    elif a != b:
        return "PASSWORD DOESNT MATCH" 
    else:
        return "PASSWORD SET"

amd()