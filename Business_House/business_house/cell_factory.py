from cells import HotelCell, EmptyCell, JailCell, TreasureCell


class CellFactory():

	@staticmethod
	def get_cell(cell_list):
	
		board = list()
		for cell in cell_list:
			if cell == "E":
				board.append(EmptyCell(cell_type='E'))
			elif cell == "J":
				board.append(JailCell(cell_type='J', penalty=150))
			elif cell == "T":
				board.append(TreasureCell(cell_type='T', treasure_val=200))
			elif cell == "H":
				board.append(HotelCell(cell_type='H', hotel_worth=200, hotel_rent=50))
			else:
				raise AssertionError("Cell Type Not Found !")

		return board

