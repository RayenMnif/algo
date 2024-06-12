# Nodes 
NodeProgram = "Program"
NodeBinaryOperation = "BinaryOperation"
NodeIndentifier = "Indentifier"
NodeNumericLiteral = "NumericLiteral"

class Statement:
    def __init__(self, type: str) -> None:
       self.type = type


class Program(Statement):
    def __init__(self, body: list[Statement]) -> None:
        self.body = body
        super().__init__(NodeProgram)
    def __repr__(self) -> str:
        return f'("Program": (body: {self.body}))'


class Expression(Statement):
    pass

class BinaryOperation(Expression):
    def __init__(self, LeftOp: Exception, RightOp: Exception, Op: str) -> None:
        self.LeftOp = LeftOp
        self.RightOp = RightOp
        self.op = Op
        super().__init__(NodeBinaryOperation)
    def __repr__(self) -> str:
        return f"({NodeBinaryOperation}: (LeftOp: {self.LeftOp}\nRightOp: {self.RightOp}\nop: {self.op}))"


class NumericLiteral(Expression):
    def __init__(self, value: float) -> None:
        self.value = value
        super().__init__(NodeNumericLiteral)
    def __repr__(self) -> str:
        return f"({NodeNumericLiteral}: (value: {self.value})"


class Indentifier(Expression):
    def __init__(self, name: str) -> None:
        super().__init__(NodeIndentifier) 
        self.name = name
    def __repr__(self) -> str:
        return f"({NodeIndentifier}: (name: {self.name}))"



