from jhansi.ast_nodes import Node, Number, Boolean, BinaryOp, UnaryOp, Assign, Var, VarDecl
from jhansi.evaluator import Evaluator

import pytest

def test_evaluate_number() -> None:
    node = Number(5)
    result = Evaluator().evaluate(node)
    assert result == 5

def test_evaluate_bool_true() -> None:
    node = Boolean(True)
    result = Evaluator().evaluate(node)
    assert result == True

def test_evaluate_bool_false() -> None:
    node = Boolean(False)
    result = Evaluator().evaluate(node)
    assert result == False

def test_evaluate_addition() -> None:
    node = BinaryOp(Number(5), '+', Number(7))
    result = Evaluator().evaluate(node)
    assert result == 12

def test_evaluate_subtraction() -> None:
    node = BinaryOp(Number(7), '-', Number(5))
    result = Evaluator().evaluate(node)
    assert result == 2

def test_evaluate_multiplication() -> None:
    node = BinaryOp(Number(7), '*', Number(5))
    result = Evaluator().evaluate(node)
    assert result == 35

def test_evaluate_division() -> None:
    node = BinaryOp(Number(10), '/', Number(5))
    result = Evaluator().evaluate(node)
    assert result == 2

def test_evaluate_unary() -> None:
    node = UnaryOp('-', Number(10))
    result = Evaluator().evaluate(node)
    assert result == -10

def test_evaluate_assign() -> None:
    node = Assign('x', Number(10))
    e = Evaluator()
    result = e.evaluate(node)
    assert len(e.symbols) > 0

def test_evaluate_vardeclint_with_no_assignment() -> None:
    node = VarDecl('x', "int", None)
    e = Evaluator()
    result = e.evaluate(node)
    assert len(e.symbols) > 0
    assert e.symbols["x"] == 0

def test_evaluate_vardeclint_with_assignment() -> None:
    node = VarDecl('x', "int", Number(10))
    e = Evaluator()
    result = e.evaluate(node)
    assert len(e.symbols) > 0
    assert e.symbols["x"] == 10

def test_evaluate_vardeclbool_with_no_assignment() -> None:
    node = VarDecl('x', "bool", None)
    e = Evaluator()
    result = e.evaluate(node)
    assert len(e.symbols) > 0
    assert e.symbols["x"] == "false"

def test_evaluate_vardecl_with_assignment() -> None:
    node = VarDecl('x', "bool", Boolean(True))
    e = Evaluator()
    result = e.evaluate(node)
    assert len(e.symbols) > 0
    assert e.symbols["x"] == True
        
def test_evaluate_raise_syntax_error() -> None:
    node = Node()
    with pytest.raises(SyntaxError):
        Evaluator().evaluate(node)
