import time
from numpy import random

def MergeSort(A):
    n=len(A)
    if n>1:
        B=[0]*int((n/2))
        C=[0]*((n)-int(n/2))
        for i in range(int((n/2))):
            B[i]=A[i]
        for i in range(n-int(n/2)):
            C[i]=A[i+int(n/2)]
        MergeSort(B)
        MergeSort(C)
        Merge(B,C,A)

def Merge(B,C,A):
    i=0
    j=0
    k=0
    p=len(B)
    q=len(C)
    while i<p and j<q:
        if B[i]<=C[j]:
            A[k]=B[i]
            i+=1
        else:
            A[k]=C[j]
            j+=1
        k+=1
    if i==p:
        for l in range(q-j):
            A[k+l]=C[j+l]
    else:
        for l in range(p-i):
            A[k+l]=B[i+l]


Array1 = random.randint(1000, size = 100)
Array2 = random.randint(1000, size = 200)
Array3 = random.randint(1000, size = 300)
Array4 = random.randint(1000, size = 400)
Array5 = random.randint(1000, size = 500)
Array6 = random.randint(1000, size = 1000)

# Random List
RandomMSTimeArray = [0]*6

start_time = time.time()
MergeSort(Array1)
end_time = time.time()
RandomMSTimeArray[0] = end_time - start_time

start_time = time.time()
MergeSort(Array2)
end_time = time.time()
RandomMSTimeArray[1] = end_time - start_time

start_time = time.time()
MergeSort(Array3)
end_time = time.time()
RandomMSTimeArray[2] = end_time - start_time

start_time = time.time()
MergeSort(Array4)
end_time = time.time()
RandomMSTimeArray[3] = end_time - start_time

start_time = time.time()
MergeSort(Array5)
end_time = time.time()
RandomMSTimeArray[4] = end_time - start_time

start_time = time.time()
MergeSort(Array6)
end_time = time.time()
RandomMSTimeArray[5] = end_time - start_time


# Sorted List
SortedMSTimeArray = [0] * 6

start_time = time.time()
MergeSort(Array1)
end_time = time.time()
SortedMSTimeArray[0] = end_time - start_time

start_time = time.time()
MergeSort(Array2)
end_time = time.time()
SortedMSTimeArray[1] = end_time - start_time

start_time = time.time()
MergeSort(Array3)
end_time = time.time()
SortedMSTimeArray[2] = end_time - start_time

start_time = time.time()
MergeSort(Array4)
end_time = time.time()
SortedMSTimeArray[3] = end_time - start_time

start_time = time.time()
MergeSort(Array5)
end_time = time.time()
SortedMSTimeArray[4] = end_time - start_time

start_time = time.time()
MergeSort(Array6)
end_time = time.time()
SortedMSTimeArray[5] = end_time - start_time


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
ReverseMSTimeArray = [0] * 6

start_time = time.time()
MergeSort(List1)
end_time = time.time()
ReverseMSTimeArray[0] = end_time - start_time

start_time = time.time()
MergeSort(List2)
end_time = time.time()
ReverseMSTimeArray[1] = end_time - start_time

start_time = time.time()
MergeSort(List3)
end_time = time.time()
ReverseMSTimeArray[2] = end_time - start_time

start_time = time.time()
MergeSort(List4)
end_time = time.time()
ReverseMSTimeArray[3] = end_time - start_time

start_time = time.time()
MergeSort(List5)
end_time = time.time()
ReverseMSTimeArray[4] = end_time - start_time

start_time = time.time()
MergeSort(List6)
end_time = time.time()
ReverseMSTimeArray[5] = end_time - start_time


if __name__=='__main__':
    print("Random Times:", RandomMSTimeArray)
    print("Sorted Times:", SortedMSTimeArray)
    print("Reverse Times:", ReverseMSTimeArray)