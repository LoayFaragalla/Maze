def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

# Driver Code

n = int(input("Please enter a length of array:  "))
arr = []
for i in range (n):
    print(f'Current Numbers List {arr}')
    number = int(input(f"Please enter a number {i} to be added: "))
    arr.insert(i, number)
    print(f'Updated List {arr}')


type_sort = int(input('Choose sort type: \nChoose 1: Insertion Sort\nChoose 2: Merge Sort\nChoose Number: '))

print("Given array is", end="\n")
printList(arr)


def insertionSort (arr):
    for j in range(len(arr)):
        key = arr[j]
        i = j - 1 
        while i >= 0 and arr[i] > key :
            arr[i+1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


if type_sort == 1:
    insertionSort(arr)
    print("Sorted array by insertion sort is: ", end="\n")
    printList(arr)
elif type_sort == 2:
    mergeSort(arr)
    print("Sorted array by merge sort is: ", end="\n")
    printList(arr)
else :
    print ('ERROR')
