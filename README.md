# SpellingBeeCheat
A Python program that provides answers for the NYT Spelling Bee game
spellingBeeCheat.py is the program and can be run like any other python file. 
The program is very simple and just asks the user for the list of letters and then to specify which of those letters is the special one that has to be included in every word. The program then prints all the possible words that fit the criteria. Since I was unable to locate the dictionary the NYT uses for their version of the game I use two different dictionaries and print the simple words that are almost guranteed to be accepted first before the group of more complex words that may be excluded from the NYT list. 
The words_simple.txt is just anagram_dictionary.txt from https://people.sc.fsu.edu/~jburkardt/datasets/words/words.html
words_complicated.txt is the TWL06 scrabble dictionary that I found here https://www.wordgamedictionary.com/twl06/download/twl06.txt
