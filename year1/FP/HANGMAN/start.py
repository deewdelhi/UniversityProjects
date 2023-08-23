

import random
from board import Board
from game import Game
from ui import Ui

file = open("sentences.txt" , "r")

number_of_sentences = int(file.readline())
sentence_number = random.randint(1,number_of_sentences)
i = 1

for line in file.readlines():
    if i == sentence_number:
        sentence = line

    i = i + 1

file.close()


sentence_list = list(sentence)
hangman_sentence = sentence_list.copy()

for i in range (0, len(hangman_sentence)-1):
    if i>0 :
        if hangman_sentence[i+1].isalpha() and hangman_sentence[i-1]!= " " and hangman_sentence[i]!= " ":
            hangman_sentence[i] = "_"


for j in range (0, len(hangman_sentence)-1):
    if hangman_sentence[j].isalpha():
        
        for x in range (0, len(sentence_list)-1):
         
            if hangman_sentence[j] == sentence_list[x] and hangman_sentence[x] == "_":
                hangman_sentence[x] =  sentence_list[x]
              


if __name__ == '__main__':
    ui = Ui(Game(Board(sentence_list,hangman_sentence)))
    ui.start_game()