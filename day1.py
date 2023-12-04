#
# Advent of Code 2023 - Day 1
# Shekhar Dhupelia
# 

# Open the file
file = open("input.txt", "r")

# Setup some counters for later
total = 0
num1 = 0
num2 = 0

# Loop through each line of text
while True:
    nextline = file.readline()

    # Print the running total
    print("Running Total = ", total, "\n")

    # If there is no next line in the file, print the total result and break out of this loop
    if not nextline:
        print(total)
        break

    # Iterate through each character from the beginning until you find the first integer and save it as num1
    while True:
        for character in nextline:
            print(character)
            if character.isdigit():
                num1 = character
                print("Found a number!!!", "num1", "\n")
                break
            

    # Iterate through each character from the end until you find the first integer and save it as num2

    # Output both numbers for my sanity
    print(num1)
    print(num2)

    # Add these two integers to our running total
    total = total + num1 + num2
