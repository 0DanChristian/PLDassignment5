# create a program that asks for 3 numebrs
# find the lowest number 

# ask for the first number
first_no = int(input("Enter your first desired number: "))
# ask for the second number 
second_no = int(input("Enter your second desired number: "))
# ask for the third number
third_no = int(input("Enter your third desired number: "))
# what number is the smallest
smallest = 0
# your statement
if first_no < second_no and first_no < third_no :
    smallest = first_no
if second_no < first_no and second_no < third_no :
    smallest = second_no
if third_no < first_no and third_no < second_no :
    smallest = third_no
# display
print(smallest, "is the smallest of your three desired numbers.")

# neat