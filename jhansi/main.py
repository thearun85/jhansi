from .lexer import Lexer
from .parser import Parser
from .evaluator import evaluate

def run(src: str) -> None:
    tokens = Lexer(src).tokenize()
    
    print(f"[Jhansi] Tokens List -> \n{tokens}")

    node = Parser(tokens).parse_token()
    print(f"[Jhansi] Node is ->\n{node}")

    result = evaluate(node)
    print(f"[Jhansi] Result is {result}")

if __name__ == '__main__':
    import sys
    src = sys.argv[1] if len(sys.argv) > 1 else "3+4"
    run(src)
