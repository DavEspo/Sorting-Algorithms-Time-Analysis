import time
from numpy import random

def QuickSort(A,l,r):
    if l<r:
        s=HoarePartition(A,l,r)
        QuickSort(A,l,s-1)
        QuickSort(A,s+1,r)

def HoarePartition(A,l,r):
    p=A[l]
    i=l
    j=r+1
    value=True
    while value==True:
        i=i+1
        while A[i]<p and i<r:
            i=i+1
        j=j-1
        while A[j]>p:
            j=j-1
        A[i],A[j]=A[j],A[i]
        if i>=j:
            value=False
    A[i],A[j]=A[j],A[i]
    A[l],A[j]=A[j],A[l]
    return j


Array1 = random.randint(1000, size = 100)
Array2 = random.randint(1000, size = 200)
Array3 = random.randint(1000, size = 300)
Array4 = random.randint(1000, size = 400)
Array5 = random.randint(1000, size = 500)
Array6 = random.randint(1000, size = 1000)

# Random List
RandomQSTimeArray = [0]*6

start_time = time.time()
QuickSort(Array1,0,len(Array1)-1)
end_time = time.time()
RandomQSTimeArray[0] = end_time - start_time

start_time = time.time()
QuickSort(Array2,0,len(Array2)-1)
end_time = time.time()
RandomQSTimeArray[1] = end_time - start_time

start_time = time.time()
QuickSort(Array3,0,len(Array3)-1)
end_time = time.time()
RandomQSTimeArray[2] = end_time - start_time

start_time = time.time()
QuickSort(Array4,0,len(Array4)-1)
end_time = time.time()
RandomQSTimeArray[3] = end_time - start_time

start_time = time.time()
QuickSort(Array5,0,len(Array5)-1)
end_time = time.time()
RandomQSTimeArray[4] = end_time - start_time

start_time = time.time()
QuickSort(Array6,0,len(Array6)-1)
end_time = time.time()
RandomQSTimeArray[5] = end_time - start_time


# Sorted List
SortedQSTimeArray = [0] * 6

start_time = time.time()
QuickSort(Array1,0,len(Array1)-1)
end_time = time.time()
SortedQSTimeArray[0] = end_time - start_time

start_time = time.time()
QuickSort(Array2,0,len(Array2)-1)
end_time = time.time()
SortedQSTimeArray[1] = end_time - start_time

start_time = time.time()
QuickSort(Array3,0,len(Array3)-1)
end_time = time.time()
SortedQSTimeArray[2] = end_time - start_time

start_time = time.time()
QuickSort(Array4,0,len(Array4)-1)
end_time = time.time()
SortedQSTimeArray[3] = end_time - start_time

start_time = time.time()
QuickSort(Array5,0,len(Array5)-1)
end_time = time.time()
SortedQSTimeArray[4] = end_time - start_time

start_time = time.time()
QuickSort(Array6,0,len(Array6)-1)
end_time = time.time()
SortedQSTimeArray[5] = end_time - start_time


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
ReverseQSTimeArray = [0] * 6

start_time = time.time()
QuickSort(List1,0,len(List1)-1)
end_time = time.time()
ReverseQSTimeArray[0] = end_time - start_time

start_time = time.time()
QuickSort(List2,0,len(List2)-1)
end_time = time.time()
ReverseQSTimeArray[1] = end_time - start_time

start_time = time.time()
QuickSort(List3,0,len(List3)-1)
end_time = time.time()
ReverseQSTimeArray[2] = end_time - start_time

start_time = time.time()
QuickSort(List4,0,len(List4)-1)
end_time = time.time()
ReverseQSTimeArray[3] = end_time - start_time

start_time = time.time()
QuickSort(List5,0,len(List5)-1)
end_time = time.time()
ReverseQSTimeArray[4] = end_time - start_time

start_time = time.time()
QuickSort(List6,0,len(List6)-1)
end_time = time.time()
ReverseQSTimeArray[5] = end_time - start_time


if __name__=='__main__':
    print("Random Times:", RandomQSTimeArray)
    print("Sorted Times:", SortedQSTimeArray)
    print("Reverse Times:", ReverseQSTimeArray)