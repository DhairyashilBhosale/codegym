
# SingleTon Using __new__ and __init__ 
class A(object):

	__instance = None

	def __new__(cls):
		if cls.__instance is None:
			print("creating new instance")
			cls.__instance =  super(A, cls).__new__(cls)
			cls.__instance.__initialized = False 
		return cls.__instance

	def __init__(self):
		if self.__initialized: return 
		self.__initialized = True
		print("Init is called")

# SingleTon Using Decorator 
def singleton(cls):
	
	instance = {}
	def getinstance():
		if cls not in instance:
			instance[cls] = cls()
		return  instance[cls]
	return getinstance

@singleton
class SingleTon():

	def __init__(self):
		print("init is called . . . ")
		
if __name__ == "__main__":
	
	print("# using __init__ and __new__")
	a = A()
	b = A()
	print(a == b)
	
	print("\n# using Decorator ")
	s = SingleTon()
	l = SingleTon()
	print(s == l)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
