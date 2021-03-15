import visualizer


def bubbleSort(array, name):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            visualizer.updateDisplay(array=array, algorithmName=name, swap1=array[j], swap2=array[j + 1])
    visualizer.updateDisplay(array=array, algorithmName=name, status="Done!")


def selectionSort(array, name):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
            visualizer.updateDisplay(array=array, algorithmName=name, swap1=array[min_index], swap2=array[j])
        array[i], array[min_index] = array[min_index], array[i]
    visualizer.updateDisplay(array=array, algorithmName=name, status="Done!")


def insertionSort(array, name):
    for i in range(1, len(array)):
        cursor = array[i]
        j = i - 1
        while j >= 0 and array[j] > cursor:
            array[j + 1] = array[j]
            j -= 1
            visualizer.updateDisplay(array=array, algorithmName=name, swap1=array[j], swap2=array[i])
        array[j + 1] = cursor
    visualizer.updateDisplay(array=array, algorithmName=name, status="Done!")
