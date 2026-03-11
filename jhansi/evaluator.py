from .lexer import lex
from .parser import Parser, Node, Number, BinOp, Assign
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Evaluate a nested node and return the final result

class Evaluator:
    def __init__(self) -> None:
        self.symbols: dict[str, int] = {} # Symbol table to persist the variable values while executing a program
    def evaluate(self, node: Node) -> int:
        
        if isinstance(node, Number):
            return int(node.value)
        elif isinstance(node, BinOp):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if node.op == '+':
                return left+right
            elif node.op == '-':
                return left-right
            elif node.op == '*':
                return left*right
            elif node.op == '/':
                return left//right # Integer division
            else:
                raise SyntaxError(f"[Jhansi] Unsupported operator : {node.op}")
        elif isinstance(node, Assign):
            name = node.name
            result = self.evaluate(node.value)
            self.symbols[name] = result
            return result
        else:
            raise SyntaxError(f"[Jhansi] Unsupported Node: {node}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        src = sys.argv[1]
    else:
        src = "3+4"
    tokens = lex(src)
    logger.info(f"[Jhansi] Tokens List -> {tokens}\n")
    p = Parser(tokens)
    node = p.parse_statement()
    logger.info(f"[Jhansi] Parsed node is {node}\n")
    e = Evaluator()
    logger.info(f"[Jhansi] Evaluated result is {e.evaluate(node)}")
    logger.info(f"[Jhansi] Symbol table is populated as:")
    for k, v in e.symbols.items():
        logger.info(f"[Jhansi] {k}:{v}")
