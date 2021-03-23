listtest = [100,44,12,200,88,3,56,133,1,38]
  
for i in range(len(listtest)):
    min = i
    for j in range(i+1, len(listtest)):
        if listtest[min] > listtest[j]:
            min = j
      
    listtest[i], listtest[min] = listtest[min], listtest[i]
  

for i in range(len(listtest)):
    print("%d" %listtest[i]), 