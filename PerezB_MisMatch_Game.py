import random
#introduce the person to the game
print('welcome to mismatch the game, here are the rules:')
print('\n')
print('you will chose two letters to match until you get all\nthe letters correct.')
print('\n')

#ask the user to chose two letters
print('choose two letters to match')
print('\n')

# Create a deck of cards 
square_list = [['a','b','c','d'],['e','f','g','h']]
for inner_list in square_list:    
  print(inner_list) 
  my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 3, 'f': 1, 'g': 7, 'h': 7} 
  list_copy = list(my_dict.values())
  new_list_copy = random.sample(list_copy, len(list_copy))
  random_list = dict(zip(my_dict.keys(), new_list_copy))


# Define a function to check if the letters match 
def check_letters(letter1, letter2): 
  if random_list.get(letter1) == random_list.get(letter2): 
    print('Correct!') 
    print('-------------------------------------------------------')
    return True 
  else: 
    print('Incorrect!')
    print('-------------------------------------------------------')
    return False 

# Count the number of cards left 
number_of_cards = len(my_dict) 
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

# Update the display of cards 
    square_list = [[' ' if card == letter1 or card == letter2 else card for card in sublist] for sublist in square_list]
    for inner_list in square_list: 
      print(inner_list) 

    if number_of_cards == 0: 
      print("Congratulations! You have matched all the cards.")