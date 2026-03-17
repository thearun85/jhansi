from .ast_nodes import Node, Number, BinaryOp, UnaryOp, Assign

class Evaluator():
    def __init__(self) -> None:
        # Symbols table to store all the variable definitions
        self.symbols: dict[str, int] = {}
        
    def evaluate(self, node: Node) -> int:
        """Process the operation and return the result."""
        if isinstance(node, Number):
            "Return the integer"
            return int(node.value)

        elif isinstance(node, BinaryOp):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            match node.op:
                case '+':
                    return int(left+right)
                case '-':
                    return int(left-right)
                case '*':
                    return int(left*right)
                case '/':
                    return int(left//right) # Integer division
            raise SyntaxError(f"[Jhansi] Evaluator: unknown operator: {node.op}") 
        elif isinstance(node, UnaryOp):
            right = self.evaluate(node.right)
            return -int(right)
        elif isinstance(node, Assign):
            result = self.evaluate(node.expr)
            self.symbols[node.name] = result
        else:
            raise SyntaxError(f"[Jhansi] Evaluator: unknown node type: {type(node.__class__)}")
