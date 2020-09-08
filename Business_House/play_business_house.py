from player import Player
from business_house_board import BusinessHouseBoard
from roll_dice import RollDice


class PlayBusinessHouse():
	
	def __init__(self, player_ids):
		'''
		init player ids
		'''
		self._players = [Player(player_id) for player_id in range(player_ids)]
		self._businessHouseBoard = BusinessHouseBoard()
		self._board_map = self._businessHouseBoard.get_board()
		self._roll_dice = RollDice(2,12)
		self._max_roll_per_player = 10
		
	def play(self):
		'''
		play as per rules.
		'''
		
		for roll_count in range(self._max_roll_per_player):
			for _player in self._players:
				# roll the dice
				_roll = self._roll_dice.roll()
				
				# update player pos
				_player = self._update_player_pos(_player, _roll)
				
				# update board and player status
				_player = self._updateBoardAndPlayerStatus(_player)
				
				# Update current player obj
				self._players[self._players.index(_player)] =  _player
				
	def _hotel_bought_by_player(self):
		'''
		'''

		hotel_owned_dict = { _player.id:0 for _player in self._players}

		for cell in self._board_map:
			if cell['cell_type'] == 'H':
				if cell['owner']:
					hotel_owned_dict[cell['owner']] += 1
						
		return 	hotel_owned_dict

	def get_winner(self):
		'''
		get Total worth
		'''
		import pdb
		pdb.set_trace()
		worth = dict()
		for player in self._players:
			worth[player.id] = player.get_money()
		
		#get Owned Hotels:
		_owned_hotels = self._hotel_bought_by_player()
		for _player, _owned_hotel_count in _owned_hotels.items():
			worth[_player] = worth[_player] + (_owned_hotel_count * 200 )
		
		#Print total worth of players in Decreasing Order.
		_worth_decreasing_ord = sorted(worth, key=worth.get, reverse=True)
		for _player in  _worth_decreasing_ord:
			print(str(_player)+" has total worth: "+str(worth[_player]))
		
	def _update_player_pos(self, player, roll):
		'''
		update player pos.
		'''
		_pos = (player.get_curr_pos() + roll) % len(self._board_map)
		player.update_pos(_pos)
		return player

	def _updateBoardAndPlayerStatus(self, player):
		'''
		update board and player status
		'''
		_pos = player.get_curr_pos()
		_cell = self._board_map[_pos]
		player, cell = self._update_player_status(_cell, player)
		self._board_map[_pos] = cell
		
		return player

	def _update_player_status(self, cell, player):
		'''
		update player status and cell info
		'''
		if cell['cell_type'] == 'E':
			pass
		elif cell['cell_type'] == 'J':
			player.debit_money(cell['fine'])
		elif cell['cell_type'] == 'T':
			player.credit_money(cell['treasure_val'])
		elif cell['cell_type'] == 'H':
			if cell['owner'] == None and player.get_money() >= cell['worth']:
				cell['owner'] = player.id
				player.debit_money(cell['worth'])
			elif player.id == cell['owner']:
				pass
			else:
				player.debit_money(cell['rent'])
				
		return player, cell

