# Replace first iteration of an element from an array by another integer.
list1 = [5, 10, 15, 20, 25, 50, 20]

index = 0
for element in list1:
    if(element == 20):
        break
    else:
        index+=1
          
list1[index] = 200
print(list1)
# Result
# [5, 10, 15, 200, 25, 50, 20]