#1. Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.
print("hello,what is your name? ")
name=input("enter your name: ")
if name=="":
    print("hello, stranger. good to meet you")
else:
    print("hello,",name, 'good to meet you')