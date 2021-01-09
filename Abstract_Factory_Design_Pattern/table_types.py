from ITable import ITable

class SmallTable(ITable):

	def __init__(self):
		"""
		"""
		self.height = 10
		self.width = 10
		self.length = 10 
		
	def get_info(self):
		"""
		"""
		return {"Height": self.height, "Width": self.width, "Length": self.length}

class LargeTable(ITable):

	def __init__(self):
		"""
		"""
		self.height = 20
		self.width = 20 
		self.length = 20 
		
	def get_info(self):
		"""
		"""
		return {"Height": self.height, "Width": self.width, "Length": self.length}

class MediumTable(ITable):

	def __init__(self):
		"""
		"""
		self.height = 50 
		self.width = 50
		self.length = 50
		
	def get_info(self):
		"""
		"""
		return {"Height": self.height, "Width": self.width, "Length": self.length}










		
