from .ast_nodes import Node, Number

def evaluate(node: Node) -> int:
    if isinstance(node, Number):
        return int(node.value)

    raise SyntaxError(f"[Jhansi] Evaluator: unknown node type: {type(node.__class__)}")
