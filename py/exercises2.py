#1
num = 9
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#2
for x in range(1, 11, 1): 
    print(x)

#3
num = 10
while num >= 1:
    print(num)
    num -= 1

#4
for n in range(2, 21, 2):
    print(n)

#5
num = int(input("Enter number: "))

if num >= 100:
    print("Big number!")
else:
    print("Small number!")