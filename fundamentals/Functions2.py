#Countdown
def countdown(x):
    listnum = []
    for i in range(x,-1,-1):
        listnum.append(i)
    return listnum

DisList = countdown(5)
print(DisList)

print("===============================================")

#Print and Return
def print_and_return (x):
    print(x[0])
    return x[1]

x = print_and_return([1,2])
print(x)

print("===============================================")

#First Plus Length
def first_plus_length(x):
    return x[0]+len(x)

x = first_plus_length([1,2,3,4,5])
print(x)

print("===============================================")

#This Length, That Value
def length_and_value(num1, num2):
    newlist = []
    for i in range(num1):
        newlist.append(num2)
    return newlist

x = length_and_value(4,7)
print(x)

print("===============================================")

#Values Greater than Second (Optional)
def values_greater_than_second(x):
    newlist = []
    if len(x) < 2:
        return False
    else:
        for i in range(0, len(x)):
            if(x[i]>x[1]):
                newlist.append(x[i])
    return newlist
    
x = values_greater_than_second([5,2,3,2,1,4])
print(x)