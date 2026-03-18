from jhansi.token import TokenType, Token
from jhansi.parser import Parser
from jhansi.ast_nodes import Number, Boolean, BinaryOp, UnaryOp, Assign, Var, VarDecl
import pytest
import re

def test_init_parser() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.EOF, "")]
    p = Parser(tokens)
    assert p.tokens == tokens
    assert p.pos == 0

def test_peek_success() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.EOF, "")]
    p = Parser(tokens)
    assert p.peek().kind == TokenType.INT_LIT

def test_eat_success() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.EOF, "")]
    p = Parser(tokens)
    assert p.peek().kind == TokenType.INT_LIT
    assert p.eat(TokenType.INT_LIT).kind == TokenType.INT_LIT
    assert p.peek().kind == TokenType.EOF

def test_eat_raise_syntax_error() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.EOF, "")]
    p = Parser(tokens)
    with pytest.raises(SyntaxError):
        assert p.peek().kind == TokenType.INT_LIT
        assert p.eat(TokenType.EOF)

def test_eat_raise_error_message() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.EOF, "")]
    p = Parser(tokens)
    msg = "[Jhansi] Parser: Expected: EOF, got INT_LIT"
    with pytest.raises(SyntaxError, match=re.escape(msg)):
        assert p.peek().kind == TokenType.INT_LIT
        assert p.eat(TokenType.EOF)

def test_parse_token_int() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_token()
    assert node is not None
    assert isinstance(node, Number)

def test_parse_token_bool_true() -> None:
    tokens = [Token(TokenType.TRUE, "true"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_token()
    assert node is not None
    assert isinstance(node, Boolean)

def test_parse_token_bool_false() -> None:
    tokens = [Token(TokenType.FALSE, "false"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_token()
    assert node is not None
    assert isinstance(node, Boolean)


def test_parse_addition() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.PLUS, '+'), Token(TokenType.INT_LIT, 7), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, BinaryOp)

def test_parse_subtraction() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.MINUS, '-'), Token(TokenType.INT_LIT, 7), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, BinaryOp)

def test_parse_multiply() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.STAR, '*'), Token(TokenType.INT_LIT, 7), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, BinaryOp)

def test_parse_divide() -> None:
    tokens = [Token(TokenType.INT_LIT, 10), Token(TokenType.SLASH, '/'), Token(TokenType.INT_LIT, 5), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, BinaryOp)

def test_parse_unary() -> None:
    tokens = [Token(TokenType.MINUS, '-'), Token(TokenType.INT_LIT, '100'), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, UnaryOp)

def test_parse_identifier() -> None:
    tokens = [Token(TokenType.IDENT, 'x'), Token(TokenType.EQUAL, '='),Token(TokenType.INT_LIT, '100'), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, Assign)

def test_parse_vardeclint_with_no_assignment() -> None:
    tokens = [Token(TokenType.VAR, 'var'), Token(TokenType.IDENT, 'x'), Token(TokenType.INT, 'int'), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, VarDecl)

def test_parse_vardeclint_with_assignment() -> None:
    tokens = [Token(TokenType.VAR, 'var'), Token(TokenType.IDENT, 'x'), Token(TokenType.INT, 'int'), Token(TokenType.EQUAL, "="), Token(TokenType.INT_LIT, "100"), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, VarDecl)

def test_parse_vardeclbool_with_no_assignment() -> None:
    tokens = [Token(TokenType.VAR, 'var'), Token(TokenType.IDENT, 'x'), Token(TokenType.BOOL, 'bool'), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, VarDecl)

def test_parse_vardeclbool_with_assignment() -> None:
    tokens = [Token(TokenType.VAR, 'var'), Token(TokenType.IDENT, 'x'), Token(TokenType.BOOL, 'bool'), Token(TokenType.EQUAL, "="), Token(TokenType.TRUE, "true"), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, VarDecl)
    
def test_parse_raise_syntax_error() -> None:
    tokens = [Token(TokenType.EOF, "")]
    with pytest.raises(SyntaxError):
        node = Parser(tokens).parse_token()
