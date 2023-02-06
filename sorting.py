import math
import random
# import matplotlib.pyplot as plt


import math
import random
# import matplotlib.pyplot as plt


def insertionSort(arr):
    comp = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            comp += 1
            arr[j + 1] = arr[j]
            j -= 1
        if (j >= 0):
            comp += 1
        arr[j + 1] = key
    return comp


def selectionSort(arr):	
    comp = 0
    for ind in range(len(arr)):
        min_index = ind
        for j in range(ind + 1, len(arr)):
            comp += 1
            if arr[j] < arr[min_index]:
                min_index = j
        (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])
    return comp




def bubbleSort(arr):
    comp = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            comp += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return comp


def merge(arr, l, m, r):
	comp = 0
	n1 = m - l + 1
	n2 = r - m
	L = [0] * (n1)
	R = [0] * (n2)
	for i in range(0, n1):
		L[i] = arr[l + i]
	for j in range(0, n2):
		R[j] = arr[m + 1 + j]
	i = 0	 
	j = 0	 
	k = l	 
	while i < n1 and j < n2:
		comp += 1
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
	return comp


def mergeSort(arr, l, r):
	if l < r:
		m = l+(r-l)//2
		a = mergeSort(arr, l, m)
		b = mergeSort(arr, m+1, r)
		c = merge(arr, l, m, r)
		return a + b + c
	else:
		return 0



def partition(arr, low, high):
	comp = 0
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		comp += 1
		if arr[j] <= pivot:
			i = i + 1
			(arr[i], arr[j]) = (arr[j], arr[i])
	(arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
	return (i + 1, comp)

def quickSort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)
		a = quickSort(arr, low, pi[0] - 1)
		b = quickSort(arr, pi[0] + 1, high)
		return pi[1] + a + b
	else:
		return 0

def getNum(v, index_lst, parent_call = False) :
	n = len(v)
	# index = 0
	index = random.randint(0, n - 1)
	# while parent_call:
	# 	index = random.randint(0, n - 1)
	# 	if not(index in index_lst):
	# 		index_lst.append(index)
	# 		break
	# 	else:
	# 		continue
	num = v[index]
	v[index], v[n - 1] = v[n - 1], v[index]
	v.pop()
	return num
def generateRandom(n) :
	lst = []
	v = [0] * n
	for i in range(n) :
		v[i] = i + 1
	while (len(v)) :
		# if len(v) == n:
		# 	print("With")
		# 	lst.append(getNum(v, index_lst, True))
		# else:
		# 	print("Non")
			lst.append(getNum(v, index_lst, False))
	return lst

index_lst = []
is_lst = []
ss_lst = []
bs_lst = []
ms_lst = []
qs_lst = []
x = range(40000, 450001, 1000)
for n in x:
	index_lst = []
	c = 0
	is_avg = 0
	ss_avg = 0
	bs_avg = 0
	ms_avg = 0
	qs_avg = 0
	total_permutations = int(math.log2(n)) // 2
	for i in range(total_permutations):
		a = generateRandom(n)
		# b = a.copy()
		# c = a.copy()
		d = a.copy()
		e = a.copy()
		is_avg += insertionSort(a)
		# ss_avg += selectionSort(b)
		# bs_avg += bubbleSort(c)
		ms_avg += mergeSort(d, 0, len(d) - 1)
		qs_avg += quickSort(e, 0, len(e) - 1)
	is_lst.append(is_avg/total_permutations)
	# ss_lst.append(ss_avg/total_permutations)
	# bs_lst.append(bs_avg/total_permutations)
	ms_lst.append(ms_avg/total_permutations)
	qs_lst.append(qs_avg/total_permutations)
	print(is_lst)
	# print(ss_lst)
	# print(bs_lst)
	print(ms_lst)
	print(qs_lst)
	

# plt.plot(x, is_lst, label="Insertion Sort")
# plt.plot(x, ss_lst, label="Selection Sort")
# plt.plot(x, bs_lst, label="Bubble Sort")
# plt.plot(x, ms_lst, label="Merge Sort")
# plt.plot(x, qs_lst, label="Quick Sort")
# plt.legend()
# plt.show()
