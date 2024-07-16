# Nodes 
from typing import List


NodeLoopTantqueRepeter = "LoopTantqueRepeter"
NodeForLoop = "ForLoop"
NodeBlockStatement = "BlockStatemnt"
NodeIfStatement = "IfStatment"
NodeCallExpresstion = "CallExpresstion"
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

class BlockStatemnt(Statement):
    def __init__(self, body: list[Statement]) -> None:
        self.body = body
        super().__init__(NodeBlockStatement)
    def __repr__(self) -> str:
        return f'{{"BlockStatemnt": {{body: {self.body}}}}}'


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


class CallExpresstion(Expression):
    def __init__(self, callee: Expression,  args: list[Expression]) -> None:
        super().__init__(NodeCallExpresstion) 
        self.callee = callee
        self.args = args 
    def __repr__(self) -> str:
        return f"{{function call :\n callee : {self.callee}, args: {{{self.args}}}}}"


class ifStatement(Expression):
    def __init__(self, cases: list[Expression],  else_case: BlockStatemnt | None) -> None:
        super().__init__(NodeIfStatement) 
        self.cases = cases
        self.else_case = else_case
    def __repr__(self) -> str:
        return f"{{IfStatment: cases : {self.cases}, else_case: {{{self.else_case}}}}}"


class loopTantqueRepeter(Statement):
    def __init__(self, condition: Expression, stmnt: BlockStatemnt, tant_que: bool) -> None:
        super().__init__(NodeLoopTantqueRepeter) 
        self.condition = condition
        self.stmnt = stmnt
        self.tant_que = tant_que
    def __repr__(self) -> str:
        return f"{{loop :\ncondition : {self.condition}, Statement: {{{self.stmnt}}}}}"


class forLoop(Statement):
    def __init__(self,i: List[Expression], stmnt: BlockStatemnt) -> None:
        super().__init__(NodeForLoop) 
        self.i = i
        self.stmnt = stmnt
    def __repr__(self) -> str:
        return f"{{for loop :\ni : {self.i}, Statement: {{{self.stmnt}}}}}"


