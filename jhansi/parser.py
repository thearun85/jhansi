from .lexer import lex, Token, TokenType

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Represents a Base node which can be extended by other classes
class Node:
    pass

# Represents a Number type
class Number(Node):
    def __init__(self, value: int) -> None:
        self.value: int = value

    def __repr__(self) -> str:
        return f"Number({self.value})"

# Represents an Arithmetic operation with a left and right operand
class BinOp(Node):
    def __init__(self, left: Node, op: str, right: Node) -> None:
        self.left: Node = left
        self.op: str = op
        self.right: Node = right

    def __repr__(self) -> str:
        return f"BinOp({self.left}, {self.op}, {self.right})"

# Represents a variable assignment with name and value
class Assign(Node):
    def __init__(self, name: str, value: Node) -> None:
        self.name: str = name
        self.value: Node = value

    def __repr__(self) -> str:
        return f"Assign({self.name}, {self.value})"

class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        "Initialize the parser with the tokens and point to first token."
        self.tokens: list[Token] = tokens
        self.pos: int = 0
        logger.info(f"[Jhansi] Parser initialized with {tokens} and {self.pos}")

    def peek(self) -> Token:
        "Return the first token"
        return self.tokens[self.pos]

    def peek_next(self) -> Token:
        return self.tokens[self.pos+1]

    def eat(self, kind: TokenType) -> Token:
        "Return the first token and point to the next."
        tok = self.peek()
        if tok.kind != kind:
            raise SyntaxError(f"[Jhansi] Expected {kind}, got {tok.kind}")
        self.pos+=1
        return tok

    def parse_statement(self) -> Node:
        if self.peek().kind == TokenType.IDENT and self.peek_next().kind == TokenType.EQUAL:
            name = str(self.eat(TokenType.IDENT).value)
            self.eat(TokenType.EQUAL)
            value = self.parse_expr()
            return Assign(name, value)
        else:
            return self.parse_expr()
        
    def parse_expr(self) -> Node:
        "Parse an expression, anything which is not a statement (which has no assignment)"
        return self.parse_addition()

    def parse_addition(self) -> Node:
        "Return a BinOp node with the left operand, operator and the right operand"
        left = self.parse_multiply()
        while self.peek().kind in (TokenType.PLUS, TokenType.MINUS):
            op = str(self.eat(self.peek().kind).value)
            right = self.parse_multiply()
            left = BinOp(left, op, right)
        return left

    def parse_multiply(self) -> Node:
        "Return a BinOp node with the left operand, operator and the right operand"
        left = self.parse_primary()
        while self.peek().kind in (TokenType.STAR, TokenType.SLASH):
            op = str(self.eat(self.peek().kind).value)
            right = self.parse_primary()
            left = BinOp(left, op, right)
        return left

    def parse_primary(self) -> Node:
        "Return a Number Node."
        tok = self.peek()
        if tok.kind == TokenType.INT:
            self.eat(TokenType.INT)
            return Number(int(tok.value))
        elif tok.kind == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.parse_expr()
            self.eat(TokenType.RPAREN)
            return node
        else:
            raise SyntaxError(f"[Jhansi] Unexpected Token: {tok.kind}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        src = sys.argv[1]
    else:
        src = "3+4"
    tokens = lex(src)
    logger.info(f"[Jhansi] Tokens List -> {tokens}\n")
    p = Parser(tokens)
    logger.info(f"[Jhansi] Parsed Nodes -> {p.parse_statement()}\n")
