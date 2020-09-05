from player import Player
from business_house_board import BusinessHouseBoard
from roll_dice import RollDice


class PlayBusinessHouse():
	
	def __init__(self, player_ids):
		'''
		init player ids
		'''
		self._players = [Player(player_id) for player_id in player_ids]
		self._businessHouseBoard = BusinessHouseBoard()
		self._roll_dice = RollDice(2,12)
		self._max_roll_per_player = 10
		
	def play(self):
		'''
		play as per rules.
		'''
		
		for roll_count in self._max_roll_per_player:
			for _player in self._players:
			
			
