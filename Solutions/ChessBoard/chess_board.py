# Open the file 'chess_board.txt' in write mode
file = open("chess_board.txt", "w")

# Initialize an empty list to represent the chess board
board = []

# Loop through 8 times to create each row of the chess board
for i in range(8):
    # Create a row with numbers from 1 to 8
    row = [i for i in range(1, 9)]
    # Append the row to the board
    board.append(row)
    # Write the row to the file, converting the list to a string
    file.write(str(row) + "\n")

# Close the file after writing all rows
file.close()

# Print the board to the console
print(board)

