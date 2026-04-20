#1
import random
answers = ["yes", "no", "maybe"]
question = input("Ask a question: ")
print(random.choice(answers))

#2
queue = []

while True:
    user = input("Enter: ")
    if user == "":
        break
    elif user == "?":
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print("Queue is empty")
    else:   
        queue.append(user)

#3
a, b = 0, 1

for i in range(10):
    print(a)
    a, b = b, a + b

#4
def counting_number(sub, string):
    count = string.count(sub)
    result = ""
    for letter in string:
        if letter not in result:
            result += letter 
    print("Count:", count)
    print("Without duplicates:", result)
counting_number("an", "banan")

#5
def is_palindrome(word):
    if word == word[::-1]:
        return "Yes"
    else:
        return "No"
print(is_palindrome("radar"))
print(is_palindrome("hello"))

#6
def largest_number(num): 
    return max(num) 
print(largest_number([10, 20, 4]))