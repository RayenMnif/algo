from runtime.value import *
from random import randint
from math import pi, sqrt
from src.utils import Error


class Environment:
    def __init__(self, parent = None) -> None:
        self.parent : Environment | None = parent
        self.variables: dict[str, RunTime] = {}

    def lookUpVar(self, var_name: str) -> RunTime:
        env = self.resolve(var_name)
        return env.variables[var_name]

    def assignVar(self, var_name: str, value: RunTime) -> RunTime:
        env = self.get_scope(var_name)
        if env:
            env.variables[var_name] = value
        else:
            self.variables[var_name] = value
        return value

    def resolve (self, var_name: str):
        if var_name in self.variables.keys(): return self
        if self.parent == None: Error(f"Canno't resolve '{var_name}' as it does not exist")
        return self.parent.resolve(var_name)

    def get_scope(self, var_name: str):
        if var_name in self.variables.keys(): return self
        if self.parent == None: return None
        return self.parent.get_scope(var_name)



def setup_global_env():
    env = Environment()

    # --- global values ---
    # Boolean values 
    env.assignVar("vrai", BooleanVal(True))
    env.assignVar("faux", BooleanVal(False))
    # global var
    env.assignVar("pi", NumberVal(pi))

    # --- native functions ---
    # ecrire
    env.assignVar("ecrire", NativeFnVal(lambda args: print() if len(args) == 0 else [print(arg) for arg in args]))
    env.assignVar("écrire", NativeFnVal(lambda args: print() if len(args) == 0 else [print(arg) for arg in args]))
    # arrondi
    env.assignVar("arrondi", NativeFnVal(lambda args: Error("arrondi takes one argumernt") if len(args) != 1 else NumberVal(round(args[0].value)) if args[0].type == NumberValue else Error("arrondi takes a number as argument") ))
    # racine_carré
    env.assignVar("racine_carre", NativeFnVal(lambda args: Error("racine_carre takes one argumernt") if len(args) != 1 else NumberVal(sqrt(args[0].value)) if args[0].type == NumberValue else Error("racine_carre takes a number as argument") ))
    env.assignVar("racine_carré", NativeFnVal(lambda args: Error("racine_carré takes one argumernt") if len(args) != 1 else NumberVal(sqrt(args[0].value)) if args[0].type == NumberValue else Error("racine_carre takes a number as argument") ))
    # ent 
    env.assignVar("ent", NativeFnVal(lambda args: Error("ent takes one argumernt") if len(args) != 1 else NumberVal(int(args[0].value)) if args[0].type == NumberValue else Error("ent takes a number as argument") ))
    # abs
    env.assignVar("abs", NativeFnVal(lambda args: Error("abs takes one argumernt") if len(args) != 1 else NumberVal(abs(args[0].value)) if args[0].type == NumberValue else Error("abs takes a number as argument") ))
    # alea 
    env.assignVar("alea", NativeFnVal(lambda args: Error("alea takes one argumernt") if len(args) != 2 else NumberVal(float(randint(int(args[0].value), int(args[1].value))) if args[0].type == NumberValue and args[0].type == NumberValue and args[0].value < args[1].value else Error("alea takes two number as argument") )))

    # estnum
    # not implimented yet 
    
    # long
    # not implimented yet 

    # long
    # not implimented yet 

    # sous_chaine(ch, d, f)
    # not implimented yet 

    # majus
    # not implimented yet 

    # effacer
    # not implimented yet 

    return env

 
