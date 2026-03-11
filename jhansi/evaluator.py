from .lexer import lex
from .parser import Parser, Node, Number, BinOp
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Evaluate a nested node and return the final result
def evaluate(node: Node) -> int:
    
    if isinstance(node, Number):
        return int(node.value)
    elif isinstance(node, BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
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
    node = p.parse_expr()
    logger.info(f"[Jhansi] Parsed node is {node}\n")
    logger.info(f"[Jhansi] Evaluated result is {evaluate(node)}")
