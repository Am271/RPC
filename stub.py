import services
import json


# Collects all the methods bound to the object, excluding dunder methods
method_list = []


# Funtion to return a JSON formatted string containing all available services and their description
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

def check(req):
	if not isinstance(req.get('call'), int): # Checks if 'call' is a key in the request JSON, also checks if the value is an integer
		return False
	if not len(req.keys()) - 1 == req.get('call'): # Checks if the number of functions declared equals the number of keys - 1 in the JSON
		return False
	return True


# Function to process requests other than broadcasts from the server
def process(req):
	call_dict = dict()
	try:
		call_dict = eval(req)
	except:
		return "Malformed JSON received, send request again"
    
    if not isinstance(req.get('call'), int): # Checks if 'call' is a key in the request JSON, also checks if the value is an integer
        return "Malformed JSON received, send request again"
    
    if not len(req.keys()) - 1 == req.get('call'): # Checks if the number of functions declared equals the number of keys - 1 in the JSON
        return "Number of functions declared is not equal to the number of function calls in the JSON"
    
	else:
		# Create an object to perform function calls
		obj = services.service()
		res_json = { 'results' : 0, 'errors' : [] } # Result in JSON to be returned
		success = 0 # Keeps count of number of functions that were successfully executed
		# Perform function calls
		for k, v in call_dict:
			if k == 'call': # If the key is 'call', the loop continues to the next key
				continue
			try:
				res = getattr(obj, k)(*v) # Attempts to obtain reference to function and perform the function call
				res_json[k] = res # Stores the result in JSON
				res_json['results'] += 1 # Counts the number of successful results
			except TypeError:
				res_json['errors'].append(k) # Stores the function names with incorrect list of parameters
        return res_json