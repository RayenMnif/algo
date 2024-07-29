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
        if self.parent == None: Error(f"impossible de résoudre la variable '{var_name}' car elle n'exite pas")
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
    def ecrire(args, env):
        if len(args) == 0:
            print()
        elif len(args) == 1 and args[0].type == MatriceValue:
            try:
                print(args[0].value[args[0].pos[0]][args[0].pos[1]])
            except TypeError:
                print(args[0].value)
        elif len(args) == 1 and args[0].type == TableauValue:
            try:
                print(args[0].value[args[0].pos])
            except TypeError:
                print(args[0].value)
        else: [ print(arg, end="") if (i != len(args) - 1) else print(arg) for i, arg in enumerate(args) ]

    env.assignVar("ecrire", NativeFnVal(ecrire))
    env.assignVar("écrire", NativeFnVal(ecrire))
    # arrondi
    env.assignVar("arrondi", NativeFnVal(lambda args, env: Error("arrondi prend un seul argument") if len(args) != 1 else NumberVal(round(args[0].value)) if args[0].type == NumberValue else Error("arrondi prend un nombre comme argument") ))
    # racine_carré
    env.assignVar("racine_carre", NativeFnVal(lambda args, env: Error("racine_carre prend un seul argument") if len(args) != 1 else NumberVal(sqrt(args[0].value)) if args[0].type == NumberValue else Error("racine_carre prend un nombre comme argument") ))
    env.assignVar("racine_carré", NativeFnVal(lambda args, env: Error("racine_carré prend un seul argument") if len(args) != 1 else NumberVal(sqrt(args[0].value)) if args[0].type == NumberValue else Error("racine_carre prend un nombre comme argument") ))
    # ent
    env.assignVar("ent", NativeFnVal(lambda args, env: Error("ent prend un seul argument") if len(args) != 1 else NumberVal(int(args[0].value)) if args[0].type == NumberValue else Error("ent prend un nombre comme argument") ))
    # abs
    env.assignVar("abs", NativeFnVal(lambda args, env: Error("abs prend un seul argument") if len(args) != 1 else NumberVal(abs(args[0].value)) if args[0].type == NumberValue else Error("abs prend un nombre comme argument") ))
    # alea
    env.assignVar("alea", NativeFnVal(lambda args, env: Error("alea takes two numbers") if len(args) != 2 else NumberVal(float(randint(int(args[0].value), int(args[1].value))) if args[0].type == NumberValue and args[0].type == NumberValue and args[0].value < args[1].value else Error("alea takes two number as argument") )))

    # estnum
    env.assignVar("estnum", NativeFnVal(lambda args, env: Error("estnum prend un seul argument (une chaine)") if len(args) != 1 else BooleanVal(args[0].value.isdigit()) if args[0].type == StringValue else Error("estnum prend des chaines de caracteres seulement")))

    #convch
    env.assignVar("convch", NativeFnVal(lambda args, env: Error("convch prend un seul argument (une valeur numerique)") if len(args) != 1 else StringVal(str(args[0].value)) if args[0].type == NumberValue else Error("convch prend seulement des valueur numerique")))

    # long
    def long(agrs):
        if len(args) != 1:
            Error("long prend un seul argument")
        else:
            if args[0].type == StringValue:
                NumberVal(len(args[0].value))
            else:
                Error("long prend un seul argument une chaine")
    env.assignVar("long", NativeFnVal(long))

    # lire
    def lire(args : list[RunTime], env : Environment):
        if len(args) > 1:
            Error("lire prend un argument ou aucun argument")
        else:
            if len(args) == 1:
                if args[0].type == StringValue:
                    print(args[0].value, end="")
                    return StringVal(input("> "))
                elif args[0].type == MatriceValue:
                    matrice : MatriceVal = args[0]
                    if matrice.pos:
                        args[0].value[args[0].pos[0]][args[0].pos[1]] = StringVal(input("> "))
                        env.assignVar(matrice.name, MatriceVal(matrice.name, matrice.value))
                    else: 
                        Error(f"Il est impossible de lire la matrice '{matrice.name}' il faux specifier les argument\nExemple: lire({matrice.name}[0,0])")
                elif args[0].type == TableauValue:
                    tableau : TableauVal = args[0]
                    if tableau.pos:
                        args[0].value[args[0].pos] = StringVal(input("> "))
                        env.assignVar(tableau.name, TableauVal(tableau.name, tableau.value))
                    else:
                        Error(f"Il est impossible de lire la tableau '{tableau.name}' il faux specifier les argument\nExemple: lire({tableau.name}[0])")
                else: Error("Unvalid argument type\nlire should take une chaine as argument or no argument")

    env.assignVar("lire", NativeFnVal(lire))
    

    # sous_chaine(ch, d, f)
    def sous_chaine(args, env):
        if len(args) != 3:
            Error("sous_chaine prend trois arguments\nsous_chaine(ch, d, f) d'ou ch est la chaine, d est le debut et f est la fin")
        if args[0].type != StringValue or args[1].type != NumberValue or args[2].type != NumberValue:
            Error("sous_chaine prend trois arguments\nsous_chaine(ch, d, f) d'ou ch est la chaine, d (entier) est le debut et f (entier) est la fin")
        ch : StringVal = args[0].value
        d : NumberVal = args[1].value
        f : NullVal = args[2].value
        if not isinstance(d, int) or not isinstance(f, int):
            Error("sous_chaine prend trois arguments\nsous_chaine(ch, d, f) d'ou ch est la chaine, d (entier) est le debut et f (entier) est la fin")
        return StringVal(ch[d:f])
    env.assignVar("sous_chaine", NativeFnVal(sous_chaine))


    # valeur 
    def valeur(args, env):
        if len(args) != 1:
            Error("valeur(x) prend un seul argument (une chaine)")
        if args[0].value.isdigit():
            return NumberVal(float(args[0].value))
        Error(f"valeur('{args[0].value}') : la chaine '{args[0].value}' n'est pas une chaine numerique")
    env.assignVar("valeur", NativeFnVal(valeur))

    # pos(ch1, ch2) 
    def pos(args, env):
        if len(args) != 2:
            Error("pos(ch1, ch2) prend deux arguments (de type chaine)")
        if args[0].type != args[1].type != StringValue:
            Error("pos(ch1, ch2) prend deux arguments (de type chaine)")
        ch1 : str = args[0].value
        ch2 : str = args[1].value
        return StringVal(ch2.find(ch1))

    env.assignVar("pos", NativeFnVal(pos))


    # majus
    env.assignVar("majus", NativeFnVal(lambda args, env: Error("majus prend un seul argument (une chaine)") if len(args) != 1 else StringVal(args[0].value.upper()) if args[0].type == StringValue else Error("majus prend des chaines de caracteres seulement")))

    # effacer(ch, d, f)
    def effacer(args, env):
        if len(args) != 3:
            Error("effacer prend trois arguments\neffacer(ch, d, f) d'ou ch est la chaine, d est le debut et f est la fin")
        if args[0].type != StringValue or args[1].type != NumberValue or args[2].type != NumberValue:
            Error("effacer prend trois arguments\neffacer(ch, d, f) d'ou ch est la chaine, d (entier) est le debut et f (entier) est la fin")
        ch : str = args[0].value
        d : int = args[1].value
        f : int = args[2].value
        if not isinstance(d, int) or not isinstance(f, int):
            Error("effacer prend trois arguments\neffacer(ch, d, f) d'ou ch est la chaine, d (entier) est le debut et f (entier) est la fin")
        return StringVal(ch[:d]+ch[f:])
    env.assignVar("effacer", NativeFnVal(effacer))

    return env
