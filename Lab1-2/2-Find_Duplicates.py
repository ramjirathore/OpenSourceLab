def findDuplicates(arr):
	list_size = len(arr)
	duplicates = []
	for i in range(list_size):
		for j in range(i + 1, list_size):
			if (arr[i] == arr[j] and arr[i] not in duplicates):
				duplicates.append(arr[i])
	return duplicates

input = [12, 11, 2, 1, 2, 12, 5, 6, 8, 5]
print(findDuplicates(input))