#1
def multiply_table(num):
    for z in range(1, 11):  
        print(z, "x", num, "=", z * num)

#2
def letter(s1, s2): 
    letter = set(s1) & set(s2) 
    return len(letter)

print(letter("bee", "peer"))


#3
import random

def number(user_num):
    secret = random.randint(1, 10)

    if user_num > secret:
        return "Too big"
    elif user_num < secret:
        return "Too small"
    else:
        return "You are SUPER"

num = int(input("Enter number: "))
print(number(num))