sender = input("What is your name? = ")

typeOfItem = input("What type of item? = ")

isFragile = bool(input('Is your item fragile? (Yes/No) =') == 'Yes')

weight = float(input("What is the weight(KG) of your item? = "))

distance = float(input("How far is the destination(KM)? = "))

isExpress = bool(input("Is your delivery a priority? (Yes/No) = ") == 'Yes')

isInternational = bool(input("Is the destination international? (Yes/No)= ")=='Yes')


baseCost = (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <= 100 and not isExpress and not isInternational:
	Total = 0.00

elif isInternational == True and isExpress == True:
	Total = (baseCost * 1.40) + 50

elif isExpress == True or (isInternational == True and weight > 20):
	Total = (baseCost * 1.20) + 25

elif weight > 30 or distance > 1000:
	Total = baseCost + 30

else:
	Total = baseCost

shippingFee = Total - baseCost


print('--------------------------------------------------------')
print('Sender = ', sender)
print('Fragile = ', typeOfItem)
print('Weight = ', weight)
print('Distance = ', distance)
print('Priority = ', isExpress)
print('International = ', isInternational)
print('Base Cost = ', baseCost)
print('Shipping Fee =', shippingFee)
print('Total =', Total)
