#7.  Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive
num=int(input("enter any number: "))
if num<=12:
    for x in range (0,13):
        mul=num*x
        print(x,"x",num,"=",mul)
else:
    print("the number should be under or equal to 12")   