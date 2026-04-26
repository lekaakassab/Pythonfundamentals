#1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = abs(w)
        self.h = abs(h)

    def area(self):
        return self.w * self.h

    def circumference(self):
        return 2 * (self.w + self.h)

    def bottom_right(self):
        return Point(self.x + self.w, self.y + self.h)

    def overlap(self, other):
        left = max(self.x, other.x)
        right = min(self.x + self.w, other.x + other.w)
        top = max(self.y, other.y)
        bottom = min(self.y + self.h, other.y + other.h)
        if right <= left or bottom <= top:
            return None
        return Rectangle(left, top, right - left, bottom - top)


r1 = Rectangle(0, 0, 5, 3)
r2 = Rectangle(2, 1, 4, 3)

print(r1.w, r1.h)
print(r1.area())
print(r1.circumference())

p = r1.bottom_right()
print(p.x, p.y)

o = r1.overlap(r2)
if o:
    print(o.area())
else:
    print("no overlap")

#2
from datetime import date

class Course:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Student:
    def __init__(self, firstname, lastname, birth_year, birth_month, birth_day, admin_number):
        self.firstname = firstname
        self.lastname = lastname
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.admin_number = admin_number
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def age(self):
        today = date.today()
        return today.year - self.birth_year


c1 = Course("Math", 101)
c2 = Course("Python", 202)
c3 = Course("History", 303)

s1 = Student("Ahmad", "Ali", 2005, 5, 10, 1)
s2 = Student("Sara", "Omar", 2003, 8, 20, 2)

s1.enroll(c1)
s1.enroll(c2)

s2.enroll(c2)
s2.enroll(c3)

students = [s1, s2]

for s in students:
    print(s.admin_number, s.firstname, s.lastname, s.age())
    for c in s.courses:
        print(c.name)
    print()

   #3
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def circumference(self):
        return 2 * (self.w + self.h)


class Square(Rectangle):
    def __init__(self, x, y, side):
        super().__init__(x, y, side, side)


r = Rectangle(0, 0, 4, 2)
s = Square(1, 1, 3)

print(r.area())
print(r.circumference())

print(s.area())
print(s.circumference())



#4
import math


class Shape:
    def area(self):
        pass

    def circumference(self):
        pass


class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def circumference(self):
        return 2 * (self.w + self.h)


class Square(Rectangle):
    def __init__(self, x, y, side):
        super().__init__(x, y, side, side)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


r = Rectangle(0, 0, 4, 2)
s = Square(1, 1, 3)
c = Circle(5)

print(r.area(), r.circumference())
print(s.area(), s.circumference())
print(c.area(), c.circumference())