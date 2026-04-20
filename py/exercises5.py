#1
t = ("apple", "banana", "cherry", "date")

print(t[0])      
print(t[-1])     
print(t[1:3])    

#2
tuple1 = 'a', 'b', 'c'
tuple2 = 'd', 'e', 'f'
new_tuple = tuple1 + tuple2
print(new_tuple)
print(tuple1 * 2)

#3
t = (10, 20, 30, 40, 50)
a, b, *rest = t
print(a)
print(b)
print(rest)
print(t.count(20))
print(t.index(40))