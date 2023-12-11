class CanonicalCollection:
    
    def __init__(self):
        self.states = []

    def addState(self,state):
        self.states.append(state)

    def getStates(self):
        return self.states
    
    def to_string(self):
        result = "" 
        for count , state in enumerate(self.getStates()):
            result = result + f"----------state at index: {count}-------------\n "
            result = result + state.to_string() + "\n"

        return result