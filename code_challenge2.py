money = int(input("Money="))


print("1000 =", money // 1000)
print("500 =", (money % 1000) // 500)
print("200 =", (money % 500) // 200)
print("100 =", (money % 200) // 100)
print("50 =", (money % 100) // 50)
print("20 =", (money % 50) // 20)
print("10 =", (money % 20) // 10)
print("5 =", (money % 10) // 5)
print("1 =", (money % 5) // 1)
