import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from .token import Token, TokenType
from .ast_nodes import Node, Number, BinaryOp, UnaryOp
class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens: list[Token] = tokens
        self.pos: int = 0 # Start at the first token

    def peek(self) -> Token:    
        "Return the next available token"
        return self.tokens[self.pos]

    def eat(self, kind: TokenType) -> Token:
        "Consume the next available token and return it, if it matches the expected kind"
        tok = self.peek()
        if tok.kind != kind:
            logger.error(f"[Jhansi] Parser: Expected: {kind}, got {tok.kind}")
            raise SyntaxError(f"[Jhansi] Parser: Expected: {kind}, got {tok.kind}")
        self.pos+=1
        return tok

    def parse_expr(self) -> Node:
        """Process expressions on a line. Anything which doesn't have an assignment entitles for an expression"""
        return self.parse_add_sub()

    def parse_add_sub(self) -> Node:
        """Process the expression left to right. It expects two operands and an operator in between them. It will exit and return the resultant node when the operators exhaust."""
        left = self.parse_mul_div()
        while self.peek().kind in (TokenType.PLUS, TokenType.MINUS):
            op = str(self.eat(self.peek().kind).value)
            right = self.parse_mul_div()
            # Build the BinaryOp Node with 2 operands and an operator
            left = BinaryOp(left, op, right)
        return left

    def parse_mul_div(self) -> Node:
        """Process the expression left to right. It expects two operands and an operator in between them. It will exit and return the resultant node when the operators exhaust."""
        left = self.parse_unary()
        while self.peek().kind in (TokenType.STAR, TokenType.SLASH):
            op = str(self.eat(self.peek().kind).value)
            right = self.parse_unary()
            left = BinaryOp(left, op, right)

        return left

    def parse_unary(self) -> Node:
        if self.peek().kind == TokenType.MINUS:
            self.eat(TokenType.MINUS)
            right = self.parse_unary()
            return UnaryOp('-', right)
        return self.parse_token()
    
    def parse_token(self) -> Node:
        """This is the innermost leaf node. It deals with the basic operand nodes like numbers and variables."""
        tok = self.peek()
        if tok.kind == TokenType.INT:
            self.eat(TokenType.INT)
            return Number(int(tok.value))

        elif self.peek().kind == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            expr = self.parse_expr()
            self.eat(TokenType.RPAREN)
            return expr

        logger.error(f"[Jhansi] Parser: Unexpected Token: {tok.kind}")
        raise SyntaxError(f"[Jhansi] Parser: Unexpected Token: {tok.kind}")
