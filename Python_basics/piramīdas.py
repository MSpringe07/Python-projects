def print_pyramid(height):
    for i in range(1, height + 1):
        # Print spaces for the left side of the pyramid
        for j in range(height - i):
            print(" ", end="")
        
        # Print asterisks for the left side of the pyramid
        for j in range(2 * i - 1):
            print("*", end="")
        
        # Move to the next line
        print()

# Get user input for the height of the pyramid
height = int(input("Enter the height of the pyramid: "))

# Call the function to print the pyramid
print_pyramid(height)