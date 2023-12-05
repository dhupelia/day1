#
# Advent of Code 2023 - Day 1
# Shekhar Dhupelia
# 

# Part 2

# Open the file
file = open("input.txt", "r")

# Setup some counters for later
total = 0
num1 = -1
num2 = -1
combined = 0

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

    # Iterate through each character from the end until you find the second integer, and then ignore the rest
    for character in line [::-1]:
        if (num2 == -1):
            if character.isdigit():
                num2 = int(character)

    # Combine the two digits into a new two-digit number
    combined = (num1 * 10) + num2
    
    # Add the combined number to the total
    total = total + combined
    
# Print the final result of Part 1
print("\n\n**** The Final Result of Part 1 =", total, " ****\n\n")

# Close the file
file.close()

# Part 2
'''
# Re-open the file
#file = open("input.txt", "r")
file = open("test_input_part2.txt")

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

    # Iterate through each character from the end until you find the second integer, and then ignore the rest
    for character in line [::-1]:
        if (num2 == -1):
            if character.isdigit():
                num2 = int(character)

    # Combine the two digits into a new two-digit number
    combined = (num1 * 10) + num2
    
    # Add the combined number to the total
    total = total + combined

# Print the final result of Part 2
print("\n\n**** The Final Result of Part 2 =", total, " ****\n\n")

# Close the file and end
file.close()
'''
exit()


