#1. Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).
def accept(m):
    

    a=[]

    if m>0:
        while m!=0:
            a.append(m%2)
            m=m//2
        print(a)
    else:
        print("negative integers are not taken. please enter positive integers above 0")    
accept(int(input("enter a positive number: ")))    