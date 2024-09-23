from random import randrange

ship_initial = ["B", "C", "F", "A", "S"]
ship_names = ["Battleship", "Cruiser", "Frigate", "Aircraft Carrier", "Sub"]
map_size = 10

def get_username():
    """
    function getting username for welcome message
    """
    while True:
        user_name = input("Enter your name: ")
        if user_name:
            print(f"Welcome to the battleship game {user_name}!")
            return user_name
        else:
            print("Please enter your name.")

def create_battlefield(map_size):
    """
    function to create a map based on size
    """
    return [["_"] * map_size for _ in range(map_size)]

def display_battlefield(board):
    """
    function to display current state of the map.
    """
    for row in board:
        print(" ".join(row))

def player_ship_coordinate(player_board, occupied):
    """
    function for player placement ship
    """
    while True:
        try:
            row = int(input("Enter the row for Battleship: "))
            col = int(input("Enter the column for Battleship: "))
            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "B"
                occupied.add((row, col))
                while True:
                    direct = str(input("Enter direction you want ship to face (N, E, S, W); "))
                    if direct == 'N':
                        if col-4>=0:
                            for x in range(3):
                                player_board[row-1-x][col] = "B"
                                occupied.add((row, col))
                            break
                        else:
                            print ("You don't have space in that direction, try again")

                    
                    elif direct == 'S':
                        if col+4<10:
                            for x in range(3):
                                player_board[row+1+x][col] = "B"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")

                    elif direct == 'E':
                        if row+4<10:
                            for x in range(3):
                                player_board[row][col+1+x] = "B"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")
                    elif direct == 'W':
                        if row-4>0:
                            for x in range(3):
                                player_board[row][col-1-x] = "B"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")

                break
            else:
                print("Invalid coordinates. Please enter correct values.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Cruiser: "))
            col = int(input("Enter the column for Cruiser: "))
            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "C"
                occupied.add((row, col))
                while True:
                    direct = str(input("Enter direction you want ship to face (N, E, S, W); "))
                    if direct == 'N':
                        if col-2>=0:
                            for x in range(1):
                                player_board[row-1-x][col] = "C"
                                occupied.add((row, col))
                            break
                        else:
                            print ("You don't have space in that direction, try again")

                    
                    elif direct == 'S':
                        if col+2<10:
                            for x in range(1):
                                player_board[row+1+x][col] = "C"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")

                    elif direct == 'E':
                        if row+2<10:
                            for x in range(1):
                                player_board[row][col+1+x] = "C"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")
                    elif direct == 'W':
                        if row-2>0:
                            for x in range(1):
                                player_board[row][col-1-x] = "C"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")

                break
            else:
                print("Invalid coordinates. Please enter correct values.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Frigate: "))
            col = int(input("Enter the column for Frigate: "))
            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "F"
                occupied.add((row, col))
                while True:
                    direct = str(input("Enter direction you want ship to face (N, E, S, W); "))
                    if direct == 'N':
                        if col-3>=0:
                            for x in range(2):
                                player_board[row-1-x][col] = "F"
                                occupied.add((row, col))
                            break
                        else:
                            print ("You don't have space in that direction, try again")

                    
                    elif direct == 'S':
                        if col+3<10:
                            for x in range(2):
                                player_board[row+1+x][col] = "F"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")

                    elif direct == 'E':
                        if row+3<10:
                            for x in range(2):
                                player_board[row][col+1+x] = "F"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")
                    elif direct == 'W':
                        if row-3>0:
                            for x in range(2):
                                player_board[row][col-1-x] = "F"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")
                break
            else:
                print("Invalid coordinates. Please enter correct values.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Aircraft Carrier: "))
            col = int(input("Enter the column for Aircraft Carrier: "))

            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "A"
                occupied.add((row, col))
                while True:
                    direct = str(input("Enter direction you want ship to face (N, E, S, W); "))
                    if direct == 'N':
                        if col-5>=0:
                            for x in range(4):
                                player_board[row-1-x][col] = "A"
                                occupied.add((row, col))
                            break
                        else:
                            print ("You don't have space in that direction, try again")

                    
                    elif direct == 'S':
                        if col+5<10:
                            for x in range(4):
                                player_board[row+1+x][col] = "A"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")

                    elif direct == 'E':
                        if row+5<10:
                            for x in range(4):
                                player_board[row][col+1+x] = "A"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")
                    elif direct == 'W':
                        if row-5>0:
                            for x in range(4):
                                player_board[row][col-1-x] = "A"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            row = int(input("Enter the row for Submarine: "))
            col = int(input("Enter the column for Submarine: "))

            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "S"
                occupied.add((row, col))
                while True:
                    direct = str(input("Enter direction you want ship to face (N, E, S, W); "))
                    if direct == 'N':
                        if col-3>=0:
                            for x in range(2):
                                player_board[row-1-x][col] = "S"
                                occupied.add((row, col))
                            break
                        else:
                            print ("You don't have space in that direction, try again")

                    
                    elif direct == 'S':
                        if col+3<10:
                            for x in range(2):
                                player_board[row+1+x][col] = "S"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")

                    elif direct == 'E':
                        if row+3<10:
                            for x in range(2):
                                player_board[row][col+1+x] = "S"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")
                    elif direct == 'W':
                        if row-3>0:
                            for x in range(2):
                                player_board[row][col-1-x] = "S"
                                occupied.add((row, col))
                            break
                        else:
                            print("You don't have space in that direction, try again")
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return player_board, occupied

