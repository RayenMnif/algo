from runtime.value import *
from src.utils import Error


class Environment:
    def __init__(self, parent = None) -> None:
        self.parent : Environment | None = parent
        self.variables: dict[str, RunTime] = {}

    def lookUpVar(self, var_name: str) -> RunTime:
        env = self.resolve(var_name)
        return env.variables[var_name]

    def assignVar(self, var_name: str, value: RunTime) -> RunTime:
        self.variables[var_name] = value
        return value

    def resolve (self, var_name: str):
        if var_name in self.variables.keys(): return self
        if self.parent == None: Error(f"Canno't resolve '{var_name}' as it does not exist")
        return self.parent.resolve(var_name)


