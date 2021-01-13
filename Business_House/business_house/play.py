from cell_factory import CellFactory
from roll_dice import RollDice
from player import Player


def play_business_house(board):

	GAME_ROUND = 10
	players = [ Player(i, 1000) for i in range(2)]
	#print(players)
	
	#Play GAME_ROUND
	for _round in range(0, GAME_ROUND):
		for player in players:
			player.player_pos = (player.player_pos + RollDice.roll(2,12)) % len(board)
			perform_action(player, board)
	
	#print("Player 0: %s, Player 1: %s"%(players[0].money, players[1].money))
	
	for cell in board:
		if cell.cell_type == "H" and cell.hotel_owner:
			if cell.hotel_owner.id_ == 0:
				players[0].money += cell.hotel_worth
			if cell.hotel_owner.id_ == 1:
				players[1].money += cell.hotel_worth
	#print("Player 0: %s, Player 1: %s"%(players[0].money, players[1].money))
	
	players.sort(key=lambda x:x.money, reverse=True)
	for player in players:
		print("Player: %s Money: %s"%(player.id_, player.money))


def perform_action(player, board):
	
	if board[player.player_pos].cell_type == "E":
		pass
	elif board[player.player_pos].cell_type == "T":
		board[player.player_pos].get_treasure(player)
	elif board[player.player_pos].cell_type == "J":
		board[player.player_pos].apply_penalty(player)
	elif board[player.player_pos].cell_type == "H":
		board[player.player_pos].deduct_rent(player)
		

if __name__ == "__main__":

	import pdb 
	board_cells = "E,E,J,H,E,T,J,T,E,E,H,J,T,H,E,E,J,H,E,T,J,T,E,E,H,J,T,H,J,E,E,J,H,E,T,J,T,E,E,H,J,T,E,H,E".split(',')
	
	# Create Board
	board = CellFactory.get_cell(board_cells)
	
	# Play Game as per rules.
	play_business_house(board)
	









