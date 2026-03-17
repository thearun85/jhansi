from .lexer import Lexer



if __name__ == '__main__':
    import sys
    src = sys.argv[1] if len(sys.argv) > 1 else "x=1; y=2; z=x+y;"
    tokens = Lexer(src).tokenize()
    print(f"Token List -> {tokens}")
    nodes = Parser(tokens).parse_program()
