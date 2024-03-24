import time
from numpy import random

def InsertionSort(A):
    for i in range(len(A)):
        n = A[i]
        j = i - 1
        while j >= 0 and A[j] > n:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = n

Array1 = random.randint(1000, size = 100)
Array2 = random.randint(1000, size = 200)
Array3 = random.randint(1000, size = 300)
Array4 = random.randint(1000, size = 400)
Array5 = random.randint(1000, size = 500)
Array6 = random.randint(1000, size = 1000)

# Random List
RandomISTimeArray = [0]*6

start_time = time.time()
InsertionSort(Array1)
end_time = time.time()
RandomISTimeArray[0] = end_time - start_time

start_time = time.time()
InsertionSort(Array2)
end_time = time.time()
RandomISTimeArray[1] = end_time - start_time

start_time = time.time()
InsertionSort(Array3)
end_time = time.time()
RandomISTimeArray[2] = end_time - start_time

start_time = time.time()
InsertionSort(Array4)
end_time = time.time()
RandomISTimeArray[3] = end_time - start_time

start_time = time.time()
InsertionSort(Array5)
end_time = time.time()
RandomISTimeArray[4] = end_time - start_time

start_time = time.time()
InsertionSort(Array6)
end_time = time.time()
RandomISTimeArray[5] = end_time - start_time


# Sorted List
SortedISTimeArray = [0] * 6

start_time = time.time()
InsertionSort(Array1)
end_time = time.time()
SortedISTimeArray[0] = end_time - start_time

start_time = time.time()
InsertionSort(Array2)
end_time = time.time()
SortedISTimeArray[1] = end_time - start_time

start_time = time.time()
InsertionSort(Array3)
end_time = time.time()
SortedISTimeArray[2] = end_time - start_time

start_time = time.time()
InsertionSort(Array4)
end_time = time.time()
SortedISTimeArray[3] = end_time - start_time

start_time = time.time()
InsertionSort(Array5)
end_time = time.time()
SortedISTimeArray[4] = end_time - start_time

start_time = time.time()
InsertionSort(Array6)
end_time = time.time()
SortedISTimeArray[5] = end_time - start_time


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
ReverseISTimeArray = [0] * 6

start_time = time.time()
InsertionSort(List1)
end_time = time.time()
ReverseISTimeArray[0] = end_time - start_time

start_time = time.time()
InsertionSort(List2)
end_time = time.time()
ReverseISTimeArray[1] = end_time - start_time

start_time = time.time()
InsertionSort(List3)
end_time = time.time()
ReverseISTimeArray[2] = end_time - start_time

start_time = time.time()
InsertionSort(List4)
end_time = time.time()
ReverseISTimeArray[3] = end_time - start_time

start_time = time.time()
InsertionSort(List5)
end_time = time.time()
ReverseISTimeArray[4] = end_time - start_time

start_time = time.time()
InsertionSort(List6)
end_time = time.time()
ReverseISTimeArray[5] = end_time - start_time


if __name__=='__main__':
    print("Random Times:", RandomISTimeArray)
    print("Sorted Times:", SortedISTimeArray)
    print("Reverse Times:", ReverseISTimeArray)