AssignmentValue : str = "Assignment"
NumberValue : str = "number"
NullValue : str = "nulle"
BooleanValue : str = "booleen"

class RunTime:
    def __init__(self, type: str) -> None:
        self.type = type

class NumberVal(RunTime):
    def __init__(self, value: float) -> None:
        self.value = value
        super().__init__(NumberValue)
    def __repr__(self) -> str:
        return f"{{value : {self.value}, type: {NumberValue}}}"

class NullVal(RunTime):
    def __init__(self) -> None:
        self.value = None
        super().__init__(NullValue)
    def __repr__(self) -> str:
        return f"{{value : nulle, type: nulle}}"


class BooleanVal(RunTime):
    def __init__(self, value: bool) -> None:
        super().__init__(BooleanValue)
        self.value = value
    def __repr__(self) -> str:
        return f"{{value : {self.value}, type: {BooleanValue}}}"