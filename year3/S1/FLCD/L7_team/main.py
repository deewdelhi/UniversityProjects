from Grammar import Grammar
from LR import LR

def printGrammarMenu():
    print( "0-exit")
    print("1-is CFG")
    print( "2-show terminals")
    print( "3-show non terminals")
    print( "4-show starting symbol")
    print( "5-show productions")
    # print( "6-activate the monster")
    print( "7-productions for non terminal")

def start():
    printGrammarMenu()
    g = Grammar()
    while True:
        i = int(input(" enter your choice:    "))
        if ( i == 0):
            break
        elif( i == 1):
            print(g.getIsCGF())
        elif( i == 2):
            print(g.getTerminals())
        elif( i==3):
             print(g.getNonTerminals())
        elif(i == 4):
             print(g.getStartingSymbol())
        elif(i == 5):
             print(g.getProductions())

        elif(i == 6):
            lrAlg = LR(g)
            
            print(lrAlg.canonicalCollection().to_string())

        elif(i == 7):
            j = input("enter the non terminal:    ")
            print(g.getProductionsForNonTerminal(j))


start()

# g = Grammar()

# lrAlg = LR(g)
# print(lrAlg.canonicalCollection().to_string())

