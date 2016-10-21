def bounds(l, val):
    """
    in a sorted list l identifies low, high, such that
    l[low] < val < l[high] if there is no val in the list and
    l[low]=l[high]=val if there is
    """
    low = 0; high = len(l)-1
    while low +1 < high:
        mid = (low + high)/2
        if l[mid]==val:
            low = mid
            high = mid
        if l[mid] > val:
            high = mid
        elif l[mid] < val:
            low = mid
    return low,high

def closest_idx(l,val):
    """
    finds an element closest to given val by absolute value in
    a non-empty list
    """
    low, high = bounds(l, val)
    return min(map(lambda c:(c, abs(l[c]-val)),[low,high]),key = lambda x:x[1])[0]

def closest(l,val):
    return l[closest_idx(l,val)]

def interpolate(l, val):
    low, high = bounds(l, val)
