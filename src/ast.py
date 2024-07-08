# Nodes 
NodeNull = "Nulle"
NodeProgram = "Program"
NodeBinaryOperation = "BinaryOperation"
NodeAssignment = "Assignment"
NodeNumericLiteral = "NumericLiteral"
NodeBooleanOperation = "BooleanOperation"
NodeVar= "Var"

class Statement:
    def __init__(self, type: str) -> None:
       self.type = type


class Program(Statement):
    def __init__(self, body: list[Statement]) -> None:
        self.body = body
        super().__init__(NodeProgram)
    def __repr__(self) -> str:
        return f'{{"Program": {{body: {self.body}}}}}'


class Expression(Statement):
    pass

class BooleanOperation(Expression):
    def __init__(self, LeftOp: Expression, RightOp: Expression, Op: str) -> None:
        self.LeftOp = LeftOp
        self.RightOp = RightOp
        self.op = Op
        super().__init__(NodeBooleanOperation)
    def __repr__(self) -> str:
        return f"\n{{{NodeBooleanOperation}:\n\tLeftOp: {self.LeftOp},\n\top: {self.op},\n\tRightOp: {self.RightOp}\n}}\n"



class BinaryOperation(Expression):
    def __init__(self, LeftOp: Expression, RightOp: Expression, Op: str) -> None:
        self.LeftOp = LeftOp
        self.RightOp = RightOp
        self.op = Op
        super().__init__(NodeBinaryOperation)
    def __repr__(self) -> str:
        return f"\n{{{NodeBinaryOperation}:\n\tLeftOp: {self.LeftOp},\n\top: {self.op},\n\tRightOp: {self.RightOp}\n}}\n"


class NumericLiteral(Expression):
    def __init__(self, value: float) -> None:
        self.value = value
        super().__init__(NodeNumericLiteral)
    def __repr__(self) -> str:
        return f"{{{NodeNumericLiteral}: {{value: {self.value}}}}}"


class Var(Expression):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(NodeVar)
    def __repr__(self) -> str:
        return f"{{{NodeVar}: {{name: {self.name}}}}}"


class Assignment(Expression):
    def __init__(self, var: Expression, value: Expression) -> None:
        super().__init__(NodeAssignment) 
        self.var = var
        self.value = value 
    def __repr__(self) -> str:
        return f"{{var : {self.var}, value : {{{self.value}}}}}"


class Null(Expression):
    def __init__(self, name: str) -> None:
        super().__init__(NodeNull) 
        self.name = name
    def __repr__(self) -> str:
        return f"{{{NodeNull}: {{{self.name}}}}}"




