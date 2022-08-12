letters=["a", "b","c", "d", "e", "f", "h", "i", "j", "l", "o", "r", "t", "y"]
numbers=["0","1","3", "4", "7", "8","6"]
symbols=["&","$","#", "@","!","*"]
print("welcome to the password generator")
nr_letter=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("how many symbols you would like?\n"))
nr_numbers=int(input("how many numbers would you like?\n"))
import random
password=""
for char in range(1,nr_letter+1):
    password+=random.choice(letters)
    #print(password)
for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)
    #print(password)
for char in range(1, nr_symbols+1):
    password+=random.choice(symbols)
    #print(password)
print(password)