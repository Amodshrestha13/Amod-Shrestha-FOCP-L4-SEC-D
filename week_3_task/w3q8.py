#8. Modify the "Times Table" again so that the user still enters the number of the table,
# but if this number is negative the table is printed backwards. So entering "-7"
# would produce the Seven Times Table starting at "12 times" down to "0 times".
num=int(input("enter a number: "))
if num<0:
    for a in range(12,-1,-1):
        multi1=num*a
        print(a,"x",num,"=",multi1)
else:
    for x in range (0,13):
        multi2=num*x
        print(x,"x",num,"=",multi2)        