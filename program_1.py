# Delete the elements in an linked list whose sum is equal to zero

class List_Node:
	def __init__(self, val):
		self.val = val
		self.next = None
def get_Node(data):
	temp = List_Node(data)
	temp.next = None
	return temp
def printList(head):
	while (head.next):
		print(head.val, end=' -> ')
		head = head.next
	print(head.val, end='')
def removeZeroSum(head, K):
	root = List_Node(0)
	root.next = head
	umap = dict()

	umap[0] = root
	sum = 0
	while (head != None):
		sum += head.val
		if ((sum - K) in umap):

			prev = umap[sum - K]
			start = prev
			aux = sum
			sum = sum - K
			while (prev != head):
				prev = prev.next
				aux += prev.val
				if (prev != head):
					umap.remove(aux)
			start.next = head.next
		else:
			umap[sum] = head
		head = head.next
	return root.next
if __name__ == '__main__':
	head = get_Node(1)
	head.next = get_Node(2)
	head.next.next = get_Node(-3)
	head.next.next.next = get_Node(3)
	head.next.next.next.next = get_Node(1)
	K = 5
	head = removeZeroSum(head, K)
	if(head != None):
		printList(head)