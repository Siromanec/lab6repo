from typing import List
import random
import string
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    Alphabet = string.ascii_lowercase
    Alphabet = list(Alphabet)
    i=0
    noise = []
    field = []
    grid = []
    line_row =[]
    is_vowel = False
    while i<9:
        letter_index = random.randint(0,25)
        if letter_index == 0 or letter_index == 4 or letter_index == 8 or letter_index == 14 or letter_index == 20:
            is_vowel = True
        noise.append(letter_index)
        i += 1
        if i == 9 and not is_vowel:
            i = 0
            noise = []
    for i in noise:
        alpha_bet = Alphabet[i]
        field.append(alpha_bet)
    for i in (0,3,6):
        line_row.append(field[i].upper())
        line_row.append(field[i+1].upper())
        line_row.append(field[i+2].upper())
        grid.append(line_row)
        line_row = []
    return grid
def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f , 'r') as words_file:
        words_file.readline() # 'Wordlists\n'
        data = words_file.readline().strip() # '#en: English'
        while data.startswith( '#' ):
            data = words_file.readline().strip() # 'a'
        list1 = check_words(letters,words_file)
    return list1
def check_words(letters: List[str],words_file) -> List[str]:
    """
    checks if words have the right letters
    >>> check_words(['s', 'g', 'i', 'v', 'r', 'v', 'o', 'n', 'q'], \
        ['girn', 'giro', 'grin', 'gris', 'grison', 'groin', 'gros', \
        'inro', 'iron', 'noir', 'nori', 'ornis', 'ring', 'rosin',\
        'roving', 'sori', 'sorn', 'vigor', 'viron', 'visor'])
    ['girn', 'giro', 'grin', 'gris', 'grison', 'groin', 'gros', \
'inro', 'iron', 'noir', 'nori', 'ornis', 'ring', 'rosin', 'roving', \
'sori', 'sorn', 'vigor', 'viron', 'visor']
    """
    letters_occurance_list = []
    words_from_dict = []
    for ch_in in letters:
        rep = letters.count(ch_in)
        if tuple((ch_in,rep)) not in letters_occurance_list:
            if rep>1:
                for repeated in range(1,rep+1):
                    letters_occurance_list.append(tuple((ch_in,repeated)))              
            else:
                letters_occurance_list.append(tuple((ch_in,rep))) #add and count letters in initial list
        letters_occurance_set = set(letters_occurance_list)
    for word in words_file:
        word = word.strip()
        word_ch_occurance_list = []
        length = len(word)
        word_ch_list = list(word)
        if 3 < length <10 and letters[4] in word_ch_list: #check for length
            for ch_w in word_ch_list:
                rep_ch_w = word_ch_list.count(ch_w)
                if tuple((ch_w,rep_ch_w)) not in word_ch_occurance_list:
                    if rep_ch_w>1:
                        for repeated_ch_w in range(1,rep_ch_w+1):
                            word_ch_occurance_list.append(tuple((ch_w,repeated_ch_w)))
                    else:
                        word_ch_occurance_list.append(tuple((ch_w,rep_ch_w))) #add and count letters in initial list
            word_ch_occurance_set = set(word_ch_occurance_list)
            if word_ch_occurance_set - letters_occurance_set == set():
                words_from_dict.append(word)  
    return words_from_dict
def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    >>> get_user_words()
    []
    """
    user_word_list = []
    eweqa = True
    while eweqa:
        user_word = str(input())
        if user_word == '':

            break
        user_word_list.append(user_word)
    return user_word_list
def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    special_words=[]
    checked_words = check_words(letters,user_words)
    for i in checked_words:
        if i not in words_from_dict:
            special_words.append(i)
    return special_words
def results():
    """
    writes text
    """
    with open("result.txt", 'w'):
        pass
