def binary_search(list,target):
    if not list:
        return -1
    
    low = 0
    high = len(list) - 1
    mid = (low + high) // 2

    if list[mid] == target:
        return target
    elif list[mid] > target:
        return binary_search(list[:mid],target)
    else:
        return binary_search(list[mid+1:],target)
    

print(binary_search([6,7,8,9,10],8))
print(binary_search([6,7,8,9,10],6))
