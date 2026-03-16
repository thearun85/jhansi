from jhansi.token import TokenType
from jhansi.lexer import Lexer
import pytest

def test_empty_source() -> None:
    src = "   "
    token = Lexer(src).tokenize()
    assert token is not None
    assert len(token) == 1
    assert token[0].kind == TokenType.EOF

def test_token_is_int() -> None:
    src = "345"
    token = Lexer(src).tokenize()
    assert token is not None
    assert len(token) == 2
    assert token[0].kind == TokenType.INT
    assert token[0].value == 345

def test_invalid_character_raises_syntax_error() -> None:
    src = "123 $ 456"
    with pytest.raises(SyntaxError, match=r"unknown character: \$"):
        Lexer(src).tokenize()

def test_invalid_character_at_start() -> None:
    src = "$123456"
    with pytest.raises(SyntaxError, match=r"unknown character: \$"):
        Lexer(src).tokenize()

def test_arithmetic_op_success() -> None:
    src = "+-*/" # Arithmetic operations
    tokens = Lexer(src).tokenize()
    assert tokens is not None
    assert len(tokens) == 5
    assert tokens[0].kind == TokenType.PLUS
    assert tokens[1].kind == TokenType.MINUS
    assert tokens[2].kind == TokenType.STAR
    assert tokens[3].kind == TokenType.SLASH

def test_expression_wrapper() -> None:
    src = "()"
    tokens = Lexer(src).tokenize()
    assert tokens is not None
    assert len(tokens) == 3
    assert tokens[0].kind == TokenType.LPAREN
    assert tokens[1].kind == TokenType.RPAREN

def test_unary() -> None:
    src = "-3" # Arithmetic operations
    tokens = Lexer(src).tokenize()
    assert tokens is not None
    assert len(tokens) == 3
    assert tokens[0].kind == TokenType.MINUS
    assert tokens[1].kind == TokenType.INT
    assert tokens[2].kind == TokenType.EOF
