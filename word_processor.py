
from collections import Counter
from functools import reduce
import string


def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    '''
    this function returns a list of words from a string,
    empty string returns a empty list,
    using lambda functions
    '''
    if text == '':
        return []
    else:
        text = split(",.? \n",text)
        list_words = list(map(lambda word: word.lower(),filter(lambda word : word != "", text)))
        return list_words



def words_longer_than(length, text):
    '''
    this function returns a list of words from a string,
    use the length to return words that are greater than the length
    empty string returns a empty list,
    using lambda functions
    '''
    if text == [] :
        return
    else:
        text = convert_to_word_list(text)
        length_of_words = list(map(lambda word: word, filter(lambda word: len(word)>length,text)))
        return length_of_words


def words_lengths_map(text):
    '''
    this function returns a dict of keys as numbers from a string,
    count how many words that have the length of the key value
    empty string returns a empty dict,
    using lambda functions
    '''
    if text == []:
        return {}
    else:
        text = convert_to_word_list(text)
        count_words = { word : len(word) for word in text}
        words = list(count_words.values())
        lenght_words = {length : words.count(length) for length in count_words.values()}
        return lenght_words


def letters_count_map(text):
    '''
    this function returns a dict of keys as alphabet from A to Z,
    count how many A to Z are in our string.
    I imported STRING at the top of the code to use (string.ascii_lowercase)
    '''
    text = text.lower()
    letters=list(string.ascii_lowercase)
    count = {key : text.count(key) for key in letters}
    return count


def most_used_character(text):
    '''
    dict.items return as keys and values in a tuple 
    compare all tuples with each other and takes the highest value
    empty string returns none,
    using lambda functions
    '''
    if text == "":
        return
    else:
        dict = letters_count_map(text)
        highest_letter = list(reduce(lambda x, y: x if x[1] > y[1] else y, dict.items()))
        return highest_letter[0]
