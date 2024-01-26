# Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format.

def temp(dig):
    f=5/9*(dig-32)
    return f
       
d=float(input("enter temperature in digits: ")) 
print(temp(d))