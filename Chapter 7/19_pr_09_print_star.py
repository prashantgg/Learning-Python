for i in range(3):  # Outer loop for rows
    for j in range(3):  # Inner loop for columns
        if i == 1 and j == 1:  # Check if it's the middle position
            print(" ", end=" ")  # Print an empty space
        else:
            print("*", end=" ")  # Print a star
    print()  # Move to the next line after each row
