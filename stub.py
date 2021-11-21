import services
import json


# Collects all the methods bound to the object, excluding dunder methods
method_list = []

def broadcast():
	# Create an object of class services
	obj = services.service()

	# Populate the list of methods available to call
	method_list = [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith("__")]
	# getattr(object, function_name_as_str) returns the address of the method to be able to call it

	# Prepare a JSON string to send to client
	json_string = "{"
	
	for i in method_list:

		# Add method names and method descriptions to JSON
		json_string += '\n"' + i + '" : "' + getattr(obj, i).__doc__ + '",'

	# Format the JSON string by removing the last ',' and adding the closing '}'
	json_string = json_string[:-1] + "\n}"

	# Return the json formatted string to server
	return json_string
