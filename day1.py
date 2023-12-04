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
foundnum1 = False
foundnum2 = False

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
    while foundnum1 == False:
        for character in nextline:
            if foundnum1 == True:
                foundnum1 = False
                break
            if character.isdigit():
                num1 = int(character)
                print("Found a number!!!", num1, "\n")
                foundnum1 = True
                total = total + num1
                break
            
    # Iterate through each character from the end until you find the first integer and save it as num2 then add it to total
