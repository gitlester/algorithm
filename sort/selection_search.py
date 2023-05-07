'''
将数组元素按照顺序找出
'''
def findSmallest(list):
    smallest_idx = 0
    smallest = list[0]
    for i in range(1,len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_idx = i
    return smallest_idx

def selectionSort(list):
    newList = []
    for i in range(len(list)):
        smallest = findSmallest(list)
        newList.append(list.pop(smallest))
    return newList

print(selectionSort([5,3,6,2,10]))
