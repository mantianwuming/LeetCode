def selectionSort(alist):
    n = len(alist)
    for i in range(n):
        minIndex = alist[i]
        for j in range(i+1, n):
            if alist[j] < alist[minIndex]:
                minIndex = j
        alist[i], alist[minIndex] = alist[minIndex], alist[i]
    return alist
l = [1, 3, 4, 2, 5, 6, 1]
l = selectionSort(l)
print(l)
