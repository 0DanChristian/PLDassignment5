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

# greetings
print("\33[1mWelcome! This will be your realization!")
import math
def rounded_grade(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
    
grAde = float(input('Please enter your \033[1mgrade: '))

if grAde.isdigit() == True:
    rndd_grd = rounded_grade(float(grAde))
        # Uno
    if rndd_grd >= 97 and rndd_grd <= 100:
        print("\033[92m1.0 is your grade! Excellent!")

        # Uno jr.
    elif rndd_grd >= 94 and rndd_grd <= 96:
        print("\033[92m1.25 is your grade! Excellent!")
    elif rndd_grd >= 91 and rndd_grd <= 93:
        print("\033[92m1.5 is your grade! Very Good")
    elif rndd_grd >= 88 and rndd_grd <= 90:
        print("\033[92m1.75 is your grade! Very Good!") 

        # dos
    elif rndd_grd >= 85 and rndd_grd <= 87:
        print("\033[93m2.0 is your grade! It was good! keep it up ")
    elif rndd_grd >= 82 and rndd_grd <= 84:
        print("\033[93m2.25 is your grade! It was good! keep it up!")
    elif rndd_grd >= 76 and rndd_grd <= 78:
        print("\033[93m2.75 is your grade! Satisfactory, keep it up buddy!")

        # failed 
    elif rndd_grd >= 65 and rndd_grd <= 74:
        print("\033[91mUnfortunately, you failed. Your grade is 5.0")

        # tres    
    elif rndd_grd <= 75:
        print("\033[93mYour grade is 3.0, its passing. Keep it up! hard work pays off") 

        # inc,w,d
else:
    special_case = grAde.title()
        # inc
    if grAde == "Incomplete" or grAde == "INCOMPLETE" or grAde == "incomplete" or grAde == "INC." or grAde == "Inc." or grAde == "inc." or grAde == "inc":
        print("Given the data provided, the case of this student is \033[91mIncomplete.")
        # withdrawn
    if grAde == "Withdrawn" or grAde == "withdrawn" or grAde == "w" or grAde == "W":
        print("Given the date provided, this student has \33[93mwithdrawn.")
        # dropped
    if grAde == "Dropped" or grAde == "dropped" or grAde == "d" or grAde == "D":
        print("Given the data provided, this student has already \33[1mdropped.")






