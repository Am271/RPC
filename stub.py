import services

# Create an object of class services
obj = services.service()

# Collects all the methods bound to the object 'obj', excluding dunder methods
method_list = [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith("__")]
print(method_list)

for i in method_list:
	# getattr(object, function_name_as_str) returns the address of the method to be able to call it
	# It returns a reference to the method in the object
	print(getattr(obj, i)(10, 2))
	# The above statement obtains the reference to all the methods in the methodlist
	# and calls them passing 10 & 2 as parameters

# print(obj.add.__doc__)