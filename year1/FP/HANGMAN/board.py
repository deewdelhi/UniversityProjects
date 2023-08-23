class Board:
    def __init__(self,sentence_list, hangman_sentence):
        self.__sentence_list = sentence_list
        self.__hangman = []
        self.__hangman_sentence = hangman_sentence
        


    @property
    def sentence_list(self):
        return self.__sentence_list

    @property
    def hangman_sentence(self):
        return self.__hangman_sentence

    @property
    def hangman(self):
        return self.__hangman

    def set_hangman(self,new_hangman): 
        self.__hangman = new_hangman

    def set_hangman_sentence(self,new_hangman_sentence):
        self.__hangman_sentence = new_hangman_sentence
        
    




