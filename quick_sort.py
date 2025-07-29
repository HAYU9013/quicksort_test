def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# 範例使用
data = [5, 3, 8, 4, 2, 7, 1, 10]
sorted_data = quick_sort(data)
print("排序後結果：", sorted_data)
