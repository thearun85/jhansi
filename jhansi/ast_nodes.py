class Node:
    pass

class Number(Node):
    def __init__(self, value: int) -> None:
        self.value: int = value

    def __repr__(self) -> str:
        return f"Number({self.value})"

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
