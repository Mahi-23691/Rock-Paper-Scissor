import random

while True:

  choices = random.randint(1, 3)

  if choices == 1:
    c = "rock"
  elif choices == 2:
    c = "paper"
  elif choices == 3:
    c = "scissors"

  print('\nChoose one of these: \n1. Rock \n2. Paper \n3. Scissors')

  user_choice = int(input('\nEnter your choice: '))

  if user_choice == 1:
    print('\nYou chose Rock')
    print(f'\nComputer chose {c}')
  elif user_choice == 2:
    print('\nYou chose Paper')
    print(f'\nComputer chose {c}')
  elif user_choice == 3:
    print('\nYou chose Scissors')
    print(f'\nComputer chose {c}')

  if user_choice == 1 and choices == 1:
    print('\nIt\'s a tie!')
  if user_choice == 1 and choices == 2:
    print('\nYou lost!')
  if user_choice == 1 and choices == 3:
    print('\nYou won!')
    break
    
  if user_choice == 2 and choices == 1:
    print('\nYou won!')
  if user_choice == 2 and choices == 2:
    print('\nIt\'s a tie!')
  if user_choice == 2 and choices == 3:
    print('\nYou lost!')
    break
    
  if user_choice == 3 and choices == 1:
    print('\nYou lost!')
  if user_choice == 3 and choices == 2:
    print('\nYou won!')
  if user_choice == 3 and choices == 3:
    print('\nIt\'s a tie!')
    continue


  

