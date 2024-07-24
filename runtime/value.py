from src.ast import BlockStatemnt

StringValue = "ChaineDeCaracter"
AssignmentValue = "Assignment"
NumberValue = "Nombre"
NullValue = "nulle"
BooleanValue = "booleen"
NativeFnvalue = "NativeFunction"
FunctionValue = "Fonction"
ProcedureValue = "Procedure"

class RunTime:
    def __init__(self, type: str) -> None:
        self.type = type

class NumberVal(RunTime):
    def __init__(self, value: float | int) -> None:
        self.value = value
        super().__init__(NumberValue)
    def __repr__(self) -> str:
        return f"{self.value}"

class NullVal(RunTime):
    def __init__(self) -> None:
        self.value = None
        super().__init__(NullValue)
    def __repr__(self) -> str:
        return f"Nulle"

class BooleanVal(RunTime):
    def __init__(self, value: bool) -> None:
        super().__init__(BooleanValue)
        self.value = value
    def __repr__(self) -> str:
        return "vrai" if self.value else "faux"

class NativeFnVal(RunTime):
    def __init__(self, call) -> None:
        super().__init__(NativeFnvalue)
        self.call = call
    def __repr__(self) -> str:
        return f"{self.call}"

class FunctionVal(RunTime):
    def __init__(self, name: str, param : list[tuple[str]], body: BlockStatemnt, return_type: str, env) -> None:
        super().__init__(FunctionValue)
        self.name = name
        self.param = param
        self.return_type = return_type
        self.env = env
        self.body = body
    def __repr__(self) -> str:
        return f"{self.name}"

class ProcedureVal(RunTime):
    def __init__(self, name: str, param : list[tuple[str]], body: BlockStatemnt, env) -> None:
        super().__init__(ProcedureValue)
        self.name = name
        self.param = param
        self.env = env
        self.body = body
    def __repr__(self) -> str:
        return f"{self.name}"

class StringVal(RunTime):
    def __init__(self, value: str) -> None:
        super().__init__(StringValue)
        self.value = value
    def __repr__(self) -> str:
        return f"{self.value}"
