#5. Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae).
def temp(tem,dig):
    a="f"
    b="c"
    if tem==a:
        cent=dig*(9/5)+32
        return cent
    elif tem==b:
        fen=5/9*(dig-32)
        return fen
    else:
        print("error")        
te=input("enter 'f' for fahrenheit and 'c' for centigrade: ")
d=float(input("enter temperature in digits: "))  
print(temp(te,d)) 
