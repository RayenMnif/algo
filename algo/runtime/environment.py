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

    def resolve(self, var_name: str):
        if var_name in self.variables.keys(): return self
        if self.parent == None: Error(f"impossible de résoudre la variable '{var_name}' car elle n'exite pas")
        return self.parent.resolve(var_name)

    def available(self, var_name: str):
        if var_name in self.variables.keys(): return True
        if self.parent == None: return False
        return self.parent.resolve(var_name)


    def get_scope(self, var_name: str):
        if var_name in self.variables.keys(): return self
        if self.parent == None: return None
        return self.parent.get_scope(var_name)



def setup_global_env():
    env = Environment()
    
    # --- helpers functions ---
    def get_data(ds: MatriceVal | TableauVal):
        if ds.pos != None:
            return ds.value[ds.pos[0]][ds.pos[1]] if ds.type == MatriceValue else ds.value[ds.pos]
        else:
            Error(f"If faut specifier les paramametre pour {"la matrice" if ds.type == MatriceValue else "le tableau"} '{ds.name}'")

    def est_digit(valeur):
        if valeur.isdigit():
            return NumberVal(float(valeur))
        Error(f"valeur('{valeur}') : la chaine '{valeur}' n'est pas une chaine numerique")

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
        else:
            for i, arg in enumerate(args):
                if i != len(args) - 1:
                    print(arg if arg.type not in [MatriceValue, TableauValue] else get_data(arg), end="")
                else: print(arg if arg.type not in [MatriceValue, TableauValue] else get_data(arg)) 

    env.assignVar("ecrire", NativeFnVal(ecrire))
    env.assignVar("écrire", NativeFnVal(ecrire))
    # arrondi
    def arroundi(args, env):
        if len(args) != 1:
            Error("arrondi(x) prend un seul argument")
        else:
            if args[0].type == NumberValue:
                return NumberVal(round(args[0].value))
            elif args[0].type in [TableauValue, MatriceValue]:
                result = get_data(args[0])
                return arroundi([result], env)
            else:
                Error("arrondi(x) prend un nombre comme argument")
    env.assignVar("arrondi", NativeFnVal(arroundi))

    # racine_carré
    def racine_carre(args, env):
        if len(args) != 1:
            Error("racine_carre(x) prend un seul argument (un nombre)")
        else:
            if args[0].type == NumberValue:
                return NumberVal(sqrt(args[0].value))
            elif args[0].type in [TableauValue, MatriceValue]:
                result = get_data(args[0])
                return racine_carre([result], env)
            else:
                Error("racine_carre(x) prend un nombre comme argument")

    env.assignVar("racine_carre", NativeFnVal(racine_carre))
    env.assignVar("racine_carré", NativeFnVal(racine_carre))

    # ent
    def ent(args, env):
        if len(args) != 1:
            Error("ent(x) prend un seul argument (un nombre)")
        else:
            if args[0].type == NumberValue:
                return NumberVal(int(args[0].value))
            elif args[0].type in [TableauValue, MatriceValue]:
                result = get_data(args[0])
                return ent([result], env)
            else:
                Error("ent(x) prend un nombre comme argument")

    env.assignVar("ent", NativeFnVal(ent))

    # abs
    def to_abs(args, env):
        if len(args) != 1:
            Error("abs(x) prend un seul argument (un nombre)")
        else:
            if args[0].type == NumberValue:
                return NumberVal(abs(args[0].value))
            elif args[0].type in [TableauValue, MatriceValue]:
                result = get_data(args[0])
                return abs([result], env)
            else:
                Error("abs(x) prend un nombre comme argument")


    env.assignVar("abs", NativeFnVal(to_abs))

    # alea
    def alea(args, env):
        if len(args) != 2:
            Error("alea(a, b) prend deux arguments (deux entiers)")
        else:
            if args[0].type in [TableauValue, MatriceValue]: args[0] = get_data(args[0])
            if args[1].type in [TableauValue, MatriceValue]: args[1] = get_data(args[1])

            if args[0].type == NumberValue and args[1].type == NumberValue:
                if args[1].value < args[0].value:
                    Error("alea(a, b) error l'argument a > b")
                return NumberVal(randint(int(args[0].value), int(args[1].value)))
            else:
                Error("alea(a, b) prend deux nombres comme argument")


    env.assignVar("alea", NativeFnVal(alea))

    # estnum
    def estnum(args, env):
        if len(args) != 1:
            Error("estnum(x) prend un seul argument (une chaine)")
        else:
            if args[0].type == StringValue:
                return BooleanVal(args[0].value.isdigit())
            elif args[0].type in [TableauValue, MatriceValue]:
                result = get_data(args[0])
                return estnum([result], env)
            else:
                Error("estnum(x) prend une chaine comme argument")


    env.assignVar("estnum", NativeFnVal(estnum))

    #convch
    def convch(args, env):
        if len(args) != 1:
            Error("convch(x) prend un seul argument (une valeur numerique)")
        else:
            if args[0].type == NumberValue:
                return StringVal(str(args[0].value))
            elif args[0].type in [TableauValue, MatriceValue]:
                result = get_data(args[0])
                return convch([result], env)
            else:
                Error("convch(x) prend une valeur numerique comme argument")


    env.assignVar("convch", NativeFnVal(convch))

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
                    return StringVal(input(""))
                elif args[0].type == MatriceValue:
                    matrice : MatriceVal = args[0]
                    if matrice.pos:
                        matrice.value[args[0].pos[0]][args[0].pos[1]] = StringVal(input("> "))
                        env.assignVar(matrice.name, MatriceVal(matrice.name, matrice.value))
                    else: 
                        Error(f"Il est impossible de lire la matrice '{matrice.name}' il faux specifier les argument\nExemple: lire({matrice.name}[0,0])")
                elif args[0].type == TableauValue:
                    tableau : TableauVal = args[0]
                    if tableau.pos != None:
                        tableau.value[args[0].pos] = StringVal(input("> "))
                        env.assignVar(tableau.name, TableauVal(tableau.name, tableau.value))
                    else:
                        Error(f"Il est impossible de lire la tableau '{tableau.name}' il faux specifier les argument\nExemple: lire({tableau.name}[0])")
                else: Error("Unvalid argument type\nlire should take une chaine as argument or no argument")
            else:
                return StringVal(input("> "))

    env.assignVar("lire", NativeFnVal(lire))
    

    # sous_chaine(ch, d, f)
    def sous_chaine(args, env):
        if len(args) != 3:
            Error("sous_chaine prend trois arguments\nsous_chaine(ch, d, f) d'ou ch est la chaine, d est le debut et f est la fin")
        if args[0].type not in [StringValue, TableauValue, MatriceValue] or args[1].type != NumberValue or args[2].type != NumberValue:
            Error("sous_chaine prend trois arguments\nsous_chaine(ch, d, f) d'ou ch est la chaine, d (entier) est le debut et f (entier) est la fin")
        if args[0].type in [MatriceValue, TableauValue]:
            ch = get_data(args[0])
            if ch.type != StringValue:
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
        if len(args) != 1 or args[0].type not in [StringValue, MatriceValue, TableauValue]:
            Error("valeur(x) prend un seul argument (une chaine)")
        if args[0].type == StringValue:
            return est_digit(args[0].value)
        else:
            if args[0].pos != None:
                return est_digit(args[0].value[args[0].pos[0]][args[0].pos[1]].value if args[0].type == MatriceValue else args[0].value[args[0].pos].value )
            else: Error(f"aucun argument est specifee dans {"la matrice" if args[0].type == MatriceValue else "le tableau"} '{args[0].name}'")
    env.assignVar("valeur", NativeFnVal(valeur))

    # pos(ch1, ch2) 
    def pos(args, env):
        if len(args) != 2:
            Error("pos(ch1, ch2) prend deux arguments (de type chaine)")
        if args[0].type in [TableauValue, MatriceValue]: args[0] = get_data(args[0])
        if args[1].type in [TableauValue, MatriceValue]: args[1] = get_data(args[1])
        if args[0].type != args[1].type != StringValue:
            Error("pos(ch1, ch2) prend deux arguments (de type chaine)")
        ch1 : str = args[0].value
        ch2 : str = args[1].value
        return StringVal(ch2.find(ch1))

    env.assignVar("pos", NativeFnVal(pos))


    # majus
    def majus(args, env):
        if len(args) != 1:
            Error("majus(x) prend un seul argument (une chaine)")
        else:
            if args[0].type == StringValue:
                return StringVal(args[0].value.upper())
            elif args[0].type in [TableauValue, MatriceValue]:
                result = get_data(args[0])
                return majus([result], env)
            else:
                Error("majus(x) prend une chaine comme argument")


    env.assignVar("majus", NativeFnVal(majus))

    # effacer(ch, d, f)
    def effacer(args, env):
        if len(args) != 3:
            Error("effacer prend trois arguments\neffacer(ch, d, f) d'ou ch est la chaine, d est le debut et f est la fin")
        if args[0].type not in [StringValue, TableauValue, MatriceValue] or args[1].type != NumberValue or args[2].type != NumberValue:
            Error("effacer prend trois arguments\neffacer(ch, d, f) d'ou ch est la chaine, d (entier) est le debut et f (entier) est la fin")
        if args[0].type in [MatriceValue, TableauValue]:
            ch = get_data(args[0])
            if ch.type != StringValue:
                Error("effacer prend trois arguments\neffacer(ch, d, f) d'ou ch est la chaine, d est le debut et f est la fin")
        ch : str = args[0].value
        d : int = args[1].value
        f : int = args[2].value
        if not isinstance(d, int) or not isinstance(f, int):
            Error("effacer prend trois arguments\neffacer(ch, d, f) d'ou ch est la chaine, d (entier) est le debut et f (entier) est la fin")
        return StringVal(ch[:d]+ch[f:])
    env.assignVar("effacer", NativeFnVal(effacer))

    return env
