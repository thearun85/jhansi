from enum import Enum, auto
from dataclasses import dataclass

# Definition for supported Token Types
class TokenType(Enum):

    INT = auto() # Represents a digit
    
    PLUS = auto() # Addition

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
        elif c == '+':
            tokens.append(Token(TokenType.PLUS, c))
            i+=1
        elif c == '(':
            tokens.append(Token(TokenType.LPAREN, c))
            i+=1
        elif c == ')':
            tokens.append(Token(TokenType.RPAREN, c))
            i+=1
        else:
            print(f"[Jhansi] Unsupported Token: '{c}'")
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
    print(f"[Jhansi] Tokens list -> {tokens}")
