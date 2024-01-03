#2. Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.
a=int(input("enter temperature in fahrenheit: "))
con=(a - 32) * 5/9
print(con,'celcius')