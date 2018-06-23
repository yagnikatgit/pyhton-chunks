''' 

Quick sort using list comprehension. 

'''

def quick_sort(lst):
    # Checks length of list.
    if len(lst) <= 1:
        return(lst)
    
    # Sets pivot in the middle
    pivot= lst[(len(lst) // 2)]
    
    # Sort numbers less than pivot.
    left = [x for x in lst if x < pivot]
    
    middle = [x for x in lst if x == pivot]
    
    # Sort numbers greater than pivot.
    right = [x for x in lst if x > pivot]
    
    # Merge three lists.
    return quick_sort(left) + quick_sort(middle) + quick_sort(right)

print(quick_sort([5,4,3,8,7,1,2,6]))
