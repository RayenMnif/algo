def Error(error: str, at_line=None) -> None:
    print(f"================ Error ================\n{error} at line {at_line}") if at_line else  print(f"================ Error ================\n{error}")
    exit(0)

VarTypes = ["entier",
    "reel", "réel",
    "chaine_de_caractere", "chaine_de_caractère", "chaine",
    "matrice", "mat",
    "tableau", "tab"]

BinaryOperator =  ["*",
    '/',
    "mod", "Mod",
    "div", "Div"]
