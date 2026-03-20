class Node:
    pass

class Number(Node):
    def __init__(self, value: int) -> None:
        self.value: int = value

    def __repr__(self) -> str:
        return f"Number({self.value})"

class Boolean(Node):
    def __init__(self, value: bool) -> None:
        self.value: bool = value

    def __repr__(self) -> str:
        return f"Boolean({'true' if self.value else 'false'})"

class Char(Node):
    def __init__(self, value: str) -> None:
        escaped = repr(value)
        self.value: str = escaped

    def __repr__(self) -> str:
        return f"Char('{self.value}')"

class BinaryOp(Node):
    def __init__(self, left: Node, op: str, right: Node) -> None:
        self.left: Node = left
        self.op: str = op
        self.right: Node = right

    def __repr__(self) -> str:
        return f"BinaryOp({self.left} {self.op} {self.right})"

class UnaryOp(Node):
    def __init__(self, op: str, right: Node) -> None:
        self.op : str = op
        self.right: Node = right

    def __repr__(self) ->str:
        return f"Unary({self.op} {self.right})"

class Assign(Node):
    def __init__(self, name: str, expr: Node) -> None:
        self.name: str = name
        self.expr: Node = expr

    def __repr__(self) -> str:
        return f"Assign({self.name} {self.expr})"

class Var(Node):
    def __init__(self, name: str) -> None:
        self.name: str = name

    def __repr__(self) -> str:
        return f"Var({self.name})"

class VarDecl(Node):
    def __init__(self, name: str, var_type: str, expr: Node|None) -> None:
        self.name: str = name
        self.var_type: str = var_type
        self.expr: Node|None = expr

    def __repr__(self) -> str:
        return f"VarDecl({self.name} {self.var_type} {self.expr})"

class If(Node):
    def __init__(self, cond: Node, if_block: list[Node], else_block: list[Node]|None) -> None:
        self.cond: Node = cond
        self.if_block: list[Node] = if_block
        self.else_block: list[Node]|None = else_block

    def __repr__(self) -> str:
        return (f"If({self.cond} {self.if_block} {self.else_block})")
