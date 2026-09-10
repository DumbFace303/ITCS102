


age = int(input("Input Age = "))

if age >= 1 and age <=5:
	print("Infant")

elif age >= 6 and age <= 12:
	print("Kid")

elif age >= 13  and age <= 19 :
	print("Teenager")

elif age >= 20 and age <= 29:
	print("Early Adulthood")

elif age >= 30 and age <= 45:
	print("Adult")

elif age >= 46 and age <= 59 :
	print("Advance Adulthood")

elif age >= 60 and age <= 150:
	print("Senior")

else:
	print("Invalid")