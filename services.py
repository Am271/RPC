class service:
	#This class provides all the functions that the RPC server will present to the client for calling
    def add(self, x, y):
        '''(number, number) -> number --Returns a sum of two numbers'''
        x = float(x); y = float(y)
        return str(x + y)
	#The above function is a sample for other functions to be defined later
