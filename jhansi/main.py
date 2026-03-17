from .lexer import Lexer
from .parser import Parser
from .evaluator import Evaluator

def run(src: str) -> None:
    tokens = Lexer(src).tokenize()
    
    print(f"[Jhansi] Tokens List -> \n{tokens}")

    nodes = Parser(tokens).parse_program()
    print(f"[Jhansi] Node is ->\n{nodes}")

    e = Evaluator()
    for node in nodes:
        result = e.evaluate(node)
        print(f"[Jhansi] Result is {result}")

    for k, v in e.symbols.items():
        print(f"key is {k} and value is {v}")

if __name__ == '__main__':
    import sys
    src = sys.argv[1] if len(sys.argv) > 1 else "3+4"
    run(src)
