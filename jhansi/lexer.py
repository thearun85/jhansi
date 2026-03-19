import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from .token import TokenType, Token, KEYWORDS



class Lexer:
    def __init__(self, source: str) -> None:    
        "Initialize the lexer with the source and the first index position in the program"
        self.source: str = source
        self.pos = 0

    def tokenize(self) -> list[Token]:
        tokens: list[Token] = [] # Hold the tokens
        "Walk through the program, validate and convert it into a list of supported tokens"

        while self.pos < len(self.source):
            c = self.source[self.pos]
            if c.isspace():
                self.pos+=1 # Ignore whitespace

            elif c.isalpha():
                # Retrieve and tokenize an IDENTIFIER.
                start = self.pos
                self.pos+=1
                while self.pos < len(self.source) and self.source[self.pos].isalnum():
                    self.pos+=1
                word = str(self.source[start: self.pos])
                token_type = KEYWORDS.get(word, TokenType.IDENT)
                
                tokens.append(Token(token_type, word))

            # Process char literal including escape sequences like newline, tab, \0, \, '
            elif c == "'":
                self.pos+=1
                if self.pos >= len(self.source):
                    raise SyntaxError(f"[Jhansi] Lexer: unterminated literal")
                c = self.source[self.pos]
                if c == '\\':
                    self.pos+=1
                    if self.pos >= len(self.source):
                        raise SyntaxError(f"[Jhansi] Lexer: unterminated escape sequence")
                    escape = self.source[self.pos]
                    match escape:
                        case 'n': c = '\n'
                        case 't': c = '\t'
                        case '0': c = '\0'
                        case '\\': c = '\\'
                        case "'": c = "'"
                        case _:
                            raise SyntaxError(f"[Jhansi] Lexer: unknown escape sequence: {escape}")
                self.pos+=1
                if self.pos >= len(self.source) or self.source[self.pos] != "'":
                    raise SyntaxError(f"[Jhansi] Lexer: unterminated literal")
                tokens.append(Token(TokenType.CHAR_LIT, c))
                self.pos+=1
                
            elif c == '=':
                self.pos+=1
                
                if self.pos < len(self.source) and self.source[self.pos] == '=':
                    tokens.append(Token(TokenType.EQEQ, '=='))
                    self.pos+=1
                else:
                    tokens.append(Token(TokenType.EQUAL, c))
                
            elif c == ';':
                tokens.append(Token(TokenType.SEMI, c))
                self.pos+=1

            elif c.isdigit():
                # Retrieve and tokenize an integer. Float is not supported currently
                start = self.pos
                self.pos+=1
                # Consume the entire length of the digit
                while self.pos < len(self.source) and self.source[self.pos].isdigit():
                    self.pos+=1
                    
                tokens.append(Token(TokenType.INT_LIT, int(self.source[start: self.pos])))
            # Arithmetic operation starts
            elif c == '+':
                tokens.append(Token(TokenType.PLUS, c))
                self.pos+=1
                
            elif c == '-':
                tokens.append(Token(TokenType.MINUS, c))
                self.pos+=1
                
            elif c == '*':
                tokens.append(Token(TokenType.STAR, c))
                self.pos+=1

            elif c == '/':
                tokens.append(Token(TokenType.SLASH, c))
                self.pos+=1

            elif c == '(':
                tokens.append(Token(TokenType.LPAREN, c))
                self.pos+=1

            elif c == ')':
                tokens.append(Token(TokenType.RPAREN, c))
                self.pos+=1


            # Arithmetic operation ends

            # Comparison operation starts
            elif c == '>':
                self.pos+=1
                if self.pos < len(self.source) and self.source[self.pos] == '=':
                    tokens.append(Token(TokenType.GTEQ, '>='))
                    self.pos+=1
                else:
                    tokens.append(Token(TokenType.GT, '>'))
            elif c == '<':
                self.pos+=1
                if self.pos < len(self.source) and self.source[self.pos] == '=':
                    tokens.append(Token(TokenType.LTEQ, '<='))
                    self.pos+=1
                else:
                    tokens.append(Token(TokenType.LT, '<'))
            elif c == '!':
                self.pos+=1
                if self.pos < len(self.source) and self.source[self.pos] == '=':
                    tokens.append(Token(TokenType.BANGEQ, '!='))
                    self.pos+=1
                else:
                    raise SyntaxError(f"[Jhansi] Lexer: unexpected character: '{c}'")

            # Comparison operations ends
            else:
                logger.error(f"[Jhansi] Lexer: unknown character: {c}")
                raise SyntaxError(f"[Jhansi] Lexer: unknown character: {c}")
                
        tokens.append(Token(TokenType.EOF, ""))
        return tokens


