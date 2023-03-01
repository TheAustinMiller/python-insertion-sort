def insertionSort(list):
  for i in range(1, len(list)):
    key = list[i]
    prevIndex = i - 1
    while prevIndex >= 0 and key < list[prevIndex] :
      list[prevIndex + 1] = list[prevIndex]
      prevIndex -= 1
    list[prevIndex + 1] = key
 
list = [-13, -17, -8, -14, -1, -20]
insertionSort(list)
print(list)
