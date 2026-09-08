#and = &&
#or = !!
#not = !


a = 10
b = 8
c = 13

print(a > b or c < a)

print (a > b or c < a and c == a)

print (not(a > b or c < a and c == a))