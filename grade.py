# program #2: grading
# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed

import math
import decimal

grade = int(input("Please enter your grade: "))
# Uno
if grade >= 97 and grade <= 100:
    print("1.0 is your grade! Excellent!")
elif grade >= 94 and grade <= 96:
    print("1.25 is your grade! Very Good!")
elif grade >= 91 and grade <= 93:
    print("1.5 is your grade! Very Good")
elif grade >= 88 and grade <= 90:
    print("1.75 is your grade! Very Good!") 
elif grade >= 85 and grade <= 87:
    print("2.0 is your grade! It was good! keep it up ")
elif grade >= 82 and grade <= 84:
    print("2.25 is your grade! It was good! keep it up!")
elif grade >= 76 and grade <= 78:
    print("2.75 is your grade! Satisfactory, keep it up buddy!")
elif grade >= 65 and grade <= 74:
    print("Unfortunately, you failed. Your grade is 5.0")

elif grade <= 75:
    print("Your grade is 3.0, its passing. Keep it up! hard work pays off")

print("Done!")

# my 2nd attempt, it was much easier and less hassle this way