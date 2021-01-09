from table_types import SmallTable, MediumTable, LargeTable

class TableFactory():

	@staticmethod	
	def get_table_details(table_type):
		"""
		"""
		if table_type == "SmallTable":
			return SmallTable()
		elif table_type == "MediumTable":
			return MediumTable()
		elif table_type == "LargeTable":
			return LargeTable()
		else:
			raise AssertionError("Table Type Not available "+table_type)

