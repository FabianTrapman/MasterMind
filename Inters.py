import numpy.random

def answer():

    '''
    input: takes none

    When this function is called upon, it generates a new random MasterMind code

    returns: a list wich consists four random colors
    '''

    list_numbers = numpy.random.randint(5, size=4)
    list_colors = []

    for i in list_numbers:

        if i == 0:
            list_colors.append('blue')
        elif i == 1:
            list_colors.append('green')
        elif i == 2:
            list_colors.append('orange')
        elif i == 3:
            list_colors.append('purple')
        elif i == 4:
            list_colors.append('red')
        else:
            list_colors.append('yellow')

    return list_colors

def answer_npc():

    colors = ['blue', 'green', 'orange', 'purple', 'red', 'yellow']

    answer_game = []

    print('A code consists of four colors.\n'
          'Colors to choose from: blue, green, orange, purple, red, yellow\n')

    color_one = ''
    color_two = ''
    color_three = ''
    color_four = ''

    color_one = input('Color 1: ')
    while color_one not in colors:
        print('Colors you have to chose from: blue, green, orange, purple, red, yellow')
        color_one = input('Color 1: ')
    color_two = input('Color 2: ')
    while color_two not in colors:
        print('Colors you have to chose from: blue, green, orange, purple, red, yellow')
        color_two = input('Color 2: ')
    color_three = input('Color 3: ')
    while color_three not in colors:
        print('Colors you have to chose from: blue, green, orange, purple, red, yellow')
        color_three = input('Color 3: ')
    color_four = input('Color 4: ')
    while color_four not in colors:
        print('Colors you have to chose from: blue, green, orange, purple, red, yellow')
        color_four = input('Color 4: ')

    answer_game.append(color_one)
    answer_game.append(color_two)
    answer_game.append(color_three)
    answer_game.append(color_four)

    return answer_game

def pc_question(question_list, answer_code):

    '''
    input: a list wich consists of four colors
           the secret code

    When this function is called upon, it checks wether the player's question is correct

    returns: a list of
             white_pins: correct GIVEN colors
             black_pins: correct PLACED colors
    '''
    #
    # print(question_list)
    # print(answer_code)

    list_check = []

    for i in range(len(answer_code)):
        if answer_code[i] == question_list[i]:
            list_check.append('black')
        elif answer_code[i] in question_list:
            list_check.append('white')
        else:
            'niks'

    return sorted(list_check)

def npc_question(question_list, code):
    '''
    input: a list wich consists of four colors
           the secret code

    returns: a list of
             white_pins: correct GIVEN colors
             black_pins: correct PLACED colors
             in numbers
    '''

    white, black = 0, 0

    for pin in pc_question(question_list, code):
        if pin == 'white':
            white += 1
        else:
            black += 1

    return [str(black), str(white)]

