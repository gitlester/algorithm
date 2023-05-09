def rescursion_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + rescursion_sum(arr[1:])

print(rescursion_sum([1,3,5,7,9]))
