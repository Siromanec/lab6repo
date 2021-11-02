from typing import List
import random
import string

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    Alphabet = string.ascii_uppercase
    Alphabet = list(Alphabet)
    i=0
    noise = []
    field = []
    grid = []
    z =[]
    is_vowel = False
    while i<9:
        x = random.randint(0,25)
        if x == 0 or x == 4 or x == 8 or x == 14 or x == 20:
            is_vowel = True
        noise.append(x)
        i += 1
        if i == 9 and not is_vowel:
            i = 0
            noise = []
    print(noise)
    for i in noise:
        y = Alphabet[i]
        field.append(y)
    for i in (0,3,6):
        z.append(field[i])
        z.append(field[i+1])
        z.append(field[i+2])
        grid.append(z)
        print(z)
        z = []
    print(field)
    print(grid)
    pass


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    pass



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass

generate_grid()