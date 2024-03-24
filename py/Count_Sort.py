import time
from numpy import random

def CountSort(Array):
    Max=max(Array)+1
    CountArray=[0]*Max
    for i in Array:
        CountArray[i]=CountArray[i]+1
    for i in range(1,len(CountArray)):
        CountArray[i]=CountArray[i-1]+CountArray[i]
        Result=[0]*len(Array)
    for i in range(len(Array)):
        Result[CountArray[Array[len(Array)-i-1]]-1]=Array[len(Array)-i-1]
        CountArray[Array[len(Array)-i-1]]=CountArray[Array[len(Array)-i-1]]-1
    for i in range(len(Result)):
        Array[i]=Result[i]

Array1 = random.randint(1000, size = 100)
Array2 = random.randint(1000, size = 200)
Array3 = random.randint(1000, size = 300)
Array4 = random.randint(1000, size = 400)
Array5 = random.randint(1000, size = 500)
Array6 = random.randint(1000, size = 1000)


# Random List
RandomCSTimeArray = [0]*6

start_time = time.time()
CountSort(Array1)
end_time = time.time()
RandomCSTimeArray[0] = end_time - start_time

start_time = time.time()
CountSort(Array2)
end_time = time.time()
RandomCSTimeArray[1] = end_time - start_time

start_time = time.time()
CountSort(Array3)
end_time = time.time()
RandomCSTimeArray[2] = end_time - start_time

start_time = time.time()
CountSort(Array4)
end_time = time.time()
RandomCSTimeArray[3] = end_time - start_time

start_time = time.time()
CountSort(Array5)
end_time = time.time()
RandomCSTimeArray[4] = end_time - start_time

start_time = time.time()
CountSort(Array6)
end_time = time.time()
RandomCSTimeArray[5] = end_time - start_time


# Sorted List
SortedCSTimeArray = [0] * 6

start_time = time.time()
CountSort(Array1)
end_time = time.time()
SortedCSTimeArray[0] = end_time - start_time

start_time = time.time()
CountSort(Array2)
end_time = time.time()
SortedCSTimeArray[1] = end_time - start_time

start_time = time.time()
CountSort(Array3)
end_time = time.time()
SortedCSTimeArray[2] = end_time - start_time

start_time = time.time()
CountSort(Array4)
end_time = time.time()
SortedCSTimeArray[3] = end_time - start_time

start_time = time.time()
CountSort(Array5)
end_time = time.time()
SortedCSTimeArray[4] = end_time - start_time

start_time = time.time()
CountSort(Array6)
end_time = time.time()
SortedCSTimeArray[5] = end_time - start_time


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
ReverseCSTimeArray = [0] * 6

start_time = time.time()
CountSort(List1)
end_time = time.time()
ReverseCSTimeArray[0] = end_time - start_time

start_time = time.time()
CountSort(List2)
end_time = time.time()
ReverseCSTimeArray[1] = end_time - start_time

start_time = time.time()
CountSort(List3)
end_time = time.time()
ReverseCSTimeArray[2] = end_time - start_time

start_time = time.time()
CountSort(List4)
end_time = time.time()
ReverseCSTimeArray[3] = end_time - start_time

start_time = time.time()
CountSort(List5)
end_time = time.time()
ReverseCSTimeArray[4] = end_time - start_time

start_time = time.time()
CountSort(List6)
end_time = time.time()
ReverseCSTimeArray[5] = end_time - start_time


if __name__=='__main__':
    print("Random Times:", RandomCSTimeArray)
    print("Sorted Times:", SortedCSTimeArray)
    print("Reverse Times:", ReverseCSTimeArray)