from abc import ABC, abstractmethod

class ITable(ABC):

	@abstractmethod
	def __init__(self):
		"""
		"""
		self.height = None
		self.width = None
		self.length = None
		
	@abstractmethod
	def get_table(self):
		"""
		"""

