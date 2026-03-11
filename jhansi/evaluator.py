from .lexer import lex
from .parser import Parser, Node, Number, BinOp

# Evaluate a nested node and return the final result
def evaluate(node: Node) -> int:
    
    if isinstance(node, Number):
        return int(node.value)
    elif isinstance(node, BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
        if node.op == '+':
            return left+right
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
    print(f"[Jhansi] Tokens List -> {tokens}\n")
    p = Parser(tokens)
    node = p.parse_expr()
    print(f"[Jhansi] Parsed node is {node}\n")
    print(f"[Jhansi] Evaluated result is {evaluate(node)}")
