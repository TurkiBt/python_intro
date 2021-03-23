def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >=0 and key < list[j] :
                list[j+1] = list[j]
                j -= 1
        list[j+1] = key
  
  
listtest = [100,44,12,200,88,3,56,133,1,38]
insertionSort(listtest)

for i in range(len(listtest)):
    print ("%d" %listtest[i])