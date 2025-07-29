import logging

# 設定 logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def quick_sort(arr):
    """
    快速排序演算法。
    """
    logging.debug(f"開始快速排序，輸入陣列: {arr}")
    if len(arr) <= 1:
        logging.debug(f"陣列長度小於等於 1，直接返回: {arr}")
        return arr
    
    try:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        
        logging.debug(f"左陣列: {left}, 右陣列: {right}")
        
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)
        
        logging.debug(f"排序後的左陣列: {sorted_left}, 排序後的右陣列: {sorted_right}")
        
        return sorted_left + [pivot] + sorted_right
    
except Exception as e:
    logging.error(f"快速排序過程中發生錯誤: {e}")
    return None  # 或拋出異常，取決於需求

# 範例使用
data = [5, 3, 8, 4, 2, 7, 1, 10]
sorted_data = quick_sort(data)
if sorted_data is not None:
    print("排序後結果：", sorted_data)
else:
    print("排序失敗")