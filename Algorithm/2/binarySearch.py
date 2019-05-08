# no recursion
def binarySearch(arr, target):
    n = len(arr)
    l, r = 0, n-1
    while l <= r:
        mid = int(l + (r-l)/2)
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

# recursion
def binarySearch_recursion(arr, l, r, target):
    if l > r:
        return False
    mid = int(l + (r - l) / 2)
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch_recursion(arr, l, mid-1, target)
    else:
        return binarySearch_recursion(arr, mid+1, r, target)

arr = [1, 3, 5, 7, 9]
print(binarySearch_recursion(arr, 0, 4, 6))
