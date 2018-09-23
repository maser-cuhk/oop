class singleton:
	#Some private stuff including the instance
	__instance=None
	__quantity=None
	__default=1000

	#class constructor with input argument
	def __init__(self,quantity=__default):
		#check if instance existed?
		if singleton.__instance!=None:
			print "instance is already created"
		else:
			#assign instance to the current instance to class__instance
			singleton.__instance=self
			singleton.__quantity=quantity
	
	@staticmethod
	def getInstance(): 
		""" Static access method. """
		if singleton.__instance == None:
			singleton(singleton.__default)
		return singleton.__instance 
	
	@staticmethod
	def getQuantity():
		return singleton.__quantity
	
	@staticmethod 	
	def addQuantity(quantity):
		singleton.__quantity+=quantity
	
	@staticmethod 
	def delQuantity(quantity):
		singleton.__quantity-=quantity


s=singleton()
print s.getQuantity() 
s.addQuantity(123)
print s.getQuantity()

