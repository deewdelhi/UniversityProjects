
import re
class FinaiteAutomata:

    def __init__(self):
        self.separator = ";"
        self.isDeterministic = False
        self.initialState = ""
        self.states = []
        self.alphabet = []
        self.finalStates = []
        self.transitions = dict()
        self.readFromFile()

    def readFromFile(self):
        with open(r"D:\uni\UniversityProjects\year3\S1\FLCD\L5_L6_FA\FiniteAutomata.txt","r") as file:
            for index, line in enumerate(file):
                if (index < 4 ):
                  
                    faElement = re.split(r'[;\n]+', line)
                    
                    filtered_list = [s for s in faElement if s]
                    
                    if ( index == 0):self.states = filtered_list
                    elif( index == 1):self.initialState = filtered_list[0]
                    elif(index == 2): self.alphabet = filtered_list
                    else: self.finalStates = filtered_list
                    
                else:
                    newLine = re.split(r'[ \n]+', line)
                    f_list = [s for s in newLine if s]
                    
                    #print(f_list)
                    if ( f_list[0] in self.states and f_list[2] in self.states and f_list[1] in self.alphabet ):
                        transitionState = (f_list[0], f_list[1])
                        if ( not transitionState in self.transitions.keys() ):
                            newSet = set(f_list[2])
                            self.transitions[transitionState] = newSet
                        else :
                            self.transitions[transitionState].__add__(f_list[2])

        self.isDeterministic = self.checkIfdeterministic()

        for key in self.transitions.keys():
            self.transitions[key] = list(self.transitions[key])

    def checkIfdeterministic(self) :

        for key in self.transitions.keys():
            if ( len(self.transitions[key]) > 1):
                return False

        return True

    def acceptSequence(self,sequence):
        if (not self.isDeterministic): return False

        if ( len(sequence) == 0): return self.initialState in self.finalStates

        currentState = self.initialState
         
        for i in range (len(sequence)):
            currentSymbol = sequence[i:i+1]
            transition = (currentState,currentSymbol)
           # print( currentState, currentSymbol)
            if ( not transition in self.transitions.keys() ): return False
            else:
                currentState = self.transitions[transition][0]
        
        return currentState in self.finalStates


    def startigMenu(self):
        print("1. states")
        print("2. alphabet")
        print("3. initial state")
        print("4. final states")
        print("5. transitions")
        print("6. is deterministic")
        print("7. check sequence")
        print("8. exit")

    def start_org(self):
        exit  = False
        sequence =""
        self.startigMenu()

        while not exit:
            choice = int( input("enter choice: ----   ") )
            if ( choice == 1):
                print(self.states)
            elif ( choice == 2):
                print(self.alphabet)
            elif ( choice == 3):
                print( self.initialState)
            elif ( choice == 4):
                print(self.finalStates)          
            elif ( choice == 5):
                print(self.transitions)
            elif ( choice == 6):
                print( self.isDeterministic)
            elif ( choice == 7):
                sequence = input("enter sequence:   ")
                if ( self.isDeterministic ) :
                    if ( self.acceptSequence(sequence)) :
                        print(f"sequence: {sequence} => accepted")
                    else:
                        print( f"sequence: {sequence} => not accepted")
                else:
                    print("not deterministic")

            else:
                exit = True


         



                 






           