from board import Board

class Game:
    def __init__(self, board:Board):
        self._board = board


    def get_sentence_list(self):
        return self._board.sentence_list

    def get_hangman(self):
        return self._board.hangman

    def get_hangman_sentence(self):
        return self._board.hangman_sentence


    def set_hangman(self): 
        hangman = self.get_hangman()
        hangman_all = "hangman"

        if hangman == []:
            hangman.append('h')
            
        else:
           if hangman != "hangman":
            hangman.append(hangman_all[len(hangman)])

        self._board.set_hangman(hangman)
        return hangman

    def set_hangman_sentence(self,letter):

        sentence_list = self.get_sentence_list()
        hangman_sentence = self.get_hangman_sentence()


        for i in range(0, len(sentence_list)-1):
            if letter ==sentence_list[i]:
                hangman_sentence[i] = letter

        self._board.set_hangman_sentence(hangman_sentence)
        return hangman_sentence


    def deal_with_letter(self,letter):
        hangman_sentence = self.get_hangman_sentence()
        sentence_list = self.get_sentence_list()
        new_hangman = []
        new_hangman_sentence = []


        if letter in sentence_list:
            if letter not in hangman_sentence:
                new_hangman_sentence = self.set_hangman_sentence(letter)
            else:
                new_hangman = self.set_hangman()

        else:
            new_hangman = self.set_hangman()

        
        if "_" in hangman_sentence and new_hangman !=['h','a','n','g','m','a','n',"0"]:
            done = False

        else:
            done = True


        if new_hangman_sentence == []:
            new_hangman_sentence = hangman_sentence


        if new_hangman == []:
            new_hangman = self.get_hangman()
             
        return new_hangman_sentence, new_hangman,done

       
