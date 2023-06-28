# Find the Kth largest and Kth smallest number in an array

def kth_Smallest(arr, N, K):
	arr.sort()
	return arr[K-1]

if __name__ == '__main__':
	arr = [12, 3, 5, 7, 19]
	N = len(arr)
	K = 2

	print("K'th smallest element is as follows ",kth_Smallest(arr, N, K))