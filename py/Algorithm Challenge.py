#1
"""
total = 0
for i = 200 to 2700:
    if (3 or 5) but not both:
        total += i
print total
"""
total = 0

for i in range(200, 2701):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        total += i

print(total)



#2
"""
if n == 1 or n == 2 → return 1
else → return rFib(n-1) + rFib(n-2)
"""
def rFib(n):
    if n == 1 or n == 2:
        return 1
    return rFib(n - 1) + rFib(n - 2)

#3
"""
split sentence into words
set longest = ""

for each word:
    if len(word) > len(longest):
        longest = word

return longest
"""
def longest_word(s):
    words = s.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

#4
"""
clean string (lowercase + remove spaces/punctuation)
reverse string
if same → return True
else → return False
"""
def is_palindrome(s):
    s = s.lower()
    s = "".join(c for c in s if c.isalnum())
    
    return s == s[::-1]
# T-Diagram
# Input  | Process            | Output
# kayak  | reverse & compare  | True

#5
"""
create new array
for each number in array:
if number >= 0:
add to new array
return new array
"""
def remove_negative(arr):
    result = []
    
    for num in arr:
        if num >= 0:
            result.append(num)
    
    return result
# T-Diagram
# [1, -2, 3] → remove negatives → [1, 3]