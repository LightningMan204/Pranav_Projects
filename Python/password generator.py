import random as rand

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{-}=|:<>?"
length = int(input("enter length: "))
password = ""

for a in range(length):
    password+=rand.choice(chars)

print(password)