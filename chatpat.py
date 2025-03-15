def print_pattern(n):
    # Loop through the first half and the middle row
    for i in range(n):
        # Create the left side of the row (numbers ascending)
        left = ''.join(str(x) for x in range(1, n - i + 1))
        # Create the right side of the row (numbers descending)
        right = ''.join(str(x) for x in range(n - i - 1, 0, -1))
        
        # Combine the left and right parts
        row = left + right
        
        # Add '*' for non-middle rows
        if i == 0 or i == n - 1:
            print(f"**{row}**")
        else:
            print(f"*{row}*")
    
    # Loop through the second half (symmetric)
    for i in range(n - 2, -1, -1):
        # Create the left side of the row (numbers ascending)
        left = ''.join(str(x) for x in range(1, n - i + 1))
        # Create the right side of the row (numbers descending)
        right = ''.join(str(x) for x in range(n - i - 1, 0, -1))
        
        # Combine the left and right parts
        row = left + right
        
        # Add '*' for non-middle rows
        if i == 0 or i == n - 1:
            print(f"**{row}**")
        else:
            print(f"*{row}*")

# Get input from the user
n = int(input())  # Take input for the pattern size
print_pattern(n)
