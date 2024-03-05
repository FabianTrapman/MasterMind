import itertools
import random

from Interactions import *
from itertools import permutations

def simplestrategy(possible_guesses, current_guess, fb):
    '''
    Guesses the code by filtering through a list of codes, looking for impossible guesses
    all possible guesses will be added to a new list    

    input:
        list: a list with all possible guesses left
        current_guess: the last given guess
        black: correct PLACED colors
        white: correct GIVEN colors

    returns: a guess that is left in the list

    bron: https://github.com/LinaBlijlevenHU/StructuredProgramming2023/blob/main/Les6/mastermind.py
          'Yet Another Mastermind Strategy' - Barteld Kooi / Universiteit Groningen
    '''

    # The list that will contain all possible guesses left
    new_guesses = []

    for code in possible_guesses:
        if fb == npc_question(current_guess, code):
            new_guesses.append(code)

    return new_guesses

def worstcase(possible_guesses, current_guess, fb):
    '''
    Guesses the code by filtering through a list of codes, evaluating how many possibilities would be left
    if it were to guess with that code. The code with most possibilities will be taken.

    input: possible_guesses: A list with all possible guesses left
           current_guess: the last given guess
           black: correct PLACED colors
           white: correct GIVEN colors

    returns: a code that has a list with highest possibilities left

    bron: 'Yet Another Mastermind Strategy' - Barteld Kooi / Universiteit Groningen
    '''

    guesses_aantal = {}

    guesses = simplestrategy(possible_guesses, current_guess, fb)

    for code in possible_guesses:
        guesses_aantal[len(simplestrategy(possible_guesses, code, fb))] = code

    return guesses_aantal[max(guesses_aantal)]
