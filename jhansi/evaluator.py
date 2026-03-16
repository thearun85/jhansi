from .ast_nodes import Node, Number, BinaryOp

def evaluate(node: Node) -> int:
    """Process the operation and return the result."""
    if isinstance(node, Number):
        "Return the integer"
        return int(node.value)

    elif isinstance(node, BinaryOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
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
    
    else:
        raise SyntaxError(f"[Jhansi] Evaluator: unknown node type: {type(node.__class__)}")
