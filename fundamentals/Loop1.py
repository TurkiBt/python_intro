#Basic
for i in range(0,151):
    print(i)

print("===============================================")

#Multiples of Five
for i in range(5,1001):
    print(i*5)

print("===============================================")

#Counting, the Dojo Way
for i in range(1,101):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Coding Dojo")

print("===============================================")

#Whoa. That Sucker's Huge
sum=0
for i in range(0,500001):
    if i % 2 != 0:
       sum+=i 
print(sum)

print("===============================================")

#Countdown by Fours
for x in range(2018, 0, -4):
         print(x)

print("===============================================")

#Flexible Counter
lowNum=2
highNum=10
mult=3
for i in range(lowNum,highNum):
    if i % mult == 0:
        print(i)
