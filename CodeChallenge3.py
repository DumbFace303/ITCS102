sender = input("What is your name? = ")

typeOfItem = input("What type of item? = ")

isFragile = bool(input("Is your item fragile? = "))
if isFragile == True:
	print("Positive")
else:
	print("Negative")

weight = float(input("What is the weight(KG) of your item? = "))

distance = float(input("How far is the destination(KM)? = "))

isExpress = bool(input("Is your delivery a priority? = "))
if isExpress == True:
	print("Positive")
else:
	print("Negative")

isInternational = bool(input("Is the destination international? = "))
if isInternational == True:
	print("Positive")
else:
	print("Negative")



baseCost = (weight * 2.50)+(distance * 0.15)

internationalExpress = total
	total = (baseCost*1.40)+50

heavyInternational = total2
	total2 = (baseCost*1.20)+25

overSized = total3
	total3 = baseCost+30