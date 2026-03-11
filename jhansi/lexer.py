from enum import Enum, auto
from dataclasses import dataclass
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Definition for supported Token Types
class TokenType(Enum):

    # Datatypes
    INT = auto() # Represents a digit

    
    # Arithmetic operators
    PLUS = auto() # Addition
    MINUS = auto() # Subtraction
    STAR = auto() # Multiplication
    SLASH = auto() # Division

    # Comparison operators
    GT = auto()
    GTEQ = auto()
    LT = auto()
    LTEQ = auto()
    EQEQ = auto()
    BANGEQ = auto()

    IDENT = auto() # Variable identifiers or names
    
    # Assignments
    EQUAL = auto() # Assign a value to a variable or identifier
    SEMI = auto() #  Statement seperator
    
    # Code organizers
    LPAREN = auto() # ( 
    RPAREN = auto() # ) Used to enclose expressions

    EOF = auto() # End of File indicator

# Represents each individual token
@dataclass
class Token:
    kind: TokenType # Type of token
    value: str|int # It value

# Tokenizer - converts a program into a sequence of tokens
def lex(src: str) -> list[Token]:
    tokens: list[Token] = []
    i: int = 0 # Variable to loop through each character of the program
    while i < len(src): # Loop through the entire length of the program
        c = src[i]
        if c == ' ': # Check for whitespace and ignore
            i+=1
        elif c.isdigit(): # Check for presence of digit
            j=i
            while i < len(src) and src[i].isdigit():
            # Accumulate entire length of the digit
                i+=1
            tokens.append(Token(TokenType.INT, int(src[j:i])))
        elif c.isalpha(): # Check if character starts with an alphabet
            # Variable names or identifiers
            j=i
            while i < len(src) and src[i].isalnum():
            # Identifiers can contain alphanumerics
            # Accumulate entire length of the string
                i+=1
            tokens.append(Token(TokenType.IDENT, str(src[j:i])))
        # Arithmetic operation starts
        elif c == '+':
            tokens.append(Token(TokenType.PLUS, c))
            i+=1
        elif c == '-':
            tokens.append(Token(TokenType.MINUS, c))
            i+=1
        elif c == '*':
            tokens.append(Token(TokenType.STAR, c))
            i+=1
        elif c == '/':
            tokens.append(Token(TokenType.SLASH, c))
            i+=1
        # Arithmetic operation ends
        # Comparison operation starts
        elif c == '>':
            i+=1
            if src[i] == '=':
                tokens.append(Token(TokenType.GTEQ, '>='))
                i+=1
            else:
                tokens.append(Token(TokenType.GT, '>'))
        elif c == '<':
            i+=1
            if src[i] == '=':
                tokens.append(Token(TokenType.LTEQ, '<='))
                i+=1
            else:
                tokens.append(Token(TokenType.LT, '<'))
        elif c == '!':
            i+=1
            if src[i] == '=':
                tokens.append(Token(TokenType.BANGEQ, '!='))
                i+=1
        # Comparison operation ends
        elif c == '(':
            tokens.append(Token(TokenType.LPAREN, c))
            i+=1
        elif c == ')':
            tokens.append(Token(TokenType.RPAREN, c))
            i+=1
        elif c == '=':
            i+=1
            if src[i] == '=':
                tokens.append(Token(TokenType.EQEQ, '=='))
                i+=1
            else:
                tokens.append(Token(TokenType.EQUAL, '='))
        elif c == ';':
            tokens.append(Token(TokenType.SEMI, c))
            i+=1

        else:
            logger.error(f"[Jhansi] Unsupported Token: '{c}'")
            raise SyntaxError(f"[Jhansi] Unsupported Token: '{c}'")
    # Add an EOF indicator to the list of tokens
    tokens.append(Token(TokenType.EOF, ""))
    return tokens

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        src = sys.argv[1]
    else:
        src = "3+4"
    tokens = lex(src)
    logger.info(f"[Jhansi] Tokens list -> {tokens}")
