from Grammar import Grammar
from Item import Item
from State import State
from CanonicalCollection import CanonicalCollection


class LR:
    def __init__(self,grammar):
        
        self.grammar = grammar
        self.workingGrammar = grammar.getEnrichedGrammar()
        # define somehow the ordered productions

    
    def getNonTerminalAfterDot(self, item):
        #    String term = item.getRightHandSide().get(item.getPositionForDot());
        term  = list(item.getRhs())
        productions = self.grammar.getProductions()

        if ( term[item.getDotPos()] not in productions.keys()):
            return None
        
        return term


    def closure(self, item):
        current_closure = set()
        current_closure.add(item)
        old_closure = set()

        m = 1
        while m == 1 or old_closure != current_closure:
            m = 0
            old_closure = current_closure
            new_closure = set(current_closure)

            for item in current_closure:
                non_terminal = self.getNonTerminalAfterDot(item)
                if non_terminal:
                    for prod in self.grammar.getProductionsForNonTerminal(non_terminal[0]):
                        current_item = Item(non_terminal, prod, 0)
                        new_closure.add(current_item)

            current_closure = new_closure

        return State(current_closure)



    def goto(self,state,element):
        result = set()

        for item in state.getItems():
           
            nonTerminal = list(item.getRhs())[0][item.getDotPos()] # get the symbol that is afer the do in each item 
            if nonTerminal == element:
                nextItem = Item(item.getLhs(), item.getRhs(), item.getDotPos() + 1)
                newState = self.closure(nextItem)
                print(newState.to_string())
                result.addAll(newState.getItems()) # ???? care e faza cu add all

        newResult  = State(result)
        return newResult
            

    def canonicalCollection(self):
        canonicalCollection = CanonicalCollection()
        canonicalCollection.addState(self.closure(Item(self.workingGrammar.getStartingSymbol(),self.workingGrammar.getProductionsForNonTerminal(self.workingGrammar.startingSymbol)[0],0))) # ['program']
        # canonicalCollection.addState(self.closure(Item(self.workingGrammar.getStartingSymbol(),self.workingGrammar.getProductionsForNonTerminal(self.workingGrammar.startingSymbol).get(0),0)))

        index = 0
        while(index < len(canonicalCollection.getStates())):
            print(len(canonicalCollection.getStates()))
            for symbol in canonicalCollection.getStates()[index].getSymbolsSucceedingTheDot():
                newState = self.goto(canonicalCollection.getStates()[index], symbol)
                print(newState.to_string())
                if not len(newState.items) == 0 :
                    indexState = canonicalCollection.getstates().index(newState)
                    if (indexState == -1):
                        canonicalCollection.addState(newState)

                        # verifica daca noua stare este in canonical si daca nu o adauga


            index = index + 1

        return canonicalCollection
                   

    def getGrammar(self):
        return self.grammar


    def getWorkigGrammar(self):
        return self.workingGrammar
