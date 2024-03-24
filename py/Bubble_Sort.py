import time
from numpy import random

def BubbleSort(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - 1 - i):
            if A[j + 1] < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]

Array1 = random.randint(1000, size = 100)
Array2 = random.randint(1000, size = 200)
Array3 = random.randint(1000, size = 300)
Array4 = random.randint(1000, size = 400)
Array5 = random.randint(1000, size = 500)
Array6 = random.randint(1000, size = 1000)


# Random List
RandomBSTimeArray = [0]*6

start_time = time.time()
BubbleSort(Array1)
end_time = time.time()
RandomBSTimeArray[0] = end_time - start_time

start_time = time.time()
BubbleSort(Array2)
end_time = time.time()
RandomBSTimeArray[1] = end_time - start_time

start_time = time.time()
BubbleSort(Array3)
end_time = time.time()
RandomBSTimeArray[2] = end_time - start_time

start_time = time.time()
BubbleSort(Array4)
end_time = time.time()
RandomBSTimeArray[3] = end_time - start_time

start_time = time.time()
BubbleSort(Array5)
end_time = time.time()
RandomBSTimeArray[4] = end_time - start_time

start_time = time.time()
BubbleSort(Array6)
end_time = time.time()
RandomBSTimeArray[5] = end_time - start_time


# Sorted List
SortedBSTimeArray = [0] * 6

start_time = time.time()
BubbleSort(Array1)
end_time = time.time()
SortedBSTimeArray[0] = end_time - start_time

start_time = time.time()
BubbleSort(Array2)
end_time = time.time()
SortedBSTimeArray[1] = end_time - start_time

start_time = time.time()
BubbleSort(Array3)
end_time = time.time()
SortedBSTimeArray[2] = end_time - start_time

start_time = time.time()
BubbleSort(Array4)
end_time = time.time()
SortedBSTimeArray[3] = end_time - start_time

start_time = time.time()
BubbleSort(Array5)
end_time = time.time()
SortedBSTimeArray[4] = end_time - start_time

start_time = time.time()
BubbleSort(Array6)
end_time = time.time()
SortedBSTimeArray[5] = end_time - start_time


List1 = list(Array1)
List2 = list(Array2)
List3 = list(Array3)
List4 = list(Array4)
List5 = list(Array5)
List6 = list(Array6)

List1.reverse()
List2.reverse()
List3.reverse()
List4.reverse()
List5.reverse()
List6.reverse()

# Reversed List
ReverseBSTimeArray = [0] * 6

start_time = time.time()
BubbleSort(List1)
end_time = time.time()
ReverseBSTimeArray[0] = end_time - start_time

start_time = time.time()
BubbleSort(List2)
end_time = time.time()
ReverseBSTimeArray[1] = end_time - start_time

start_time = time.time()
BubbleSort(List3)
end_time = time.time()
ReverseBSTimeArray[2] = end_time - start_time

start_time = time.time()
BubbleSort(List4)
end_time = time.time()
ReverseBSTimeArray[3] = end_time - start_time

start_time = time.time()
BubbleSort(List5)
end_time = time.time()
ReverseBSTimeArray[4] = end_time - start_time

start_time = time.time()
BubbleSort(List6)
end_time = time.time()
ReverseBSTimeArray[5] = end_time - start_time


if __name__=='__main__':
    print("Random Times:", RandomBSTimeArray)
    print("Sorted Times:", SortedBSTimeArray)
    print("Reverse Times:", ReverseBSTimeArray)