def factorial(factnum=1):
    factorial = 1
    for i in range (1,factnum+1):
        factorial = factorial * i
    return factorial

print("what number you want to calculate factorial:")
factnum = int(input())
s = factorial(factnum)
print(f' {factnum} factorial is : {s}')
   
