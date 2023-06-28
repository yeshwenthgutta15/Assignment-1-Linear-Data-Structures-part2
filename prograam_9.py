# Evaluate a postfix expression using stack

class evalpostfix:
	def __init__(self):
		self.stack = []
		self.top = -1

	def pop(self):
		if self.top == -1:
			return
		else:
			self.top -= 1
			return self.stack.pop()

	def push(self, i):
		self.top += 1
		self.stack.append(i)

	def centralfunc(self, ab):
		for i in ab:
			try:
				self.push(int(i))
			except ValueError:
				val1 = self.pop()
				val2 = self.pop()
				if i == '/':
					self.push(val2 / val1)
				else:
					switcher = {'+': val2 + val1, '-': val2 -
								val1, '*': val2 * val1, '^': val2**val1}
					self.push(switcher.get(i))
		return int(self.pop())
if __name__ == '__main__':
	str = '100 200 + 2 / 5 * 7 +'
	strconv = str.split(' ')
	obj = evalpostfix()
	print(obj.centralfunc(strconv))