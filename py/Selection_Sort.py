import time
from numpy import random

def SelectionSort(A):
    for i in range(len(A) - 1):
        Min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[Min]:
                Min = j
        A[i], A[Min] = A[Min], A[i]

Array1 = random.randint(1000, size = 100)
Array2 = random.randint(1000, size = 200)
Array3 = random.randint(1000, size = 300)
Array4 = random.randint(1000, size = 400)
Array5 = random.randint(1000, size = 500)
Array6 = random.randint(1000, size = 1000)

# Random List
RandomSSTimeArray = [0]*6

start_time = time.time()
SelectionSort(Array1)
end_time = time.time()
RandomSSTimeArray[0] = end_time - start_time

start_time = time.time()
SelectionSort(Array2)
end_time = time.time()
RandomSSTimeArray[1] = end_time - start_time

start_time = time.time()
SelectionSort(Array3)
end_time = time.time()
RandomSSTimeArray[2] = end_time - start_time

start_time = time.time()
SelectionSort(Array4)
end_time = time.time()
RandomSSTimeArray[3] = end_time - start_time

start_time = time.time()
SelectionSort(Array5)
end_time = time.time()
RandomSSTimeArray[4] = end_time - start_time

start_time = time.time()
SelectionSort(Array6)
end_time = time.time()
RandomSSTimeArray[5] = end_time - start_time


# Sorted List
SortedSSTimeArray = [0] * 6

start_time = time.time()
SelectionSort(Array1)
end_time = time.time()
SortedSSTimeArray[0] = end_time - start_time

start_time = time.time()
SelectionSort(Array2)
end_time = time.time()
SortedSSTimeArray[1] = end_time - start_time

start_time = time.time()
SelectionSort(Array3)
end_time = time.time()
SortedSSTimeArray[2] = end_time - start_time

start_time = time.time()
SelectionSort(Array4)
end_time = time.time()
SortedSSTimeArray[3] = end_time - start_time

start_time = time.time()
SelectionSort(Array5)
end_time = time.time()
SortedSSTimeArray[4] = end_time - start_time

start_time = time.time()
SelectionSort(Array6)
end_time = time.time()
SortedSSTimeArray[5] = end_time - start_time


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
ReverseSSTimeArray = [0] * 6

start_time = time.time()
SelectionSort(List1)
end_time = time.time()
ReverseSSTimeArray[0] = end_time - start_time

start_time = time.time()
SelectionSort(List2)
end_time = time.time()
ReverseSSTimeArray[1] = end_time - start_time

start_time = time.time()
SelectionSort(List3)
end_time = time.time()
ReverseSSTimeArray[2] = end_time - start_time

start_time = time.time()
SelectionSort(List4)
end_time = time.time()
ReverseSSTimeArray[3] = end_time - start_time

start_time = time.time()
SelectionSort(List5)
end_time = time.time()
ReverseSSTimeArray[4] = end_time - start_time

start_time = time.time()
SelectionSort(List6)
end_time = time.time()
ReverseSSTimeArray[5] = end_time - start_time


if __name__=='__main__':
    print("Random Times:", RandomSSTimeArray)
    print("Sorted Times:", SortedSSTimeArray)
    print("Reverse Times:", ReverseSSTimeArray)