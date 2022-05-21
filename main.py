def z():
    print("spam")
    print("spam")
    print("spam")
z()

def print_with_exclamation(word):
    print(word + "!")
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

def print_sum_twice(x, y):
    print(x + y)
    print(x + y)
print_sum_twice(5, 8)

def function(variable):
    variable += 1
    print(variable)
function(7)
#print(variable)

def max(x, y):
    if x >=y:
        return x
    else:
        return y

print(max(4, 7))
z = max(8, 5)
print(z)


def add_numbers(x, y):
    total = x + y
    return total
    #print("This won't be printed")

print(add_numbers(4, 5))

def add(x, y):
    return x + y
def do_twice(func, x, y):
    return func(func(x, y), func(x, y))
a = 5
b = 10
print(do_twice(add, a, b))


#Module

import random
for i in range(5):
    value = random.randint(1, 6)
    print(value)

from math import pi
print(pi)



import module_1
module_1.greeting("Jonathan")

print(module_1.pic)

import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

list = []
for i in range (5):
    a = int(input("Enter Your number: "))
    list.append(a)

b = list[0] + list[3]

print(list, b)

