from jhansi.token import TokenType, Token
from jhansi.parser import Parser
from jhansi.ast_nodes import Number
import pytest
import re

def test_init_parser() -> None:
    tokens = [Token(TokenType.INT, 5), Token(TokenType.EOF, "")]
    p = Parser(tokens)
    assert p.tokens == tokens
    assert p.pos == 0

def test_peek_success() -> None:
    tokens = [Token(TokenType.INT, 5), Token(TokenType.EOF, "")]
    p = Parser(tokens)
    assert p.peek().kind == TokenType.INT

def test_eat_success() -> None:
    tokens = [Token(TokenType.INT, 5), Token(TokenType.EOF, "")]
    p = Parser(tokens)
    assert p.peek().kind == TokenType.INT
    assert p.eat(TokenType.INT).kind == TokenType.INT
    assert p.peek().kind == TokenType.EOF

def test_eat_raise_syntax_error() -> None:
    tokens = [Token(TokenType.INT, 5), Token(TokenType.EOF, "")]
    p = Parser(tokens)
    with pytest.raises(SyntaxError):
        assert p.peek().kind == TokenType.INT
        assert p.eat(TokenType.EOF)

def test_eat_raise_error_message() -> None:
    tokens = [Token(TokenType.INT, 5), Token(TokenType.EOF, "")]
    p = Parser(tokens)
    msg = "[Jhansi] Parser: Expected: TokenType.EOF, got TokenType.INT"
    with pytest.raises(SyntaxError, match=re.escape(msg)):
        assert p.peek().kind == TokenType.INT
        assert p.eat(TokenType.EOF)

def test_parse_token_success() -> None:
    tokens = [Token(TokenType.INT, 5), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_token()
    assert node is not None
    assert isinstance(node, Number)

def test_parse_raise_syntax_error() -> None:
    tokens = [Token(TokenType.EOF, "")]
    with pytest.raises(SyntaxError):
        node = Parser(tokens).parse_token()
