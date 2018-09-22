class singleton:
	__instance=None

	@staticmethod
	def getInstance():
		if singleton.__instance==None:
			singleton()
		return singleton.__instance
	def __init__(self):
		if singleton.__instance!=None:
			raise Exception("Singleton Class")
		else:
			singleton.__instance=self

s=singleton()
print s
s = singleton.getInstance()
print s

s = singleton.getInstance()
print s
