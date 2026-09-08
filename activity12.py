#Conditional Statement

import getpass

username = "user1"
password = "password123"

u = input("Input Username = ")
p = getpass.getpass("Input Password = ")

if username == u and password == p :
	print('"ACCESS GRANTED"')
else : 
	print('"ACCESS DENIED"')


