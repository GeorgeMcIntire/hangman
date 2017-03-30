
board = [["-"]*3 for i in range(3)]

def printboard(board):
	for i in board:
		print "".join(i)
		


for turn in range(9):
	
	player1row = int(raw_input("Player 1 Row:"))
	player1col = int(raw_input("Player 1 Column:"))
	
	if type(player1row) != int or type(player1col) != int:
		break
	if player1row > 2 or player1col > 2:
		break
	if player1row < 0 or player1col < 0:
		break
	
	if board[player1row][player1col] == "B":
		board[player1row][player1col] = "O"
		print printboard(board)
	
	elif board[player1row][player1col] != "B":
		print "Already guessed"
		break

	
	player2row = int(raw_input("Player 2 Row:"))
	player2col = int(raw_input("Player 2 Column:"))
	
				
			
	if type(player2row) != type(int) or type(player2col) != type(int):
		break
	if player2row > 2 or player2col > 2:
		break
	if player2row < 0 or player2col < 0:
		break
	
		
	if board[player2row][player2col] == "B":
		board[player2row][player2col] = "X"
		print printboard(board)

	elif board[player2row][player2col] != "B":
		print "Already guessed"
		break
	
	if board[0][0] == board[0][1] == board[0][2] == "O":
		print "Player 1 win2!"
		print printboard(board)
		break
	if board[1][0] == board[1][1] == board[1][2] == "O":
		print "Player 1 win2!"
		print printboard(board)
		break
	if board[2][0] == board[2][1] == board[2][2] == "O":
		print "Player 1 win2!"
		print printboard(board)
		break
	if board[0][0] == board[1][0] == board[2][0] == "O":
		print "Player 1 win2!"
		print printboard(board)
		break1
	if board[0][1] == board[1][1] == board[2][1] == "O":
		print "Player 1 win2!"
		print printboard(board)
		break
	if board[0][2] == board[1][2] == board[2][2] == "O":
		print "Player 1 win2!"
		print printboard(board)
		break	
	if board[0][0] == board[1][1] == board[2][2] == "O":
		print "Player 1 win2!"
		print printboard(board)
		break
	if board[2][0] == board[1][1] == board[0][2] == "O":
		print "Player 1 win2!"
		print printboard(board)
		break

	if board[0][0] == board[0][1] == board[0][2] == "X":
		print "Player 2 wins!"
		print printboard(board)
		break
	if board[1][0] == board[1][1] == board[1][2] == "X":
		print "Player 2 wins!"
		print printboard(board)
		break
	if board[2][0] == board[2][1] == board[2][2] == "X":
		print "Player 2 wins!"
		print printboard(board)
		break
	if board[0][0] == board[1][0] == board[2][0] == "X":
		print "Player 2 wins!"
		print printboard(board)
		break
	if board[0][1] == board[1][1] == board[2][1] == "X":
		print "Player 2 wins!"
		print printboard(board)
		break
	if board[0][2] == board[1][2] == board[2][2] == "X":
		print "Player 2 wins!"
		print printboard(board)
		break	
	if board[0][0] == board[1][1] == board[2][2] == "X":
		print "Player 2 wins!"
		print printboard(board)
		break
	if board[2][0] == board[1][1] == board[0][2] == "X":
		print "Player 2 wins!"
		print printboard(board)
		break
	
	print "Turn", turn + 1
	
	if turn == 8:
		print "Nobody wins!!!"