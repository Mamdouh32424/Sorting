import time
from random import randint
def BubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def SelectionSort(arr):
	n = len(arr)
	
	for i in range(1, n - 1):
		for j in range(i, n):
			if arr[j] < arr[i - 1]:
				arr[i - 1], arr[j] = arr[j], arr[i - 1]

def InsertionSort(arr):
    pass

def MergeSort(arr, l, r):
	if l >= r:
		return
	
	mid = (l + r) // 2
	MergeSort(arr, l, mid)
	MergeSort(arr, mid + 1, r)
	res = []
	pointer_l, pointer_r = l, mid + 1
	while pointer_l <= mid and pointer_r <= r:
		if arr[pointer_l] < arr[pointer_r]:
			res.append(arr[pointer_l])
			pointer_l += 1
		else:
			res.append(arr[pointer_r])
			pointer_r += 1
	
	while pointer_l <= mid:
		res.append(arr[pointer_l])
		pointer_l += 1
	
	while pointer_r <= r:
		res.append(arr[pointer_r])
		pointer_r += 1
	
	for i in range(r - l + 1):
		arr[l + i] = res[i]

def QuickSort(arr):
    n = len(arr)
    if n <= 1:
    	return arr
    
    left_part, right_part = [], []
    pivot, count = arr[randint(0, n - 1)], 0
    
    for i in range(n):
    	if arr[i] < pivot:
    		left_part.append(arr[i])
    	elif arr[i] > pivot:
    		right_part.append(arr[i])
    	else:
    		count += 1
    
    return QuickSort(left_part) + [pivot] * count + QuickSort(right_part)

if __name__ == "__main__": # for testing
    list = [64, 34, 25, 12, 22, 11, 90]
    
    # BubbleSort
    cpy = list[:]
    startTime = time.time()
    BubbleSort(cpy)
    bubble_delta_time = (time.time() - startTime) * 1000
    
    # SelectionSort:
    cpy = list[:]
    startTime = time.time()
    SelectionSort(cpy)
    select_delta_time = (time.time() - startTime) * 1000
    
    # MergeSort:
    cpy = list[:]
    startTime = time.time()
    MergeSort(cpy, 0, len(cpy) - 1)
    merge_delta_time = (time.time() - startTime) * 1000
    
    # QuickSort:
    cpy = list[:]
    startTime = time.time()
    cpy = QuickSort(cpy)
    quick_delta_time = (time.time() - startTime) * 1000
    
    print("Time taken for Bubble Sort:", bubble_delta_time, "milliseconds")
    print("Time taken for Selection Sort:", select_delta_time, "milliseconds")
    print("Time taken for Merge Sort:", merge_delta_time, "milliseconds")
    print("Time taken for Quick Sort:", quick_delta_time, "milliseconds")
    
    
