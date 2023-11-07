import re
import os
from symbolTable import SymbolTable
from typing import List
from symbolTable import SymbolTable
from hashTable import HashTable

class ScannerException(Exception):
    pass

class Scanner:
    def __init__(self):
        self.program = None
        self.tokens = []
        self.reservedWords = []
        self.symbolTable = None
        self.PIF = []
        self.index = 0
        self.currentLine = 1
        self.read_tokens()
        self.separators = ["{", "}", "(", ")", "[", "]", ":", ";", " ", ",", "\t", "\n", "'", "\"","<<",">>","->"]
        self.operators = ["+", "-", "*", "/", "%", "<=", ">=", "==", "!=", "<", ">", "=", "!=!", "<>", "="]

    def set_program(self, program):
        self.program = program

    def read_tokens(self):
        
        with open(r"D:\uni\UniversityProjects\year3\S1\FLCD\L3\lab2_python\token.in","r") as file:
            for line in file:
                parts = line.strip().split(" ")
                if parts[0] in ["FCT","int","string","char","bool","READ","IF","ELSE","DO","arr","GO_THROUGH","SENDBACK","SHOW","SENDBACK","IF","MIN_INT","MAX_INT"]:
                    self.reservedWords.append(parts[0])
                else:
                    self.tokens.append(parts[0])

        print( self.tokens)
        print( self.reservedWords)

    def skip_spaces(self):
        while self.index < len(self.program) and self.program[self.index].isspace():
            if self.program[self.index] == '\n':
                self.currentLine += 1
            self.index += 1

    def skip_comments(self):
        while self.index < len(self.program) and self.program[self.index] == '#':
            while self.index < len(self.program) and self.program[self.index] != '\n':
                self.index += 1

    def treat_string_constant(self):
        regex_for_string_constant = re.compile(r'^"[a-zA-Z0-9_ ?:*^+=.!]*"')
        matcher = regex_for_string_constant.match(self.program[self.index:])
        if not matcher:
            if re.compile(r'^"[^"]"').match(self.program[self.index:]):
                raise ScannerException("Invalid string constant at line " + str(self.currentLine))
            if re.compile(r'^"[^"]').match(self.program[self.index:]):
                raise ScannerException("Missing \" at line " + str(self.currentLine))
            return False
        string_constant = matcher.group(0)
        self.index += len(string_constant)
        try:
            position = self.symbolTable.addStringConstant(string_constant)
        except Exception as e:
            position = self.symbolTable.getPositionStringConstant(string_constant)
        self.PIF.append(("str const", position))
        return True

    def treat_int_constant(self):
        regex_for_int_constant = re.compile(r'^([+-]?[1-9][0-9]*|0)')
        matcher = regex_for_int_constant.match(self.program[self.index:])
        if not matcher:
            return False
        if re.compile(r'^([+-]?[1-9][0-9]*|0)[a-zA-Z_]').match(self.program[self.index:]):
            return False
        int_constant = matcher.group(1)
        self.index += len(int_constant)
        try:
            position = self.symbolTable.addIntConstant(int(int_constant))
        except Exception as e:
            position = self.symbolTable.getPositionIntConstant(int(int_constant))
        self.PIF.append(("int const", position))
        return True

        """
        _summary_
        possible_identifier NOT valid when:
            - if it s a reserved word
            - if it s not a variable declaration ( ex: myFunction(int) variableName(char) anotherVar(string) yetAnotherVar(bool) )
        """
    def check_if_valid(self, possible_identifier, program_substring):
        if possible_identifier in self.reservedWords:
            return False
        if re.match(r'^[A-Za-z_][A-Za-z0-9_]* \((int|char|string|bool)\)', program_substring):
            return True
        return self.symbolTable.hasIdentifier(possible_identifier)

    def treat_identifier2(self):
       # regex_for_identifier_declaration = re.compile(r'^[A-Za-z_][A-Za-z0-9_]* \((int|char|string|bool)\)')
        regex_for_identifier = re.compile(r'^([a-zA-Z_][a-zA-Z0-9_]*)')
        matcher = regex_for_identifier.match(self.program[self.index:])
        if not matcher:
            return False
        identifier = matcher.group(1)
        if not self.check_if_valid(identifier, self.program[self.index:]):
            return False
        self.index += len(identifier)
        try:
            position = self.symbolTable.addIdentifier(identifier)
        except Exception as e:
            position = self.symbolTable.getPositionIdentifier(identifier)
        self.PIF.append(("identifier", position))
        return True
    
    def treatAsIdentifier(self,token):
        if token.isidentifier():
            # is the token a reserved word?
            for reservedKeyword in self.reservedWords:
                if reservedKeyword == token:
                    self.index += len(token) + 1 # for the space 
                    self.PIF.append((token, (-1, -1)))
                    return True
                
            position = self.symbolTable.addIdentifier(token)
            self.PIF.append((token, position))
            self.index += len(token) + 1 # for the space 

    def treatAsSeparator(self,token):
        for separator in self.separators:
            if ( token == separator) :
                self.PIF.append((token, (-1, -1)))
                self.index  =  self.index + 2


    def treatAsOperator(self, token) :
        for operator in self.operators:
            if ( token == operator) :
                self.PIF.append((token, (-1, -1)))
                self.index  =  self.index + 2

    def treatAsIntConstant ( self, token):
        regex_for_int_constant = re.compile(r'^([+-]?[1-9][0-9]*|0)')
        matcher = regex_for_int_constant.match(token)
        if matcher:
            position = self.symbolTable.addIntConstant(int(token))
            self.PIF.append((token, position))

    def treatAsStringConstant( self, token ):
        regex_for_string_constant = re.compile(r'^"[a-zA-Z0-9_ ?:*^+=.!]*"')
        matcher = regex_for_string_constant.match(token)
        
    









    def treat_from_token_list(self):
        possible_token = self.program[self.index:].split(" ")[0]
        for reserved_token in self.reservedWords:
            if possible_token.startswith(reserved_token):
                regex = r'^[A-Za-z0-9_]*' + re.escape(reserved_token) + r'[A-Za-z0-9_]+'
                if re.match(regex, possible_token):
                    return False
                self.index += len(reserved_token)
                self.PIF.append((reserved_token, (-1, -1)))
                return True
        for token in self.tokens:
            if possible_token == token or possible_token.startswith(token):
                self.index += len(token)
                self.PIF.append((token, (-1, -1)))
                return True
        return False

    def next_token(self):
        self.skip_spaces()
        self.skip_comments()
        if self.index == len(self.program):
            return
        if self.treat_identifier():
            return
        if self.treat_string_constant():
            return
        if self.treat_int_constant():
            return
        if self.treat_from_token_list():
            return
        raise ScannerException("Lexical error: invalid token at line " + str(self.currentLine) + ", index " + str(self.index))

    def scan(self, program_file_name):
        try:
            
            with open (rf"D:\uni\UniversityProjects\year3\S1\FLCD\L1\{program_file_name}.txt","r") as file:
                self.set_program(file.read())

            self.index = 0
            self.PIF = []
            identifiersHashTable = HashTable(20)
            intConstantHashTable = HashTable(20)
            stringConstantHashTable = HashTable(20)
            symbol_table = SymbolTable(20,identifiersHashTable,intConstantHashTable,stringConstantHashTable)
            self.symbolTable = symbol_table
            self.currentLine = 1
            while self.index < len(self.program):
                self.next_token()
            with open("PIF" + program_file_name.replace(".txt", ".out"), "w") as file_writer:
                for pair in self.PIF:

                    print (pair)
                    #file_writer.write(f"{pair[0]} -> ({pair[1][0]}, {pair[1][1]})\n")

            with open("ST" + program_file_name.replace(".txt", ".out"), "w") as file_writer:
                #file_writer.write(self.symbolTable.toString())
                pass
            print("Lexically correct")
        except (IOError, ScannerException) as e:
            print(str(e))
            print(self.PIF)

    def treatTokens(self, line) :
        tokens = line.split()
        for token in tokens :
            classifyToken(token)




    def classifyToken(self, token):

        if self.index == len(self.program):
            return
        if self.treat_identifier():
            return
        if self.treat_string_constant():
            return
        if self.treat_int_constant():
            return
        if self.treat_from_token_list():
            return
        """
        -identifier
        -int constant
        -string constant
        -operator
        -separator
        :param token: [description]
        """



