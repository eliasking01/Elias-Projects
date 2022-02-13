
def game():
	grid_start = "| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |"
	grid = "|   |   |   |\n|   |   |   |\n|   |   |   |"

	player_1 = input("Player #1 name: ")
	player_2 = input("Player #2 name: ")

	start_of_game = True
	player_1_turn = True
	player_1_won = False
	until_tie = 0
	tie = False

	while True:
		if start_of_game:
			print(grid_start)
			start_of_game = False
		else:
			print(grid)

		if player_1_turn:
			player_1_turn = False
			print(player_1 + "'s turn.")
			x_turn = input("where do you want to place your X: ")
			if x_turn in "123456789" and len(x_turn) == 1:
				for num in range(len(grid_start)):
					if grid_start[num] == x_turn:
						if grid[num] == "X":
							print("You already placed an 'X' there.")
							player_1_turn = True
						elif grid[num] == "O":
							print(player_2 + " already placed an 'O' there.")
							player_1_turn = True
						else:
							until_tie += 1
							grid = grid[0:num] + "X" + grid[num + 1:]
							# grid.replace(grid[num], "X") DOES NOT WORK

			else:
				print(player_1 + ", Please type a valid response.")
				player_1_turn = True
		else:
			player_1_turn = True
			print(player_2 + "'s turn.")
			o_turn = input("where do you want to place your O: ")
			if o_turn in "123456789" and len(o_turn) == 1:
				for num in range(len(grid_start)):
					if grid_start[num] == o_turn:
						if grid[num] == "O":
							print("You already placed an 'O' there.")
							player_1_turn = False
						elif grid[num] == "X":
							print(player_1 + " already placed an 'X' there.")
							player_1_turn = False
						else:
							until_tie += 1
							grid = grid[0:num] + "O" + grid[num + 1:]
							# grid.replace(grid[num], "X") DOES NOT WORK
			else:
				print(player_2 + ", Please type a valid response.")
				player_1_turn = False

		# X columns
		if "X" in grid[2] and "X" in grid[16] and "X" in grid[30]:
			player_1_won = True
			break
		elif "X" in grid[6] and "X" in grid[20] and "X" in grid[34]:
			player_1_won = True
			break
		elif "X" in grid[10] and "X" in grid[24] and "X" in grid[38]:
			player_1_won = True
			break
		# X rows
		elif "X" in grid[2] and "X" in grid[6] and "X" in grid[10]:
			player_1_won = True
			break
		elif "X" in grid[16] and "X" in grid[20] and "X" in grid[24]:
			player_1_won = True
			break
		elif "X" in grid[30] and "X" in grid[34] and "X" in grid[38]:
			player_1_won = True
			break
		# X diagonals
		elif "X" in grid[2] and "X" in grid[20] and "X" in grid[38]:
			player_1_won = True
			break
		elif "X" in grid[10] and "X" in grid[20] and "X" in grid[30]:
			player_1_won = True
			break


		# O columns
		if "O" in grid[2] and "O" in grid[16] and "O" in grid[30]:
			player_1_won = False
			break
		elif "O" in grid[6] and "O" in grid[20] and "O" in grid[34]:
			player_1_won = False
			break
		elif "O" in grid[10] and "O" in grid[24] and "O" in grid[38]:
			player_1_won = False
			break
		# O rows
		elif "O" in grid[2] and "O" in grid[6] and "O" in grid[10]:
			player_1_won = False
			break
		elif "O" in grid[16] and "O" in grid[20] and "O" in grid[24]:
			player_1_won = False
			break
		elif "O" in grid[30] and "O" in grid[34] and "O" in grid[38]:
			player_1_won = False
			break
		# O diagonals
		elif "O" in grid[2] and "O" in grid[20] and "O" in grid[38]:
			player_1_won = False
			break
		elif "O" in grid[10] and "O" in grid[20] and "O" in grid[30]:
			player_1_won = False
			break


		if until_tie == 9:
			tie = True
			break


	if player_1_won == True:
		print(grid)
		print(player_1, "won!")
	elif player_1_won == False and not tie:
		print(grid)
		print(player_2, "won!")

	if tie:
		print(grid)
		print("You both tied!")


game()
