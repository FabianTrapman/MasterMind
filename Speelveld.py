from Interactions import *
from Strats import *

def save_playfield(list_question, list_pin):

    '''
    input: 
        list: past guesses and pins

    When this function is called upon it keeps track of all the past player's questions and pins

    returns:
         string: displays a neat version of your past guesses and pins
    '''

    save_playfield_string = f''
    guess_counter = 0

    for i in range(len(list_question)):
        guess_counter += 1
        save_playfield_string += f'guess {guess_counter}\n' \
                                 f'{list_question[i]}\n' \
                                 f'{list_pin[i]}\n'

    return save_playfield_string

def end():
    '''
    Ends the game and asks if the player wants to go for another round
    '''

    # Multiple prints and inputs to end the game

    print('Would you like to play again? yes/no')
    answer = input('')

    if answer == 'yes':
        print('You can either choose to,\n'
              'guess the computer\'s code or let the computer guess your code.\n'
              '\n'
              'type \'pc\' to guess yourself\n'
              'type \'npc\' to let the computer guess\n')

        version = input('Answer: ')

        if version == 'pc':
            start_pc()
        elif version == 'npc':
            start_npc()
    else:
        exit()

def start_npc():
    '''
    Starts the non-player controlled game
    '''

    global simplestrategy

    # Multiple prints and inputs to get the game going

    print("For the difficulty of this game you can choose to")
    print("Go for the DEFAULT mode, which makes you play with 6 different colors and a code length of 4")
    print("Go for the ENHANCED mode, which makes you play with up to 16 different colors and a code length of up to 8")
    print("Please choose the game mode that you would like to play")
    print("Game modes to choose from: default, enhanced")
    mode = input("Choose a difficulty: ")

    if mode == "default":
        colors = ["blue", "green", "orange", "purple", "red", "yellow"]
        answer_game = generate_code(4, 6, colors)
        
    elif mode == "enhanced":
        colors = ['blue', 'green', 'orange', 'purple', 'red', 'yellow', 'grey', 'maroon', 'fuchsia', 'lime', 'olive',
                'navy', 'teal', 'aqua', 'silver', 'white']

        print('How long should your code be?')
        length_code = input('Make your choice: ')
        length_code = int(length_code)

        print('With how many colors would you like to play? (max 16)')
        amount_colors = input('Make your choice: ')
        amount_colors = int(amount_colors)

        answer_game = generate_code(length_code, amount_colors, colors)

    print('Wich algorithm would you like to use?\n'
          'simple strategy, worst case or fabian\n')

    algo = input('Make your choice: ')

    guesses = list(itertools.product(set(answer_game), repeat=length_code))

    print(f"The code that computer will try to guess is {answer_game}")

    # Keeps track of all guesses
    guess_counter = 0
    # Picks a random code from all possible guesses left
    current_guess = guesses[random.randint(0, len(guesses))]

    # Asks the user for black and white pins
    print(f'code : {current_guess}')
    # black_pins = input('How many colors are correctly placed?: ')
    # white_pins = input('How many colors are correctly given but not correctly placed?: ')

    black_pins, white_pins = npc_question(current_guess, answer_game)

    print(f"{black_pins} black pins")
    print(f"{white_pins} white pins")

    # The computer has guessed correctly, and will display it
    if current_guess == tuple(answer_game):
        print(f'You gave the code: {answer_game}.\n'
              f'The computer guessed: {current_guess}\n'
              f'The computer guessed correctly!\n')

    # The guesses variable gets replaced by the new list, wich contains all the new possibilities
    # if algo == 'simple strategy':
    guesses = simplestrategy(guesses, current_guess, npc_question(current_guess, answer_game))

    # The computer has 10 tries, once that is reached the computer has lost
    while guess_counter != 11:
        # Picks a random code from all possible guesses left
        if algo == 'simple strategy' and len(guesses) != 1:
            current_guess = guesses[random.randint(0, len(guesses))]
        elif algo == 'simple strategy' and len(guesses) == 1:
            current_guess = guesses[0]
        elif algo == 'worst case':
            current_guess = worstcase(guesses, current_guess, [black_pins, white_pins])

        # Asks the user for black and white pins
        print(f'guess : {current_guess}')

        # black_pins = input('How many colors are correctly placed?: ')
        # white_pins = input('How many colors are correctly given but not correctly placed?: ')

        black_pins, white_pins = npc_question(current_guess, answer_game)

        print(f"{black_pins} black pins")
        print(f"{white_pins} white pins")
        print(answer_game)
        print(len(answer_game))

        # The computer has guessed correctly, and will display it
        if current_guess == tuple(answer_game):
            print(f'You gave the code: {answer_game}.'
                  f'The computer guessed: {current_guess}'
                  f'The computer guessed correctly!')

            end()

        # The guesses variable gets replaced by the new list, wich contains all the new possibilities
        # if algo == 'simple strategy':
        guesses = simplestrategy(guesses, current_guess, npc_question(current_guess, answer_game))
        print(len(guesses))

