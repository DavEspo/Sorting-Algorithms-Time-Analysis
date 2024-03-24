from Bubble_Sort import SortedBSTimeArray,RandomBSTimeArray,ReverseBSTimeArray
from Selection_Sort import SortedSSTimeArray,RandomSSTimeArray,ReverseSSTimeArray
from Insertion_Sort import SortedISTimeArray,RandomISTimeArray,ReverseISTimeArray
from Merge_Sort import SortedMSTimeArray,RandomMSTimeArray,ReverseMSTimeArray
from Quick_Sort import SortedQSTimeArray,RandomQSTimeArray,ReverseQSTimeArray
from Count_Sort import SortedCSTimeArray,RandomCSTimeArray,ReverseCSTimeArray
from Heap_Sort import SortedHSTimeArray,RandomHSTimeArray,ReverseHSTimeArray
import matplotlib.pyplot as plt


# Sorted Data
x1_sorted = [100, 200, 300, 400, 500, 1000]
y1_sorted = SortedBSTimeArray

x2_sorted = [100, 200, 300, 400, 500, 1000]
y2_sorted = SortedSSTimeArray

x3_sorted = [100, 200, 300, 400, 500, 1000]
y3_sorted = SortedISTimeArray

x4_sorted = [100, 200, 300, 400, 500, 1000]
y4_sorted = SortedMSTimeArray

x5_sorted = [100, 200, 300, 400, 500, 1000]
y5_sorted = SortedQSTimeArray

x6_sorted = [100, 200, 300, 400, 500, 1000]
y6_sorted = SortedCSTimeArray

x7_sorted = [100, 200, 300, 400, 500, 1000]
y7_sorted = SortedHSTimeArray

plt.plot(x1_sorted, y1_sorted, label = "Bubble Sort")
plt.plot(x2_sorted, y2_sorted, label = "Selection Sort")
plt.plot(x3_sorted, y3_sorted, label = "Insertion Sort")
plt.plot(x4_sorted, y4_sorted, label = "Merge Sort")
plt.plot(x5_sorted, y5_sorted, label = "Quick Sort")
plt.plot(x6_sorted, y6_sorted, label = "Count Sort")
plt.plot(x7_sorted, y7_sorted, label = "Heap Sort")

plt.xlabel("Input Size")
plt.ylabel("Time Taken")
plt.title("Order of Growth - Sorted Data")

plt.legend()

plt.show()


# Random Data
x1_random = [100, 200, 300, 400, 500, 1000]
y1_random = RandomBSTimeArray

x2_random = [100, 200, 300, 400, 500, 1000]
y2_random = RandomSSTimeArray

x3_random = [100, 200, 300, 400, 500, 1000]
y3_random = RandomISTimeArray

x4_random = [100, 200, 300, 400, 500, 1000]
y4_random = RandomMSTimeArray

x5_random = [100, 200, 300, 400, 500, 1000]
y5_random = RandomQSTimeArray

x6_random = [100, 200, 300, 400, 500, 1000]
y6_random = RandomCSTimeArray

x7_random = [100, 200, 300, 400, 500, 1000]
y7_random = RandomHSTimeArray

plt.plot(x1_random, y1_random, label = "Bubble Sort")
plt.plot(x2_random, y2_random, label = "Selection Sort")
plt.plot(x3_random, y3_random, label = "Insertion Sort")
plt.plot(x4_random, y4_random, label = "Merge Sort")
plt.plot(x5_random, y5_random, label = "Quick Sort")
plt.plot(x6_random, y6_random, label = "Count Sort")
plt.plot(x7_random, y7_random, label = "Heap Sort")

plt.xlabel("Input Size")
plt.ylabel("Time Taken")
plt.title("Order of Growth - Random Data")

plt.legend()

plt.show()


# Reverse Data
x1_reverse = [100, 200, 300, 400, 500, 1000]
y1_reverse = ReverseBSTimeArray

x2_reverse = [100, 200, 300, 400, 500, 1000]
y2_reverse = ReverseSSTimeArray

x3_reverse = [100, 200, 300, 400, 500, 1000]
y3_reverse = ReverseISTimeArray

x4_reverse = [100, 200, 300, 400, 500, 1000]
y4_reverse = ReverseMSTimeArray

x5_reverse = [100, 200, 300, 400, 500, 1000]
y5_reverse = ReverseQSTimeArray

x6_reverse = [100, 200, 300, 400, 500, 1000]
y6_reverse = ReverseCSTimeArray

x7_reverse = [100, 200, 300, 400, 500, 1000]
y7_reverse = ReverseHSTimeArray

plt.plot(x1_reverse, y1_reverse, label = "Bubble Sort")
plt.plot(x2_reverse, y2_reverse, label = "Selection Sort")
plt.plot(x3_reverse, y3_reverse, label = "Insertion Sort")
plt.plot(x4_reverse, y4_reverse, label = "Merge Sort")
plt.plot(x5_reverse, y5_reverse, label = "Quick Sort")
plt.plot(x6_reverse, y6_reverse, label = "Count Sort")
plt.plot(x7_reverse, y7_reverse, label = "Heap Sort")

plt.xlabel("Input Size")
plt.ylabel("Time Taken")
plt.title("Order of Growth - Reverse Data")

plt.legend()

plt.show()