from Inters import *
from Strats import *

def save_playfield(list_question, list_pin):

    '''
    input: a list with past guesses and pins

    When this function is called upon it keeps track of all the past player's questions and pins

    returns: a string wich displays a neat version of your past guesses and pins
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

    print('Wich algorithm would you like to use?\n'
          'simple strategy, worst case or fabian\n')

    algo = input('Make your choice: ')

    # Generates all possible guesses and puts them in a list
    colors = ['blue', 'green', 'orange', 'purple', 'red', 'yellow']
    # Bron(Itertools): docent
    guesses = list(itertools.product(colors, repeat=4))
    print(len(guesses))

    answer_game = answer_npc()

    # Keeps track of all guesses
    guess_counter = 0
    # Picks a random code from all possible guesses left
    current_guess = guesses[random.randint(0, len(guesses))]

    # Asks the user for black and white pins
    print(f'code : {current_guess}')
    black_pins = input('How many colors are correctly placed?: ')
    white_pins = input('How many colors are correctly given but not correctly placed?: ')

    # The computer has guessed correctly, and will display it
    if black_pins == 4:
        print(f'You gave the code: {answer_game}.\n'
              f'The computer guessed: {current_guess}\n'
              f'The computer guessed correctly!\n')

    # The guesses variable gets replaced by the new list, wich contains all the new possibilities
    # if algo == 'simple strategy':
    guesses = simplestrategy(guesses, current_guess, npc_question(current_guess, answer_game))

    # The computer has 10 tries, once that is reached the computer has lost
    while guess_counter != 11:
        # Picks a random code from all possible guesses left
        print(guesses)
        if algo == 'simple strategy':
            current_guess = guesses[random.randint(0, len(guesses))]
        elif algo == 'worst case':
            current_guess = worstcase(guesses, current_guess, [black_pins, white_pins])

        # Asks the user for black and white pins
        print(f'code : {current_guess}')

        black_pins = input('How many colors are correctly placed?: ')
        white_pins = input('How many colors are correctly given but not correctly placed?: ')

        # The computer has guessed correctly, and will display it
        if black_pins == '4':
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
    answer_game = answer()
    # Keeps track of past questions and pins and gives it to save_playfield()
    list_save_playfield_question = []
    list_save_playfield_pin = []


    # The colors the user can choose from
    colors = ['blue', 'green', 'orange', 'purple', 'red', 'yellow']
    print('Colors to choose from: blue, green, orange, purple, red, yellow\n'
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
                print('Colors you have to chose from: blue, green, orange, purple, red, yellow')
                guess = input('Guess a color: ')

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