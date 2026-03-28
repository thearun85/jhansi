from dataclasses import dataclass
from enum import IntEnum, auto

class TokenType(IntEnum):

    # -- Declarations & Definitions -----------------------------------------------------
    VAR         = auto() # 'var' - typed variable declaration, inside functions only
    CONST       = auto() # 'const' - compile-time constant, top-level only
    IDENT       = auto() # identifier - variable name, function name, struct name
    EQUAL       = auto() # '=' - assignment operator
    COLONEQUAL  = auto() # ':=' - short declaration: infers type from RHS
    SEMI        = auto() # ';' - statement seperator
    FUNC        = auto() # 'func' - function declaration
    STRUCT      = auto() # 'struct' - struct declaration (body deferred to V2)
    
    # -- Literals -----------------------------------------------------------------------
    INT_LIT     = auto() # integer literal - e.g. 0, 42, -1. value: int
    BOOL_LIT    = auto() # boolean literal - 'true' or 'false'. value: bool

    # -- Types --------------------------------------------------------------------------
    INT         = auto() # 'int' - signed integer type
    BOOL        = auto() # 'bool' - boolean type. not interchangeable with int
    VOID        = auto() # 'void' - return type only. not a value type
    
    # -- Arithmetic Operators -----------------------------------------------------------
    PLUS        = auto() # '+' - addition 
    MINUS       = auto() # '-' - subtraction
    STAR        = auto() # '*' - multiplication
    SLASH       = auto() # '/' - division
    PERCENT     = auto() # '%' - modulo

    # -- Comparison Operators -----------------------------------------------------------
    # All comparison operators produce type bool, not int.
    GT          = auto() # '>' - greater than
    GTEQ        = auto() # '>=' - greater than or equal to
    LT          = auto() # '<' - less than
    LTEQ        = auto() # '<=' - less than or equal to
    EQEQ        = auto() # '==' - equality
    BANGEQ      = auto() # '!=' - inequality

    # -- Logical Operators -------------------------------------------------------------
    # Operands must be type bool. sema rejects int operands.
    AND         = auto() # '&&' - logical and.
    OR          = auto() # '||' - logical or.
    BANG        = auto() # '!' - unary logical not 
    
    # -- Delimiters & Punctuation ------------------------------------------------------
    LPAREN      = auto() # '('
    RPAREN      = auto() # ')'
    LBRACE      = auto() # '{' - block open
    RBRACE      = auto() # '}' - block close
    COMMA       = auto() # ',' - parameter and argument seperator
    
    # -- Control Flow ------------------------------------------------------------------
    RETURN      = auto() # 'return' - returns a value from a function
    IF          = auto() # 'if' - conditional. condition must be bool
    ELSE        = auto() # 'else' - else branch or else-if chain
    FOR         = auto() # 'for' - loop. covers while-style and C-style

    # -- Meta --------------------------------------------------------------------------
    EOF         = auto() # end of token stream - signals parser to stop

# Maps source keywords to their TokenType.
# The lexer checks this dict after scanning any identifier.
# If the identifier is a keyword, it uses the mapped type instead of IDENT.
# true/false map to BOOL_LIT - the lexer sets value=True or value=False.

KEYWORDS: dict[str, TokenType] = {
    "var":      TokenType.VAR,
    "const":    TokenType.CONST,
    "func":     TokenType.FUNC,
    "struct":   TokenType.STRUCT,
    "int":      TokenType.INT,
    "bool":     TokenType.BOOL,
    "void":     TokenType.VOID,
    "true":     TokenType.BOOL_LIT,
    "false":    TokenType.BOOL_LIT,
    "if":       TokenType.IF,
    "else":     TokenType.ELSE,
    "for":      TokenType.FOR,
    "return":   TokenType.RETURN,
}

@dataclass
class Token:
    kind:   TokenType    # what kind of token this is
    value:  str|int|bool # raw value: identifier, string, integers or bool
    line:   int          # 1-based line number - for error messages
    pos:    int          # 0-based column offset - for error messages
    
