from enum import Enum, auto
from dataclasses import dataclass

# Maintain a list of tokens supported by the language
class TokenType(Enum):

    # Data types
    INT = auto() # Integer

    EOF = auto() # End of File

@dataclass
class Token:
    "Represents individual logical characters from the source file"
    kind: TokenType
    value: str|int

