from ICell import ICell


class HotelCell(ICell):

	def __init__(self, **kwargs):
		self.cell_type = kwargs['cell_type']
		self.hotel_worth = kwargs['hotel_worth']
		self.hotel_rent = kwargs['hotel_rent']
		self.hotel_owner = None

	def get_hotel_owner(self):
		return self.hotel_owner
	
	def deduct_rent(self, player):
		if self.hotel_owner == None:
			#Buy a Hotel
			#print("Buying Hotel By Player: %s"%(player.id_))
			self.__buy_hotel(player)
		elif self.hotel_owner and self.hotel_owner.id_ != player.id_:
			# Pay Rent 
			#print("Paying Hotel Rent by Player: %s"%(player.id_))
			player.money -= self.hotel_rent
			self.hotel_owner.money += self.hotel_rent
		elif self.hotel_owner.id_ == player.id_:
			# Do nothing if already aquired
			#print("Owned Hotel")
			pass
		else:
			AssertionError("never reach here !")

	def __buy_hotel(self, player):
		if self.hotel_owner == None and player.money >= self.hotel_worth:
			player.money -= self.hotel_worth
			self.hotel_owner = player
	
class EmptyCell(ICell):
	
	def __init__(self, **kwargs):
		self.cell_type = kwargs['cell_type']

class JailCell(ICell):

	def __init__(self, **kwargs):
		self.cell_type = kwargs['cell_type']	
		self.penalty = kwargs['penalty']

	def apply_penalty(self, player):
		if player.money:
			player.money -= self.penalty
	 
class TreasureCell(ICell):

	def __init__(self, **kwargs):
		self.cell_type = kwargs['cell_type']
		self.treasure_val = kwargs['treasure_val']

	def get_treasure(self, player):
		player.money += self.treasure_val
	


	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

