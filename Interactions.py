import numpy.random
import random

def generate_code(length, num_colors, colors):
    '''
    Generate a secret code based on the specified length and number of colors.

    Args:
        length (int): The length of the generated code.
        num_colors (int): The number of unique colors in the code.

    Returns:
        list: The generated secret code.
    '''

    # Ensure the number of unique colors requested does not exceed the total number of available colors
    num_colors = min(num_colors, len(colors))

    # Shuffle the colors to randomly select unique colors
    random.shuffle(colors)

    # Take the first 'num_colors' colors from the shuffled list to ensure uniqueness
    selected_colors = colors[:num_colors]

    # Repeat the selected colors to match the desired length
    result = selected_colors * (length // num_colors) + selected_colors[:length % num_colors]

    return result

def pc_question(question_list, answer_code):

    '''
    When this function is called upon, it checks wether the player's question is correct

    Args: a list wich consists of four colors
           the secret code

    returns:
        list: white_pins: correct GIVEN colors, black_pins: correct PLACED colors
    '''

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
    When this function is called upon, it checks wether the computer's question is correct

    Args: a list wich consists of four colors
           the secret code

    returns:
        list: white_pins: correct GIVEN colors, black_pins: correct PLACED colors
    '''

    white, black = 0, 0

    for pin in pc_question(question_list, code):
        if pin == 'white':
            white += 1
        else:
            black += 1

    return [str(black), str(white)]
