
import re

def load_words():
    with open('words_complicated.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
def simple_words():
    with open('words_simple.txt')as word_file:
        simple_words = set(word_file.read().split())
    return simple_words

def find_words(prefix):
    potential = ([item for item in matching_items if item.startswith(prefix)])
    if prefix in matching_items:
        words.append(prefix)
    if len(potential)>0:
        for i in letters:
            find_words( prefix+i)
    

if __name__ == '__main__':
    english_words = load_words()
    simpleWords = simple_words()

    letters= input("What is the list of letters? ").lower()
    prefix = input("What is the special letter? ").lower()
    min_length =4
    pattern = f'^(?=[^{prefix}]*{prefix})[{letters}]{{{min_length},}}$'
    
    regex = re.compile(pattern)
    words =[]
    simple = []
    
    for item in simpleWords:
        if regex.search(item):
           simple.append(item)
    simple.sort()
    
    for item in english_words:
        if regex.search(item):
            words.append(item)
    words.sort()
    for i in simple:
        print(i)
    print("Number of simple words found is: " + str(len(simple)))
    print("\n\n\n")
    print("More complicated words")
    for i in words:
        if not(i in simple):
            print(i)
    print("Total number of words found is: " + str(len(words)))