def comp_ship_coordinate(comp_board):
    """
    function for computer opponent.
    """
    for ship in ship_initial:
        while True:
            row = randrange(0, 10)
            col = randrange(0, 10)
            if comp_board[row][col] == "_":
                comp_board[row][col] = ship
                break

    return comp_board

def check_player_hit(comp_board, dummy_board, user):
    """
    Function for player hit or missed on enemy ship
    """
    print(user)
    row = int(input("Enter your row: "))
    col = int(input("Enter your col: "))
    hit = 1  # Assume there will be a hit

    if comp_board[row][col] == "B":
        comp_board[row][col] = "b"
        dummy_board[row][col] = "X" # 'X' will signify on the dummy board when a player hits a ship
        print("Computer: Battleship been hit!")
    elif comp_board[row][col] == "C":
        comp_board[row][col] = "c"
        dummy_board[row][col] = "X"
        print("Computer: Cruiser been hit!")
    elif comp_board[row][col] == "F":
        comp_board[row][col] = "f"
        dummy_board[row][col] = "X"
        print("Computer: Frigate been hit!")
    elif comp_board[row][col] == "A":
        comp_board[row][col] = "a"
        dummy_board[row][col] = "X"
        print("Computer: Aircraft Carrier been hit")
    elif comp_board[row][col] == "S":
        comp_board[row][col] = "s"
        dummy_board[row][col] = "X"
        print("Computer: Sub been hit")
    else:
        dummy_board[row][col] = "*"
        hit = 0  # Note that there was not a hit
        print("Missed me!")

    return hit


def check_comp_hit(player_board):                       # Refactored function to map hits and misses
    """
    function for comp hit or missed on the player ship
    """

    hit = 1                                             # Assunme there will be a hit

    while True:                                         # Randomly select a row and column that has not previously been fired upon
        row = randrange(0, 10)
        col = randrange(0, 10)
        if player_board[row][col] != "*" and player_board[row][col] != "a" and player_board[row][col] != "b" and comp_board[row][col] != "c" and comp_board[row][col] != "f" and comp_board[row][col] != "s":
            break

    print("Computer has selected coordinates", row, col)

    if player_board[row][col] == "B":                   # If the computer has hit a vessel, change the value to lowercase and return a hit value of "1"
        player_board[row][col] = "b"
        print("Player: Battleship been hit!")
    elif player_board[row][col] == "C":
        player_board[row][col] = "c"
        print("Player: Cruiser been hit!")
    elif player_board[row][col] == "F":
        player_board[row][col] = "f"
        print("Player: Frigate been hit!")
        hit = 1
    elif player_board[row][col] == "A":
        player_board[row][col] = "a"
        print("Player: Aircraft carrier been hit!")
    elif player_board[row][col] == "S":
        player_board[row][col] = "s"
        print("Player: Sub been hit!")
    else:
        hit = 0                                         # Note that there was not a hit
        print("Missed me!")
        player_board[row][col] = "*"

    return hit

if __name__ == "__main__":

        user = get_username()

        player_board = create_battlefield(map_size)
        comp_board   = create_battlefield(map_size)
        dummy_board = create_battlefield(map_size) # create a dummy board

        occupied = set()

        print("Player's turn:")
        player_ship_coordinate(player_board, occupied)
        display_battlefield(player_board)

        print("\nComputer opponent's turn:")
        comp_ship_coordinate(comp_board)
        # display_battlefield(comp_board) # for testing purposes
        display_battlefield(dummy_board)  # display the blank dummy board instead of computer board

        # Suggested while loop to alternate between the player and computer firing upon positions

        player_hits = 0 
        comp_hits   = 0

        while True:
            player_hits += check_player_hit(comp_board, dummy_board, user)   # If the player hit count reaches "5" all of the computer's vessels have been sunk
            if player_hits == 5:
                print("Player has won - game over")
                break

            comp_hits += check_comp_hit(player_board)           # If the computer hit count reaches "5" all of the player's vessels have been sunk
            if comp_hits == 5:
                print("Computer has won - game over")
                break


            print(f"Player {user} board")                       # Just included the redisplay of the boards for testing purposes
            display_battlefield(player_board)

            print(" ")

            print("Computer board")
            display_battlefield(dummy_board) # display dummy board instead of computer board