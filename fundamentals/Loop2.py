#Biggie Size
def biggie_size(x):
    for i in range(0, len(x)):
        if(x[i]>=0):
            x[i]='big'
    return x

x = biggie_size([-1, 3, 5, -5]) 
print(x)

print("===============================================")

#Count Positives
def count_positives(x):
    count=0
    for i in range(0, len(x)):
        if x[i] > 0:
            count+=1
        if len(x) == (i+1):
            if x[i]>= 0:
                count+=1
            x[i]=count
    return x

x = count_positives([1,6,-4,-2,-7,-2])
print(x)

print("===============================================")

#Sum Total
def sum_total(x):
    sum = 0
    for i in range(0, len(x)):
        sum += x[i]
    return sum

x = sum_total([1,2,3,4])
print(x)

print("===============================================")

#Average
def average(x):
    sum = 0
    for i in range(0, len(x)):
        sum += x[i]
    return sum/len(x)

x = average([1,2,3,4])
print(x)

print("===============================================")

#Length
def length(x):
    return len(x)

x = length([37,2,1,-9])
print(x)

print("===============================================")

#Minimum
def minimum(x):
    min = x[0]
    if(len(x) == 0):
        return False
    else:
        for i in range(0, len(x)):
            if(x[i]<min):
                min=x[i]
    return min

x  = minimum([37,2,1,-9])
print(x)

print("===============================================")

#Maximum
def Maximum(x):
    max = x[0]
    if(len(x) == 0):
        return False
    else:
        for i in range(0, len(x)):
            if(x[i]>max):
                max=x[i]
    return max

x  = Maximum([37,2,1,-9])
print(x)