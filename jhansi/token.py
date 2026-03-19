from enum import IntEnum, auto
from dataclasses import dataclass

# Maintain a list of tokens supported by the language
class TokenType(IntEnum):

    # Literals
    INT_LIT = auto() # Integer
    CHAR_LIT = auto() # Char literal 'a' single character

    # Datatypes
    INT = auto()
    BOOL = auto()
    CHAR = auto()

    # Arithmetic operators
    # Addition and Subtraction are of the same precedence, so they can be processed left to right
    PLUS = auto() # Addition
    MINUS = auto() # Subtraction
    STAR = auto() # Multiplication
    SLASH = auto() # Division

    # Comparison operators
    GT = auto() # greater than >
    GTEQ = auto() # greater than or equal >=
    LT = auto() # less than <
    LTEQ = auto() # less than or equal <=
    EQEQ = auto() # same as ==
    BANGEQ = auto() # not equal !=

    # Declaration and Assignments
    IDENT = auto() # Variable names
    EQUAL = auto() # Variable assignments
    SEMI = auto() # statement seperator
    VAR = auto()
    TRUE = auto()
    FALSE = auto()

    
    # Code organizers
    LPAREN = auto() # (
    RPAREN = auto() # )

    EOF = auto() # End of File

# Language keywords
KEYWORDS: dict[str, TokenType] = {
    "var": TokenType.VAR,
    "int": TokenType.INT,
    "bool": TokenType.BOOL,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "char": TokenType.CHAR,
}

@dataclass
class Token:
    "Represents individual logical characters from the source file"
    kind: TokenType
    value: str|int

