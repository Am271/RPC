class service:
	def add(x, y):
		'''(number, number) -> number\nReturns a sum of two numbers'''
		return x + y

obj = service()

method_list = [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith("__")]
print(method_list)
print(obj.add.__doc__)