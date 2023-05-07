'''
输入一个有序的元素列表。如果要查找的元素包含在列表中，二分查找返回其位置；否则返回 None
'''
def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = (low + high)//2
        some = list[middle]
        if some == item:
            return middle
        if some > item:
            high = middle - 1
        else:
            low = middle + 1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list,3))
