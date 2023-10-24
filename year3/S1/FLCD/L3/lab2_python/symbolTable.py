from hashTable import KeyValuePair, HashTable
class SymbolTable:
    def __init__(self,  size,identifiersHashTable:HashTable,intConstantsHashTable:HashTable,stringConstantsHashTable:HashTable ):
        self.size = size
        self.identifiersHashTable = identifiersHashTable
        self.intConstantsHashTable  = intConstantsHashTable 
        self.stringConstantsHashTable  = stringConstantsHashTable


    def get_size(self):
        return self.size
    
    def addIdentifier( self,identifier):
        self.identifiersHashTable.add(identifier)
        return identifier
    
    def addIntConstant( self, constant):
        self.intConstantsHashTable.add(constant)
        return constant
    
    def addStringConstant( self, constant):
        self.stringConstantsHashTable.add(constant)
        return constant

    def hasIdentifier(self,identifier):
        return self.identifiersHashTable.contains(identifier)
    
    def hasIntConstant(self,identifier):
        return self.intConstantsHashTable.contains(identifier)

    def hasStringConstant(self,identifier):
        return self.stringConstantsHashTable.contains(identifier)
    
    def toString(self):
        self.identifiersHashTable.toString()

