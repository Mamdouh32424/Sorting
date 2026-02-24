import Sorting
import matplotlib.pyplot as plt
import random


def generateRandomArray(size):
    list = []
    for i in range(size):
        list.append(random.randint(1, 100000))
    return list


def main():
    sizes = [100, 500, 1000, 5000, 10000, 25000]# 50000, 100000]
    bubble_times = []
    selection_times = []
    insertion_times = []

    for size in sizes:
        arr = generateRandomArray(size)
        print(f"Sorting array of size {size}...")
        bubble_times.append(Sorting.BubbleSort(arr.copy()))
        selection_times.append(Sorting.SelectionSort(arr.copy()))
        insertion_times.append(Sorting.InsertionSort(arr.copy()))

    print("Done")
    plt.plot(sizes, bubble_times, label='Bubble Sort',marker='o')
    plt.plot(sizes, selection_times, label='Selection Sort',marker='o')
    plt.plot(sizes, insertion_times, label='Insertion Sort',marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Time (ms)')
    plt.legend()
    plt.show()




if __name__ == "__main__":
    main()