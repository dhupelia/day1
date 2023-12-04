#
# Advent of Code 2023 - Day 1
# Shekhar Dhupelia
# 

# Open the file
file = open("input.txt", "r")

# Setup some counters for later
total = 0
linecounter = 0
num1 = -1
num2 = -1

# Loop through each line of text
for nextline in file:

    # Increment the line counter for testing
    linecounter = linecounter + 1

    # Prep the string for parsing
    line = nextline.strip('\n')

    # Print the running total
    print("Line", linecounter, "Running Total =", total)

    # Iterate through each character from the beginning until you find the first integer, add it to the total, and then ignore the rest
    for character in line:
        if (num1 != -1):
            if character.isdigit():
                num1 = int(character)
                print("Found num1: ", num1)
                total = total + num1
        # Reset num1 now that we're done with the first integer
        num1 = -1

    # Iterate through each character from the end until you find the second integer, add it to the total, then add it to total
    for character in line [::-1]:
        if (num2 != -1):
            if character.isdigit():
                num2 = int(character)
                print("Found num2: ", num2)
                total = total + num2
        # Reset num2 now that we're done with the first integer
        num2 = -1

# Print the final result
print("\n\n**** The Final Result =", total, " ****\n\n")

# Close the file and end
file.close()
exit()
