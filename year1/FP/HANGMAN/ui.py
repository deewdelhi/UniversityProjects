from game import Game

class Ui:
    def __init__(self,game:Game):
        self._game = game


    def start_game(self):
        print( " ".join(self._game.get_hangman_sentence()))

        done = False
        while done == False:
            user_letter = input("enter your letter:  ")


            hangman_sentence,hangman,done=  self._game.deal_with_letter(user_letter)

            print ( " ".join(hangman_sentence)) 
            if 0 in hangman:
                hangman.remove(0)
            print ( "".join(hangman)) 

            if done == True or "".join(hangman) == "hangman" :
                print ( "game over")
                break



        