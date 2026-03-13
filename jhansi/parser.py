import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from .token import Token, TokenType
from .ast_nodes import Node, Number
class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens: list[Token] = tokens
        self.pos: int = 0 # Start at the first token

    def peek(self) -> Token:
        return self.tokens[self.pos]

    def eat(self, kind: TokenType) -> Token:
        tok = self.peek()
        if tok.kind != kind:
            logger.error(f"[Jhansi] Parser: Expected: {kind}, got {tok.kind}")
            raise SyntaxError(f"[Jhansi] Parser: Expected: {kind}, got {tok.kind}")
        self.pos+=1
        return tok

    def parse_token(self) -> Node:
        tok = self.peek()
        if tok.kind == TokenType.INT:
            self.eat(TokenType.INT)
            return Number(int(tok.value))

        logger.error(f"[Jhansi] Parser: Unexpected Token: {tok.kind}")
        raise SyntaxError(f"[Jhansi] Parser: Unexpected Token: {tok.kind}")
