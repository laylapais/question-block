

class Symbols:
    def isChar(self, c: str) -> bool:
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

    def isNumber(self, c: str) -> bool:
        return c >= '0' and c <= '9'

    def isOperator(self, c: str) -> bool:
        return c == '>' or c == '<' or c == '=' or c == '!' or c == '+' or c == '-' or c == '%'

    def ignore(self, c: str) -> bool:
        return c == '\t' or c == '\n' or c == ' ' or c == '\r' or c == '\t' or c == '\0'
    
    def other(self, c: str) -> bool:
        return c =='(' or c == ')' or c == '{' or c == '}' or c == '[' or c == ']' or c == '.' or c == ','

