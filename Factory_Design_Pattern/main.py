from TableFactory import TableFactory

if __name__ == "__main__":
	
	table = TableFactory.get_table("SmallTable")
	print(table.get_table())
	
	table = TableFactory.get_table("MediumTable")
	print(table.get_table())

	table = TableFactory.get_table("LargeTable")
	print(table.get_table())

