class Item:
    def __init__ (self,l,r,d):
        self.lhs = l #string
        self.rhs = r #list
        self.dotPos = d #int

    def getLhs(self) :
        return self.lhs
    
    def getRhs(self) :
        return self.rhs
    
    def getDotPos(self):
        return self.dotPos
    
    def to_string(self):
    # Extract the right-hand side of the production up to the position of the dot
        right_hand_side1 = list(self.rhs)[:self.dotPos]

        # Join the strings to represent the right-hand side before the dot
        string_right_hand_side1 = ''.join(right_hand_side1)

        # Extract the right-hand side of the production after the position of the dot
        right_hand_side2 = list(self.rhs)[0][self.dotPos:]

        # Join the strings to represent the right-hand side after the dot
        string_left_hand_side2 = ''.join(right_hand_side2)

        # Return the formatted string representation of the LR(0) item
        return f"{self.lhs} -> {string_right_hand_side1}.{string_left_hand_side2} \n"


    def __eq__(self, other_item):
        return (
            isinstance(other_item, Item) and
            self.lhs == other_item.lhs and
            self.rhs == other_item.rhs and
            self.dotPos == other_item.dotPos
        )
    
    def __hash__(self):
        result = self.lhs[0]
        if ( type(self.rhs) == list):
            for i in self.rhs:
                result = result + i
        else:
            result = result+self.rhs
        
        return hash(result)
