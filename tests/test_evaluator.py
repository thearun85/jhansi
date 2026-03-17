from jhansi.ast_nodes import Node, Number, BinaryOp, UnaryOp, Assign
from jhansi.evaluator import Evaluator

import pytest

def test_evaluate_number() -> None:
    node = Number(5)
    result = Evaluator().evaluate(node)
    assert result == 5

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
    
def test_evaluate_raise_syntax_error() -> None:
    node = Node()
    with pytest.raises(SyntaxError):
        Evaluator().evaluate(node)
