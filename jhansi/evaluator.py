from .lexer import lex
from .parser import Parser, Node, Number, BinOp, Assign, Var, IF
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
            elif node.op == '>':
                return left>right
            elif node.op == '>=':
                return left>=right
            elif node.op == '<':
                return left<right
            elif node.op == '<=':
                return left<=right
            elif node.op == '==':
                return left==right
            elif node.op == '!=':
                return left!=right # Integer division

            else:
                raise SyntaxError(f"[Jhansi] Unsupported operator : {node.op}")
        elif isinstance(node, Assign):
            name = node.name
            result = self.evaluate(node.value)
            self.symbols[name] = result
            return result
            
        elif isinstance(node, Var):
            try:
                result = self.symbols[node.name]
                return result
            except KeyError:
                raise NameError(f"[Jhansi] Undeclared variable '{node.name}'")
                
        elif isinstance(node, IF):
            condition = self.evaluate(node.condition)
            if condition:
                nodes = node.body
                for node in nodes:
                    result = self.evaluate(node)
                return result
            else:
                if node.else_body:
                    for node in node.else_body:
                        result = self.evaluate(node)
                    return result
                else:
                    return 0
        else:
            raise SyntaxError(f"[Jhansi] Unsupported Node: {node}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        src = sys.argv[1]
    else:
        src = "3+4"
    tokens = lex(src)
    p = Parser(tokens)
    nodes = p.parse_program()
    logger.info(f"[Jhansi] Parsed node is {nodes}\n")
    e = Evaluator()
    for node in nodes:
        logger.info(f"[Jhansi] Evaluated result is {e.evaluate(node)}")
    logger.info(f"[Jhansi] Symbol table is populated as:")
    for k, v in e.symbols.items():
        logger.info(f"[Jhansi] {k}:{v}")
