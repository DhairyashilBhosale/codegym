from TableFactory import TableFactory

if __name__ == "__main__":
	
	table = TableFactory.get_table("SmallTable")
	table.get_table()
	
	table = TableFactory.get_table("MediumTable")
	table.get_table()

	table = TableFactory.get_table("LargeTable")
	table.get_table()

