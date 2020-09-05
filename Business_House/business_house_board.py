class BusinessHouseBoard():
	
	def __init__(self):
		'''
		BusinessHouseBoard is based on python lists.
		init board cell and pos and create board with all required properties.
		TODO: implement dynamic creation of board.
		'''
		self._cell_pos_type = ['E','E','J','H','E','T','J','T','E','E','H','J','T','H','E','E','J','H','E','T','J','T','E','E','H','J','T','H','J','E','E','J','H','E','T','J','T','E','E','H','J','T','E','H','E']
		self._board_cell_info = dict()
		self._board_map = list()
		self._create_board()
		
	def _create_board(self):
		'''
		create board dict with all attributes.
		update  self._board_map list with all required attrributes
		'''
		for cell_type in self._cell_pos_type:
			if cell_type == 'E':
				self._board_map.append({'cell_type':'E', 'players_in_cell':[]})
			elif cell_type == 'J':
				self._board_map.append({'cell_type':'J', 'fine':150, 'players_in_cell':[]})
			elif cell_type == 'T':
				self._board_map.append({'cell_type':'T', 'treasure_val':200, 'players_in_cell':[]})
			elif cell_type == 'H':
				self._board_map.append({'cell_type':'H', 'owner':None, 'rent':50, 'worth':200, 'players_in_cell':[]})

	def get_board(self):
		'''
		return board cell
		'''
		return self._board_map
		
	def get_cell_info(self, cell_index):
		'''
		return cell info in dict form
		'''
		if not cell_index > len(self._board_map):
			return self._board_map[cell_index]
		else:
			return 1
		
