import json
from collections import defaultdict

import requests


def download_word_list():
    #possible update get url from env
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    response = requests.get(url)
    return response.text.split()

def prepare_word_dictionary(words):
    word_dict = defaultdict(lambda: defaultdict(list))
    for word in words:
        if word.isalpha():  # Only include words with alphabetic characters
            length = len(word)
            first_letter = word[0].lower()
            word_dict[first_letter][length].append(word)
    return word_dict

words = download_word_list()
word_dict = prepare_word_dictionary(words)

# Convert defaultdict to a normal dict for JSON serialization
normal_dict = {k: {ik: iv for ik, iv in v.items()} for k, v in word_dict.items()}

with open('word_converter/word_dict.json', 'w') as f:
    json.dump(normal_dict, f, indent=4)
