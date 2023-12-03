class CanonicalCollection:
    
    def __init__(self):
        self.states = []

    def addState(self,state):
        self.states.append(state)

    def getStates(self):
        return self.states
    
    def to_string(self):
        result = ""
        for state in self.states:
            result = result + state.to_string()

        return result