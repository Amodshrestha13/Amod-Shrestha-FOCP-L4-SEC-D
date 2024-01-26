# write and test a function that determines if a given integer is a prime number. A
# prime number is an integer greater than 1 that cannot be produced by multiplying
# two other integers.
def prime(num):
    if num==1:
        print("enteres integer is a prime number")
    elif num>1:
        if num%2==0:
            print("entered integer is not a prime number")
        else:
            print("entered integer is a prime number")
    else:
        print("entered integer is not a prime number")                
prime(int(input("enter a integer: ")))    
