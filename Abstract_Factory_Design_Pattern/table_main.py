from table_factory import TableFactory

if __name__ == "__main__":
	
	table = TableFactory.get_table_details("SmallTable")
	print(table.get_info())
	
	table = TableFactory.get_table_details("MediumTable")
	print(table.get_info())

	table = TableFactory.get_table_details("LargeTable")
	print(table.get_info())

