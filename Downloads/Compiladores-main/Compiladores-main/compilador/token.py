

class Token:
    TK_IDENTIFIER  = 'TK_IDENTIFIER'
    TK_NUMBER      = 'TK_NUMBER'
    TK_OPERATOR    = 'TK_OPERATOR'
    TK_OTHER       = 'TK_OTHER'
    TK_ASSIGN      = 'TK_ASSIGN'
    TK_FLOAT       = 'TK_FLOAT'
    TK_ERROR       = 'TK_ERROR'
    TK_STRING      = 'RW_STRING'

    reservedWord = {
        'main': "RW_MAIN",
        'return': "RW_RETURN",
        "function": "RW_FN",
        "if": "RW_IF",
        "elif": "RW_ELSEIF",
        "else": "RW_ELSE",
        "print": "RW_PRINT",
        "input": "RW_INPUT",
        "void": "RW_VOID",
        "float": "RW_FLOAT",
        "int": "RW_INT",
        "char": "RW_CHAR",
        "bool": "RW_BOOL",
        "string": "RW_STRING",
        "while": "RW_WHILE",
        "true": "RW_TRUE",
        "false": "RW_FALSE",
        "for": "RW_FOR",
        "break": "RW_BREAK",
        "array": "RW_ARRAY",
        "not": "OPR_NOT",
        "or": "OPR_OR",
        "and": "OPR_AND"
    }

    tokenCategory = {
        'TK_IDENTIFIER': 0,
        'TK_NUMBER': 1,
        'TK_OPERATOR': 2,
        'TK_OTHER': 3,
        'TK_ASSIGN': 4,
        'TK_FLOAT': 5,
        'TK_ERROR': 6,
        'RW_MAIN': 7,
        'RW_RETURN': 8,
        'RW_FN': 9,
        'RW_IF': 10,
        'RW_ELSEIF': 11,
        'RW_ELSE': 12,
        'RW_PRINT':13,
        'RW_INPUT':14,
        'RW_VOID':15,
        'RW_FLOAT':16,
        'RW_INT':17,
        'RW_CHAR':18,
        'RW_BOOL':19,
        'RW_STRING':20,
        'RW_WHILE':21,
        'RW_TRUE':22,
        'RW_FALSE':23,
        'RW_FOR':24,
        'RW_BREAK':25,
        'RW_ARRAY':26,
        'OPR_NOT':27,
        'OPR_OR':28,
        'OPR_AND':29,
    }

    def __init__(self, nameType, lexeme, line, column) -> None:
        self.__nameType = nameType
        self.__type = self.tokenCategory[nameType]
        self.__lexema = lexeme
        self.__line = line
        self.__column = column

    def __str__(self) -> str:
        return '%s[%04d, %04d] (%04d, %20s) (%s)' % (' '*14,self.__line,self.__column,self.__type, self.__nameType, self.__lexema)

    def getType(self) -> int:
        return self.__type

    def getNameType(self) -> str:
        return self.__nameType

    def getLexema(self) -> str:
        return self.__lexema

    def getLine(self) -> str:
        return self.__line

    def getColumn(self) -> str:
        return self.__column