from jhansi.ast_nodes import Node, Number, BinaryOp
from jhansi.evaluator import evaluate

import pytest

def test_evaluate_number() -> None:
    node = Number(5)
    result = evaluate(node)
    assert result == 5

def test_evaluate_addition() -> None:
    node = BinaryOp(Number(5), '+', Number(7))
    result = evaluate(node)
    assert result == 12

def test_evaluate_subtraction() -> None:
    node = BinaryOp(Number(7), '-', Number(5))
    result = evaluate(node)
    assert result == 2

def test_evaluate_multiplication() -> None:
    node = BinaryOp(Number(7), '*', Number(5))
    result = evaluate(node)
    assert result == 35

def test_evaluate_division() -> None:
    node = BinaryOp(Number(10), '/', Number(5))
    result = evaluate(node)
    assert result == 2
    
def test_evaluate_raise_syntax_error() -> None:
    node = Node()
    with pytest.raises(SyntaxError):
        evaluate(node)
