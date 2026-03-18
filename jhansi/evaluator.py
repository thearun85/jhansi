from .ast_nodes import Node, Number, BinaryOp, UnaryOp, Assign, Var, VarDecl

class Evaluator():
    def __init__(self) -> None:
        # Symbols table to store all the variable definitions
        self.symbols: dict[str, int] = {}
        
    def evaluate(self, node: Node) -> int:
        """Process the operation and return the result."""

        if isinstance(node, VarDecl):
            print(f"node is {node}")
            if node.expr is None:
                self.symbols[node.name] = 0
            else:
                self.symbols[node.name] = self.evaluate(node.expr)
        
        elif isinstance(node, Number):
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
            return result
        elif isinstance(node, Var):
            try:
                return self.symbols[node.name]
            except KeyError:
                raise NameError(f"[Jhansi] Evaluator: undeclared variable '{node.name}'")
        else:
            raise SyntaxError(f"[Jhansi] Evaluator: unknown node type: {type(node).__name__}")
