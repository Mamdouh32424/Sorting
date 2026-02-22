import time


def BubbleSort(arr):
    startTime = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    endTime = time.time()
    return (endTime - startTime) * 1000

def SelectionSort(arr):
    pass

def InsertionSort(arr):
    pass


if __name__ == "__main__": # for testing
    list = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", list)
    delta_time = BubbleSort(list)
    print("Time taken for Bubble Sort:", delta_time, "milliseconds")
    print("Sorted array:", list)