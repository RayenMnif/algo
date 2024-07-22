ReturnValue = "Retourner"
StringValue = "ChaineDeCaracter"
AssignmentValue = "Assignment"
NumberValue = "Nombre"
NullValue = "nulle"
BooleanValue = "booleen"
NativeFnvalue = "NativeFunction"

class RunTime:
    def __init__(self, type: str) -> None:
        self.type = type

class NumberVal(RunTime):
    def __init__(self, value: float) -> None:
        self.value = value
        super().__init__(NumberValue)
    def __repr__(self) -> str:
        return f"{self.value}"

class NullVal(RunTime):
    def __init__(self) -> None:
        self.value = None
        super().__init__(NullValue)
    def __repr__(self) -> str:
        return f"{self.value}"


class ReturnVal(RunTime):
    def __init__(self, value: RunTime) -> None:
        super().__init__(ReturnValue)
        self.value = value
    def __repr__(self) -> str:
        return f"{self.value}"


class BooleanVal(RunTime):
    def __init__(self, value: bool) -> None:
        super().__init__(BooleanValue)
        self.value = value
    def __repr__(self) -> str:
        return f"{self.value}"

class NativeFnVal(RunTime):
    def __init__(self, call) -> None:
        super().__init__(NativeFnvalue)
        self.call = call
    def __repr__(self) -> str:
        return f"{self.value}"


class StringVal(RunTime):
    def __init__(self, value: str) -> None:
        super().__init__(StringValue)
        self.value = value
    def __repr__(self) -> str:
        return f"{self.value}"
