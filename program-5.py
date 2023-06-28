# In an array, Count Pairs with given sum

def Pairs_Count(arr, n, sum):
	count = 0 
	for i in range(0, n):
		for j in range(i + 1, n):
			if arr[i] + arr[j] == sum:
				count += 1
	return count
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print(" the Count of pairs is",Pairs_Count(arr, n, sum))

