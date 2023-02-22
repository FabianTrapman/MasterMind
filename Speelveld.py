# Wanneer het spel start kun je gaan raden
# wanneer je wilt stoppen met het spel met einde spel ga je terug naar het startscherm
# press start to begin voor start spel
# met opslaan van speelveld worden alle oudere gokken opgeslagen en weergegeven
# met update speelveld wordt het speelveld aangepast
# met geheime code kan je de code weergeven als hij is geraden

from Inters import *

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
    Ends the game
    '''

def start():
    '''
    Starts the game
    '''

    global answer
    global human_question

    # Keeps track of the amount of questions the user has asked in total
    guess_counter = 0
    # Establishes the answer that the user needs to guess
    answer = answer()
    # Keeps track of past questions and pins and gives it to save_playfield()
    list_save_playfield_question = []
    list_save_playfield_pin = []


    # The colors the user can choose from
    colors = ['blue', 'green', 'orange', 'purple', 'red', 'yellow']
    print('Colors to chose from: blue, green, orange, purple, red, yellow\n'
          'Type \'start\' to start a new round')

    # The user has 10 guesses in total, once that is reached the while loop stops
    while guess_counter != 10:

        list_human_question = []

        # Each question takes four colors, once that is reached the while loops stops
        while len(list_human_question) != 4:

            guess = input('Guess a color: ')

            if guess == 'start':
                start()
            # If the given color is incorrect, it keeps asking for a correct one
            while guess not in colors:
                print('Colors you have to chose from: blue, green, orange, purple, red, yellow')
                guess = input('Guess a color: ')

                if guess == 'start':
                    start()

            list_human_question.append(guess)

        # Checks if the question is correct
        if list_human_question == answer:
            print('Congrats! That\'s the right answer.')
            break

        # Incorrect questions will be checked for white and black pins
        guess_pins = human_question(list_human_question, answer)

        list_save_playfield_question.append(list_human_question)
        list_save_playfield_pin.append(guess_pins)

        print(save_playfield(list_save_playfield_question, list_save_playfield_pin))

start()