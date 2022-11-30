from token import Token
from symbols import Symbols

class Lexico:
    symbols_lex = Symbols()
    
    def __init__(self, filename) -> None:
        self.__content = ''
        self.__fileLines = self.readFile(filename)
        self.__state = 0
        self.__position = 0
        self.__column = 0
        self.__line = 0

    def readFile(self, filename) -> list:
        lines = []
        try:
            with open(filename) as f:
                lines = [line for line in f.readlines()]
            f.close()
        except:
            print('Error')

        return lines

    def readLines(self):
        for index, line in enumerate(self.__fileLines):
            self.__line = index
            self.__content = line

            if line[0] == ' ':
                self.startWithSpace()

            self.getToken()

            self.__position = 0
            self.__column = 0

    def startWithSpace(self):
        count = 0
        for ignore in self.__content:
            if ignore != ' ': break
            count += 1

        self.__column += count
                
    def getToken(self) -> Token:
        while self.__position < len(self.__content):
            current = self.__content[self.__position]
            self.__match(current)
            self.__next()
            

    def __match(self, current: str) -> Token:
        match self.__state:
            case 0:
                if self.symbols_lex.isChar(current):
                    self.__state = 1
                elif self.symbols_lex.isNumber(current):
                    self.__state = 2
                elif self.symbols_lex.isOperator(current):
                    self.__state = 3
                elif self.symbols_lex.other(current):
                    self.__state = 4
                elif current == '"':
                    self.__state = 6
            case 1:
                if not self.symbols_lex.isChar(current) and not self.symbols_lex.isNumber(current):
                    word = ''.join(self.__content[self.__column:self.__position]).strip()
                    if word in Token.reservedWord:
                        self.__createToken(Token.reservedWord[word])
                    else:
                        self.__createToken(Token.TK_IDENTIFIER)
            case 2:
                if(current == '.'):
                    self.__state = 5
                elif self.symbols_lex.isChar(current):
                    self.__next()
                    self.__createToken(Token.TK_ERROR) 
                elif not self.symbols_lex.isNumber(current):
                    self.__createToken(Token.TK_NUMBER)
                
            case 3:
                if not self.symbols_lex.isOperator(current):
                    self.__createToken(Token.TK_OPERATOR)
            case 4:
                self.__createToken(Token.TK_OTHER)
            case 5: 
                if self.symbols_lex.isOperator(current) or self.symbols_lex.ignore(current) or current == ';':
                    self.__createToken(Token.TK_FLOAT)
                elif  not self.symbols_lex.isNumber(current):
                    self.__next()
                    self.__createToken(Token.TK_ERROR)
            case 6:
                if current == '"':
                   self.__next()
                   self.__createToken(Token.TK_STRING)
                    

    def __createToken(self, type):
        word = ''.join(self.__content[self.__column:self.__position]).strip()
        token = Token(type,word,self.__line+1,self.__column+1)
        print(token)
        if not self.symbols_lex.ignore(self.__content[self.__position]):
            self.__column = self.__position
        else:
            self.__column = self.__position + 1

        self.__back()
        self.__state = 0

    def __next(self) -> str:
        self.__position += 1

    def __isEOF(self) -> bool:
        return self.__position == len(self.__content)
    
    def __back(self) -> None:
        self.__position -= 1


test = Lexico("file.txt")
test.readLines()

