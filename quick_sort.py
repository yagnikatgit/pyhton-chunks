def quick_sort(lst):
    if len(lst) <= 1:
        return(lst)
    pivot= lst[(len(lst) // 2)]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + quick_sort(middle) + quick_sort(right)

print(quick_sort([5,4,3,8,7,1,2,6]))