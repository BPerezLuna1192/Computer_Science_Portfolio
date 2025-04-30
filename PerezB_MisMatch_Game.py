import random

# introduce the person to the game & give instructions
print('Welcome to Mismatch the Game! Here are the rules:')
print('\n')
print('You will choose two letters to match until you get all the letters correct.')
print('\n')

# Ask the user for their favorite prizes (4 prizes, each repeated twice)
prizes = []
print("Please enter 4 prizes that you like (one for each prize):")
for i in range(4):
    prize = input(f"Enter your prize {i+1}: ")
    prizes.append(prize)

# Duplicate the prizes to make sure each one is assigned to two letters
prizes = prizes * 2  # Each prize is now repeated twice

# Create a deck of cards by using 2d list of all cards (8 cards total)
square_list = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]

# Use a dictionary to map each letter to a prize
my_dict = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], prizes))

# Randomize the prizes (values) and assign them to letters
randomized_values = random.sample(prizes, len(prizes))  # Randomize the prizes

# Create a new dictionary with the randomized prizes
randomized_dict = dict(zip(my_dict.keys(), randomized_values))

# Display the initial game board with hidden values
def display_board(revealed):
    print("\nCurrent board:")
    for inner_list in square_list:
        print([randomized_dict[card] if card in revealed else card for card in inner_list])
    print("\n")

# Display the initial board before the game starts
print("Here's the board with the letters/cards:")
display_board([])  # Display the board with all cards hidden

# Define a function to check if the letters match based on their values
def check_letters(letter1, letter2): 
    if randomized_dict[letter1] == randomized_dict[letter2]: 
        print(f'Correct! The prize is: {randomized_dict[letter1]}')
        print('-------------------------------------------------------')
        return True 
    else: 
        print('Incorrect. Try again!')
        print('-------------------------------------------------------')
        return False 

# Count the number of cards left (each pair of matched letters reduces this count)
number_of_cards = len(my_dict) 
# List of revealed cards
revealed = []

# Main game loop
while number_of_cards > 0: 
    print(f'You have {number_of_cards} cards left.') 
    print('Choose two letters to match') 
    letter1 = input('Choose a letter: ').lower() 
    letter2 = input('Choose another letter: ').lower() 

    if letter1 not in my_dict or letter2 not in my_dict: 
        print("Invalid input. Please choose letters from the given options.")       
        continue 

    if check_letters(letter1, letter2):
        number_of_cards -= 2
        # Add the matched cards to the revealed list
        revealed.append(letter1)
        revealed.append(letter2)

        # Update the display of cards (show matched cards)
        display_board(revealed) 

        if number_of_cards == 0: 
            print("Congratulations! You have matched all the cards.")
            break  # End the game