import time
from numpy import random

def Heapify(arr,N,i):
    largest = i
    l=2*i+1
    r=2*i+2
    if l<N and arr[largest]<arr[l]:
        largest=l
    if r<N and arr[largest]<arr[r]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        Heapify(arr,N,largest)
 
def HeapSort(arr):
    N=len(arr)
    for i in range(0,N//2):
        Heapify(arr,N,N//2-1-i)
    for i in range(0,N):
        arr[N-1-i],arr[0]=arr[0],arr[N-1-i]
        Heapify(arr,N-1-i,0)


Array1 = random.randint(1000, size = 100)
Array2 = random.randint(1000, size = 200)
Array3 = random.randint(1000, size = 300)
Array4 = random.randint(1000, size = 400)
Array5 = random.randint(1000, size = 500)
Array6 = random.randint(1000, size = 1000)

# Random List
RandomHSTimeArray = [0]*6

start_time = time.time()
HeapSort(Array1)
end_time = time.time()
RandomHSTimeArray[0] = end_time - start_time

start_time = time.time()
HeapSort(Array2)
end_time = time.time()
RandomHSTimeArray[1] = end_time - start_time

start_time = time.time()
HeapSort(Array3)
end_time = time.time()
RandomHSTimeArray[2] = end_time - start_time

start_time = time.time()
HeapSort(Array4)
end_time = time.time()
RandomHSTimeArray[3] = end_time - start_time

start_time = time.time()
HeapSort(Array5)
end_time = time.time()
RandomHSTimeArray[4] = end_time - start_time

start_time = time.time()
HeapSort(Array6)
end_time = time.time()
RandomHSTimeArray[5] = end_time - start_time


# Sorted List
SortedHSTimeArray = [0] * 6

start_time = time.time()
HeapSort(Array1)
end_time = time.time()
SortedHSTimeArray[0] = end_time - start_time

start_time = time.time()
HeapSort(Array2)
end_time = time.time()
SortedHSTimeArray[1] = end_time - start_time

start_time = time.time()
HeapSort(Array3)
end_time = time.time()
SortedHSTimeArray[2] = end_time - start_time

start_time = time.time()
HeapSort(Array4)
end_time = time.time()
SortedHSTimeArray[3] = end_time - start_time

start_time = time.time()
HeapSort(Array5)
end_time = time.time()
SortedHSTimeArray[4] = end_time - start_time

start_time = time.time()
HeapSort(Array6)
end_time = time.time()
SortedHSTimeArray[5] = end_time - start_time


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
ReverseHSTimeArray = [0] * 6

start_time = time.time()
HeapSort(List1)
end_time = time.time()
ReverseHSTimeArray[0] = end_time - start_time

start_time = time.time()
HeapSort(List2)
end_time = time.time()
ReverseHSTimeArray[1] = end_time - start_time

start_time = time.time()
HeapSort(List3)
end_time = time.time()
ReverseHSTimeArray[2] = end_time - start_time

start_time = time.time()
HeapSort(List4)
end_time = time.time()
ReverseHSTimeArray[3] = end_time - start_time

start_time = time.time()
HeapSort(List5)
end_time = time.time()
ReverseHSTimeArray[4] = end_time - start_time

start_time = time.time()
HeapSort(List6)
end_time = time.time()
ReverseHSTimeArray[5] = end_time - start_time


if __name__=='__main__':
    print("Random Times:", RandomHSTimeArray)
    print("Sorted Times:", SortedHSTimeArray)
    print("Reverse Times:", ReverseHSTimeArray)