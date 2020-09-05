class Player():

	def __init__(self, id):
		'''
		Init player id with default money and pos [position]
		'''
		self.id = id
		self._money = 1000
		self._current_pos = 0
		
	def get_money(self):
		'''
		return money
		'''
		return self._money
		
	def get_curr_pos(self):
		'''
		return curr position
		'''
		return self._current_pos
		
	def credit_money(self, money):
		'''
		update money
		'''
		self._money += money

	def debit_money(self, money):
		'''
		update money
		'''
		self._money -= money
	
	def update_pos(self, pos):
		'''
		update current position
		'''
		self._current_pos = pos

