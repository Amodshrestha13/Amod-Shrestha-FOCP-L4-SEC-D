#2. Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.
passw1=input("enter new password: ")
passw2=input("enter password: ")
if passw1==passw2:
    print("password set")
else:
    print("error")   