#1 1 2 3 5 8

print("want to see the fibonacci series for a number? give  try! type a number below")
num = int(input())

v1 = v2 = 1
fib = []
fib.append(1)

while v2 < num:
    fib.append(v2)
    total = v1 + v2
    v1 = v2
    v2 = total
    
print(f"Here is the possible fibonacci sequence for your number: {fib}")
