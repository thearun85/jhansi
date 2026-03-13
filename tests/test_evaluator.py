from jhansi.ast_nodes import Number, Node
from jhansi.evaluator import evaluate

import pytest

def test_evaluate_success() -> None:
    node = Number(5)
    result = evaluate(node)
    assert result == 5

def test_evaluate_raise_syntax_error() -> None:
    node = Node()
    with pytest.raises(SyntaxError):
        evaluate(node)
