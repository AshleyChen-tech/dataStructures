# 无序列表的顺序搜索
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


# 有序列表的顺序搜索
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False 
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found


# 有序列表的二分搜索
def binarySearch(alist, item):
    left = 0
    right = len(alist) - 1
    found = False

    while left < right and not found:
        mid = (left + right) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                left = mid - 1
            else:
                right = mid + 1
    return found


# 二分搜索递归
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binarySearch(alist[:mid], item)
            else:
                return binarySearch(alist[mid+1:], item)
    


