#3. Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.
import sys
def amd():
    a=sys.argv[1:]
    a.sort(key=len)
    return a[0]
print(amd())   