def start_pc():
    '''
    Starts the player controlled game
    '''

    global answer
    global pc_question

    # Keeps track of the amount of questions the user has asked in total
    guess_counter = 0
    # Establishes the answer that the user needs to guess

    print("For the difficulty of this game you can choose to")
    print("Go for the DEFAULT mode, which makes you play with 6 different colors and a code length of 4")
    print("Go for the ENHANCED mode, which makes you play with up to 16 different colors and a code length of up to 8")


    print("Please choose the game mode that you would like to play")
    print("Game modes to choose from: default, enhanced")
    mode = input("Choose a difficulty: ")

    if mode == "default":
        colors = ['blue', 'green', 'orange', 'purple', 'red', 'yellow']
        answer_game = generate_code(4, 6, colors)

    elif mode == "enhanced":
        colors = ['blue', 'green', 'orange', 'purple', 'red', 'yellow', 'grey', 'maroon', 'fuchsia', 'lime', 'olive',
                'navy', 'teal', 'aqua', 'silver', 'white']
        
        print('How long should your code be?')
        length_code = input('Make your choice: ')
        length_code = int(length_code)

        print('With how many colors would you like to play? (max 16)')
        amount_colors = input('Make your choice: ')
        amount_colors = int(amount_colors)

        answer_game = generate_code(length_code, amount_colors, colors)

    # Keeps track of past questions and pins and gives it to save_playfield()
    list_save_playfield_question = []
    list_save_playfield_pin = []


    # The colors the user can choose from
    colors = ['blue', 'green', 'orange', 'purple', 'red', 'yellow']
    print(f'Colors to choose from: {colors}\n'
          'Type \'start\' to start a new round')

    # The user has 10 guesses in total, once that is reached the while loop stops
    while guess_counter != 11:

        list_pc_question = []

        # Each question takes four colors, once that is reached the while loops stops
        while len(list_pc_question) != 4:

            guess = input('Guess a color: ')

            if guess == 'start':
                start_pc()
            # If the given color is incorrect, it keeps asking for a correct one
            while guess not in colors:
                print(f'Colors you have to chose from: {colors}')
                guess = input('Guess a color:  ')

                if guess == 'start':
                    start_pc()

            list_pc_question.append(guess)

        # Checks if the question is correct
        if list_pc_question == answer_game:
            print('Congrats! That\'s the right answer.')
            break

        # Incorrect questions will be checked for white and black pins
        guess_pins = pc_question(list_pc_question, answer_game)

        list_save_playfield_question.append(list_pc_question)
        list_save_playfield_pin.append(guess_pins)

        print(save_playfield(list_save_playfield_question, list_save_playfield_pin))

        guess_counter += 1

    print('Oh no! You\'re a disappointing failure!')

    end()

# Introduction + giving the option to guess or give feedback
print('Welcome to Fabian\'s version of Mastermind!\n'
      'You can either choose to,\n'
      'guess the computer\'s code or let the computer guess your code.\n'
      '\n'
      'type \'pc\' to guess yourself\n'
      'type \'npc\' to let the computer guess\n')

version = input('Make your choice: ')

# obviously pc stands for player controlled and npc stands for non player controlled
if version == 'pc':
    start_pc()
elif version == 'npc':
    start_npc()