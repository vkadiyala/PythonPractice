input1 = int(input("filter the min price between 1 to 10:"))
input2 = int(input("filter the max price between 1 to 10:"))

'price range accepted' if input2 > input1 else 'Enter the max price value again!'
#input2 = int(input("filter the max price between 1 to 10:"))


list = [1,9,8,7,6,5,4,3,2,10]
list.sort()
print(list)
finallist = list[input1-1:input2]
print(finallist)
    
    
    