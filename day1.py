#
# Advent of Code 2023 - Day 1
# Shekhar Dhupelia
# 

# Open the file
file = open("input.txt", "r")

# Setup some counters for later
total = 0
num1 = -1
num2 = -1
combined = 0

# Debug --- Setup a line counter
linecounter = 0

# Loop through each line of text
for nextline in file:

    # Prep the string for parsing
    line = nextline.strip('\n')

    # Reset num1 and num2
    num1 = -1
    num2 = -1

    # Iterate through each character from the beginning until you find the first integer, and then ignore the rest
    for character in line:
        if (num1 == -1):
            if character.isdigit():
                num1 = int(character)
                print("Found num1: ", num1)

    # Iterate through each character from the end until you find the second integer, and then ignore the rest
    for character in line [::-1]:
        if (num2 == -1):
            if character.isdigit():
                num2 = int(character)
                print("Found num2: ", num2)

    # Combine the two digits into a new two-digit number
    combined = (num1 * 10) + num2
    
    # Add the combined number to the total
    total = total + combined
    
    # Debug --- Increment the line counter for testing
    linecounter = linecounter + 1

# Print the final result
print("\n\n**** The Final Result =", total, " ****\n\n")

# Close the file and end
file.close()
exit()
