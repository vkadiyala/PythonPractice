#Take two lists, say for example these two:
#
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.#
#
#Extras:
#
#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

#call this below 2 statements instead of function
#import importlib
#importlib.import_module("fibonacci.py")

def febo(num):
    v1 = v2 = 1
    fib = []
    fib.append(1)

    while v2 < num:
        fib.append(v2)
        total = v1 + v2
        v1 = v2
        v2 = total
    return fib

a = febo(60)
b = list(range(1,20,1))

print(a)
print(b)

common = []

for elem in a:
    for elem2 in b:
        if elem2 == elem:
            common.append(elem)
            break

print(f'Common values in the above 2 lists: {common}')


