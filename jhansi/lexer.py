import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from .token import TokenType, Token



class Lexer:
    def __init__(self, source: str) -> None:    
        "Initialize the lexer with the source and the first index position in the program"
        self.source: str = source
        self.pos = 0

    def tokenize(self) -> list[Token]:
        tokens: list[Token] = [] # Hold the tokens
        "Walk through the program, validate and convert it into a list of supported tokens"

        while self.pos < len(self.source):
            c = self.source[self.pos]
            if c.isspace():
                self.pos+=1 # Ignore whitespace
            
            elif c.isdigit():
                # Retrieve and tokenize an integer. Float is not supported currently
                start = self.pos
                self.pos+=1
                while self.pos < len(self.source) and self.source[self.pos].isdigit():
                    self.pos+=1
                    
                tokens.append(Token(TokenType.INT, int(self.source[start: self.pos])))
            else:
                logger.error(f"[Jhansi] Lexer: unknown character: {c}")
                raise SyntaxError(f"[Jhansi] Lexer: unknown character: {c}")
                
        tokens.append(Token(TokenType.EOF, ""))
        return tokens


