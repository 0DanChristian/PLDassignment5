# program #3: life stages 
# 0-12      = kid
# 13-17     = teen
# 18        = debut
# 19 above  = adult


age = int(input("Please enter your age:"))
if age >= 0 and age <= 12:
	print('kid')
elif age >= 13 and age <= 17:
	print('Teen')
elif age <= 18:
	print('Debut')
else:
	print('Adult')

print("Done!")


#inspired by the reporters who used shortened method


