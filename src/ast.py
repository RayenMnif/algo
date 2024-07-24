# Nodes
NodeReturn = "Retourner"
NodeString = "ChaineDeCaractere"
NodeCallExpresstion = "CallExpresstion"
NodeLoopTantqueRepeter = "Boucle"
NodeForLoop = "BouclePour"
NodeBlockStatement = "BlockStatemnt"
NodeIfStatement = "IfStatment"
NodeCallExpresstion = "CallExpresstion"
NodeNull = "Nulle"
NodeProgram = "Program"
NodeBinaryOperation = "BinaryOperation"
NodeAssignment = "Assignment"
NodeReel = "Réel"
NodeEntier = "Entier"
NodeBooleanOperation = "BooleanOperation"
NodeIndentifier= "Indentifier"
NodeFunction = "Fonction"
NodeProcedure = "Procedure"

class Statement:
    def __init__(self, type: str) -> None:
       self.type = type

class Expression(Statement):
    pass

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

class ReturnStatement(Statement):
    def __init__(self, value: Expression) -> None:
        self.value = value
        super().__init__(NodeReturn)
    def __repr__(self) -> str:
        return f'{{"{NodeReturn}": {{value: {self.value}}}}}'

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


class Reel(Expression):
    def __init__(self, value: float) -> None:
        self.value = value
        super().__init__(NodeReel)
    def __repr__(self) -> str:
        return f"{{{NodeReel}: {{value: {self.value}}}}}"

class Entier(Expression):
    def __init__(self, value: int) -> None:
        self.value = value
        super().__init__(NodeEntier)
    def __repr__(self) -> str:
        return f"{{{NodeEntier}: {{value: {self.value}}}}}"



class String(Expression):
    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(NodeString)
    def __repr__(self) -> str:
        return f"{{{NodeString}: {{value: {self.value}}}}}"

class Indentifier(Expression):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(NodeIndentifier)
    def __repr__(self) -> str:
        return f"{{{NodeIndentifier}: {{name: {self.name}}}}}"


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


class Function(Expression):
    def __init__(self, callee: Expression, parameters: list[tuple[Indentifier, str]], return_type: str, statement: BlockStatemnt) -> None:
        super().__init__(NodeFunction)
        self.callee = callee
        self.parameters = parameters
        self.return_type = return_type
        self.statement = statement
    def __repr__(self) -> str:
        return f"{{fonction :\n callee : {self.callee}, parameters: {self.parameters}, statement: {self.statement}, return_type: {self.return_type}}}"


class Procedure(Statement):
    def __init__(self, callee: Expression,  parameters: list[tuple[Indentifier, Indentifier]], statement: BlockStatemnt) -> None:
        super().__init__(NodeProcedure)
        self.callee = callee
        self.parameters = parameters
        self.statement = statement
    def __repr__(self) -> str:
        return f"{{Procedure :\n callee : {self.callee}, parameters: {self.parameters}, statement: {self.statement}}}"

class UserDefinedFunction(Expression):
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
    def __init__(self,var_name: str, interval: list[Expression], stmnt: BlockStatemnt) -> None:
        super().__init__(NodeForLoop)
        self.var_name = var_name
        self.interval = interval
        self.stmnt = stmnt
    def __repr__(self) -> str:
        return f"{{for loop :\nvar : {self.var_name}, interval: {self.interval}, Statement: {{{self.stmnt}}}}}"


class CallExpresstion(Expression):
    def __init__(self,callee: Expression, args: list[Expression]) -> None:
        super().__init__(NodeCallExpresstion)
        self.callee = callee
        self.args = args
    def __repr__(self) -> str:
        return f"{{CallExpresstion :\ncallee : {self.callee}, args: {self.args}}}"
