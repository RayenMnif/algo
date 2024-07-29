from runtime.value import *

def Error(error: str, at_line=None) -> None:
    print(f"================ Error ================\n{error} a la ligne {at_line}") if at_line else  print(f"================ Error ================\n{error}")
    exit(0)


VarValues = {"chaine": StringValue, "chaine_de_caractere": StringValue, "chaine_de_caractère": StringValue,
            "reel": NumberValue, "réel": NumberValue,
             "entier": NumberValue,
             "matrice": MatriceValue, "Mat": MatriceValue,
             "tableau": TableauValue, "Tab": TableauValue}

BinaryOperator =  ["*",
    '/',
    "mod", "Mod",
    "div", "Div"]
