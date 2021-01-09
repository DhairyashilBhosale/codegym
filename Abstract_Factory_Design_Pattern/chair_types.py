from IChair import IChair

class SmallChair(IChair):

	def __init__(self):
		"""
		"""
		self.color = "red"
		self.size = "small"
		self.cup_holder = False

	def get_info(self):
		return {"Color": self.color, "Size":self.size, "Cup_holder": self.cup_holder}
	

class MediumChair(IChair):

	def __init__(self):
		"""
		"""
		self.color = "blue"
		self.size = "medium"
		self.cup_holder = True

	def get_info(self):
		return {"Color": self.color, "Size":self.size, "Cup_holder": self.cup_holder}
	

class LargeChair(IChair):

	def __init__(self):
		"""
		"""
		self.color = "black"
		self.size = "large"
		self.cup_holder = True

	def get_info(self):
		return {"Color": self.color, "Size":self.size, "Cup_holder": self.cup_holder}
	


















