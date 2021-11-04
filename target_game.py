


from typing import List
import random
import string
import os
os.getcwd()
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
    for i in noise:
        y = Alphabet[i]
        field.append(y)
    for i in (0,3,6):
        z.append(field[i].upper())
        z.append(field[i+1].upper())
        z.append(field[i+2].upper())
        grid.append(z)
        z = []
    return grid
def get_words(f: str, letters: List[str]) -> List[str]:

    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """

    letters_occurance_list = []
    word_list = []

    with open(f , 'r' ) as words_file:
        words_file.readline() # 'Wordlists\n'
        data = words_file.readline().strip() # '#en: English'
        while data.startswith( '#' ):
            data = words_file.readline().strip() # 'a'
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
                    word_list.append(word) 
    return word_list



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_word_list = []
    a = True
    while a:
        user_word = str(input())
        if user_word == '':

            break
        user_word_list.append(user_word)
        
    
    
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

#generate_grid()
print(get_words(r"C:\Users\Siromanec\Desktop\py_progs\lab6\en.txt" , ['s', 'g', 'i', 'v', 'r', 'v', 'o', 'n', 'q']))
get_user_words()