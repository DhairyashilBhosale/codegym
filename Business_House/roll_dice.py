from random import randint

class RollDice():

	def __init__(self, min, max):
		'''
		'''
		self._min = min
		self._max = max
	
	def roll(self):
		'''
		return random number between range
		'''
		return randint(self._min, self._max)
		
