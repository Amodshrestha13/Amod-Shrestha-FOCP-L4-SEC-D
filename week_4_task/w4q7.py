# Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean.
def amd():
    temp_list=[]
    n=6
    for a in range(n):
        a=int(float("enter the temperature: "))
        temp_list.append(a)
    print(temp_list)
    maximum=max(temp_list)
    minimum=min(temp_list)
    total=sum(temp_list)
    mean=total/len(temp_list)
    print("maximum temperature is: ",maximum)
    print("minimum temperature is: ",minimum)
    print("mean temperature is: ",mean)
amd()  