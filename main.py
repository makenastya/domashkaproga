arr = list(map(int, input().split()))
def qsort(arr):
    if arr:
        l = []
        for x in arr:
            if x < arr[0]:
                l.append(x)
        l = qsort(l)
        m = []
        for x in arr:
            if x == arr[0]:
                m.append(x)
        r = []
        for x in arr:
            if x > arr[0]:
                r.append(x)
        r = qsort(r)
        return (l + m + r)
    return []
print(qsort(arr))