from .lexer import lex, Token, TokenType

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

class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        "Initialize the parser with the tokens and point to first token."
        self.tokens: list[Token] = tokens
        self.pos: int = 0

    def peek(self) -> Token:
        "Return the first token"
        return self.tokens[self.pos]

    def eat(self, kind: TokenType) -> Token:
        "Return the first token and point to the next."
        tok = self.peek()
        if tok.kind != kind:
            raise SyntaxError(f"[Jhansi] Expected {kind}, got {tok.kind}")
        self.pos+=1
        return tok
        
    def parse_expr(self) -> Node:
        "Parse an expression, anything which is not a statement (which has no assignment)"
        node: Node = Node()
        while self.peek().kind != TokenType.EOF:
            # Loop until end of file
            node = self.parse_addition()
        return node

    def parse_addition(self) -> Node:
        "Return a BinOp node with the left operand, operator and the right operand"
        left = self.parse_primary()
        while self.peek().kind == TokenType.PLUS:
            op = str(self.eat(TokenType.PLUS).value)
            right = self.parse_primary()
            left = BinOp(left, op, right)
        return left

    def parse_primary(self) -> Node:
        "Return a Number Node."
        tok = self.peek()
        if tok.kind == TokenType.INT:
            self.eat(TokenType.INT)
            return Number(int(tok.value))
        else:
            raise SyntaxError(f"[Jhansi] Unexpected Token: {tok.kind}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        src = sys.argv[1]
    else:
        src = "3+4"
    tokens = lex(src)
    print(f"[Jhansi] Tokens List -> {tokens}\n")
    p = Parser(tokens)
    print(f"[Jhansi] Parsed Nodes -> {p.parse_expr()}\n")
