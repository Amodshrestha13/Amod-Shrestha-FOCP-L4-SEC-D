#4. A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.
sweet=int(input("enter the number of sweets in the tube: "))
students=int(input("enter the number of stdents present that day:  "))
di=sweet//students
leftovers=sweet%students
print("each student will get",di)
print("leftovers=",leftovers)