from play_business_house import PlayBusinessHouse






if __name__ == "__main__":
	_num_players = 3
	playBusinessHouse = PlayBusinessHouse(_num_players)
	
	#Play Game.
	playBusinessHouse.play()
	
	#Get Result.
	playBusinessHouse.get_winner()
