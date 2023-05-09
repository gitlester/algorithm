def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in arr[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
print(quick_sort([10, 5, 2, 3]))


    
