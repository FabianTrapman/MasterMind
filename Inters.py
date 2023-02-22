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

def human_question(question_list, answer_code):

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
