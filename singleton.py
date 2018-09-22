class singleton:
	__instance=None 
	__quantity=None

	def __init__(self,quantity):
		if singleton.__instance!=None:
			print "instance is already created"
		else:
			singleton.__instance=self
			singleton.__quantity=quantity
		#	print singleton.__quantity
	
	@staticmethod
	def getInstance(): 
		""" Static access method. """
		if singleton.__instance == None:
			singleton(1000)
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

s=singleton(1000)
print s.getQuantity() 
singleton(5000)
s.addQuantity(1515)
s.delQuantity(421)
print s.getQuantity()

