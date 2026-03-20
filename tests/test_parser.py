from jhansi.token import TokenType, Token
from jhansi.parser import Parser
from jhansi.ast_nodes import Number, Boolean, Char, BinaryOp, UnaryOp, Assign, Var, VarDecl, If
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

def test_parse_token_basic_char_literal() -> None:
    tokens = [Token(TokenType.CHAR_LIT, "a"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_token()
    assert node is not None
    assert isinstance(node, Char)

def test_parse_token_escape_char_literal() -> None:
    tokens = [Token(TokenType.CHAR_LIT, "\0"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_token()
    assert node is not None
    assert isinstance(node, Char)

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

def test_parse_compare_gt() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.GT, '+'), Token(TokenType.INT_LIT, 7), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, BinaryOp)

def test_parse_compare_gteq() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.GTEQ, '+'), Token(TokenType.INT_LIT, 7), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, BinaryOp)

def test_parse_compare_lt() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.LT, '+'), Token(TokenType.INT_LIT, 7), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, BinaryOp)

def test_parse_compare_lteq() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.LTEQ, '+'), Token(TokenType.INT_LIT, 7), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, BinaryOp)

def test_parse_compare_eqeq() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.EQEQ, '+'), Token(TokenType.INT_LIT, 7), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, BinaryOp)

def test_parse_compare_bangeq() -> None:
    tokens = [Token(TokenType.INT_LIT, 5), Token(TokenType.BANGEQ, '+'), Token(TokenType.INT_LIT, 7), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_expr()
    assert node is not None
    assert isinstance(node, BinaryOp)
        
def test_parse_identifier() -> None:
    tokens = [Token(TokenType.IDENT, 'x'), Token(TokenType.EQUAL, '='),Token(TokenType.INT_LIT, '100'), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, Assign)

def test_parse_vardecl_int_with_no_assignment() -> None:
    tokens = [Token(TokenType.VAR, 'var'), Token(TokenType.IDENT, 'x'), Token(TokenType.INT, 'int'), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, VarDecl)

def test_parse_vardecl_int_with_assignment() -> None:
    tokens = [Token(TokenType.VAR, 'var'), Token(TokenType.IDENT, 'x'), Token(TokenType.INT, 'int'), Token(TokenType.EQUAL, "="), Token(TokenType.INT_LIT, "100"), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, VarDecl)

def test_parse_vardecl_bool_with_no_assignment() -> None:
    tokens = [Token(TokenType.VAR, 'var'), Token(TokenType.IDENT, 'x'), Token(TokenType.BOOL, 'bool'), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, VarDecl)

def test_parse_vardecl_bool_with_assignment() -> None:
    tokens = [Token(TokenType.VAR, 'var'), Token(TokenType.IDENT, 'x'), Token(TokenType.BOOL, 'bool'), Token(TokenType.EQUAL, "="), Token(TokenType.TRUE, "true"), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, VarDecl)

def test_parse_vardecl_char_with_no_assignment() -> None:
    tokens = [Token(TokenType.VAR, 'var'), Token(TokenType.IDENT, 'x'), Token(TokenType.CHAR, 'char'), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, VarDecl)

def test_parse_vardecl_char_with_assignment() -> None:
    tokens = [Token(TokenType.VAR, 'var'), Token(TokenType.IDENT, 'x'), Token(TokenType.CHAR, 'char'), Token(TokenType.EQUAL, "="), Token(TokenType.CHAR_LIT, "'a'"), Token(TokenType.SEMI, ";"), Token(TokenType.EOF, "")]
    node = Parser(tokens).parse_statement()
    assert node is not None
    assert isinstance(node, VarDecl)

def test_parse_simple_if_cond() -> None:
    tokens = [Token(TokenType.IF, 'IF'), Token(TokenType.LPAREN, '('),Token(TokenType.TRUE, 'true'), Token(TokenType.RPAREN, ')'), Token(TokenType.LBRACE, "{"), Token(TokenType.VAR, "var"), Token(TokenType.IDENT, 'x'), Token(TokenType.INT, 'int'),Token(TokenType.SEMI, ";"), Token(TokenType.RBRACE, "}"), Token(TokenType.EOF, "")]
    nodes = Parser(tokens).parse_program()
    assert len(nodes) == 1
    assert isinstance(nodes[0], If)
    
def test_parse_raise_syntax_error() -> None:
    tokens = [Token(TokenType.EOF, "")]
    with pytest.raises(SyntaxError):
        node = Parser(tokens).parse_token()
