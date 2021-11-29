class service:
	#This class provides all the functions that the RPC server will present to the client for calling
	def add(self, x, y):
		'''(number, number) -> number --Returns a sum of two numbers'''
		x = float(x); y = float(y)
		return str(x + y)
	#The above function is a sample for other functions to be defined later
	def sub(self, x, y):
		'''(number, number) -> number --Returns the difference of two numbers'''
		x = float(x); y = float(y)
		return str(x - y)

	def mult(self, x, y):
		'''(number, number) -> number --Returns the product of two numbers'''
		x = float(x); y = float(y)
		return str(x * y)

	def div(self, x, y):
		'''(dividend, divisor) -> number --Divides two numbers and returns the quotient'''
		x = float(x); y = float(y)
		if y == 0.0:
			return "Division by zero not possible!"
		return str(x / y)

	def gcd(self, x, y):
		'''(number, number) -> number --Returns the GCD(Greatest Common Divisor) of two numbers'''
		x = int(x); y = int(y); gcd_ = 1
		for i in range(1, min(x, y)+1):
			if((x % i == 0) and (y % i == 0)):
				gcd_ = i
		return gcd_