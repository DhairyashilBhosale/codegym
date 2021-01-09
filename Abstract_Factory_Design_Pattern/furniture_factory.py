from IFurniture import IFurniture 
from chair_factory import ChairFactory
from table_factory import TableFactory

class FurnitureFactory(IFurniture):

	@staticmethod
	def get_furniture(furniture_type):
		"""
		"""
		if furniture_type in ["LargeChair", "SmallChair", "MediumChair"]:
			return ChairFactory().get_chair_details(furniture_type)
		elif furniture_type in ["LargeTable", "SmallTable", "MediumTable"]:
			return TableFactory().get_table_details(furniture_type)
		else:
			raise AssertionError("Furniture Not Found: "+furniture_type)

