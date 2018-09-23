import abc

"""
Factory Class
"""
class factory():
	__instance=None

	def __init__(self,product):
		if product=='product1':
			self.__instance=concreteProduct1()
		elif product=='product2':
			self.__instance=concreteProduct2()
		else:
			self.__instance=concreteProduct_default()

	def getInstance(self):		
		return self.__instance

"""
Abstract Product Class
"""
class product():
	__metaclass__=abc.ABCMeta

	@abc.abstractmethod
	def interface(self):
		pass

"""
Concrete Product Class (extend product)
"""
class concreteProduct_default(product):
	def interface(self):
		print "This is default product"

class concreteProduct1(product):
	def interface(self):
		print "This is concrete Product 1"
		

class concreteProduct2(product):
	def interface(self):
		print "This is concrete Product 2"

def main():
	factory_test=factory("").getInstance().interface()

if __name__=="__main__":
	main()

