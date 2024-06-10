import colorama
from sys import argv, exit

colorama.init(autoreset=True)

# tokens 
# --- var types ---
TT_Number = "Number"
TT_String = "String"

# --- var related ---
TT_Var = "Var"
TT_Indentifier = "Indentifier"

# --- operations ---
TT_Equels = "Equals"
TT_NotEqual = "Not Equals"
TT_Less = "LESS"
TT_Greater = "Grater"
TT_GreaterOrEqual = "GraterOrEqual"
TT_LessOrEqual = "LessOrEqual"
TT_BinaryOperator = "BinaryOperator"

# --- keywords ---
TT_Vrai = "Vrai"
TT_Faux = "Faux"
TT_Mod = "Mod"
TT_Div = "Div"

TT_OpenParen = "OpenParen"
TT_CloseParen = "CloseParen"

class Token:
    def __init__(self, value: str, type: str) -> None:
        self.value = value
        self.type = type
    def __repr__(self) -> str:
        return f" ({self.value} : {self.type})"


class Lexer:
    def __init__(self, source_code : str) -> None:
        self.src = source_code
        self.PosLine = 1

    def is_skippable(self, x: str) -> bool:
        if  x == "\n": self.PosLine += 1
        return x == " " or x == "\n" or x == "\t" or x == "\r"

    def stringify(self, src: list[str]) -> str:
        string = ""
        i = 1
        while src[i] != src[0] and i < len(src):
            string += src[i]
            i += 1
        return string

    def tokinze(self) -> list[Token]:
        tokens : list[Token] = []
        src = list(self.src)
        while len(src) != 0:
            if self.is_skippable(src[0]): src.pop(0) 
            elif src[0] == "(": 
                tokens.append(Token("(", TT_OpenParen))
                src.pop(0)
            elif src[0] == ")": 
                tokens.append(Token(")", TT_CloseParen))
                src.pop(0)
            elif  src[0] == "<": 
                if src[1] not in "-=":
                    tokens.append(Token("<", TT_Less))
                    src.pop(0)
                elif src[1] == "=": 
                    tokens.append(Token("<=", TT_LessOrEqual))
                    src.pop(0)
                    src.pop(0)
                else:
                    tokens.append(Token("<-", TT_Indentifier))
                    src.pop(0)
                    src.pop(0)
            elif src[0] in ["+", "-", "*", "/"]: 
                tokens.append(Token(src[0], TT_BinaryOperator))
                src.pop(0)
            elif src[0] == ">":
                if src[1] != "=":
                    tokens.append(Token(">", TT_Greater))
                    src.pop(0)
                else:
                    tokens.append(Token(">=", TT_GreaterOrEqual))
                    src.pop(0)
                    src.pop(0)
            elif src[0].isdigit():
                number = ""
                while src[0].isdigit():
                    number += src[0]
                    src.pop(0)
                tokens.append(Token(number, TT_Number))
            elif src[0] == "=": 
                tokens.append(Token("=", TT_Equels))
                src.pop(0)
            elif src[0]+src[1] == "!=": 
                tokens.append(Token("!=", TT_NotEqual))
            elif src[0] in ["'", '"']:
                string = self.stringify(src)
                for i in range(len(string) + 2):
                    src.pop(0)
                tokens.append(Token(string, TT_String))
            elif src[0].isalpha():
                string =  ""
                while src[0].isalpha():
                    string += src[0]
                    src.pop(0)
                tokens.append(Token(string, TT_Var))
            else:
                print(f"{colorama.Fore.RED}< Error >{colorama.Fore.RESET}\nUnkown symbol '{src[0]}' at line {self.PosLine} ")
                exit(0)

        return tokens


class Statement:
    def __init__(self, type) -> None:
       self.type = type
    def __repr__(self) -> str:
        return f"(Statement : {self.type})"

class Program:
    def __init__(self, body: list[Statement], type: Statement) -> None:
        self.body = body
        self.type = Statement("Program")


class Expression():
    def __init__(self, type: str) -> None:
       self.type = type
    def __repr__(self) -> str:
        return f"(Expression : {self.type})"

class BinaryOperation:
    def __init__(self, LeftOp: Exception, RightOp: Exception, Op: str, type: Exception) -> None:
        self.LeftOp = LeftOp
        self.RightOp = RightOp
        self.op = Op
        self.type = Exception("BinaryOperator")


class NumericLiteral:
    def __init__(self, value: float, type: Expression) -> None:
        self.value = value
        self.type = Expression("NumericLiteral")


class Indentifier:
    def __init__(self, type: Expression, name: str) -> None:
        self.type = Expression("Indentifier") 
        self.name = name


class Parser:
    pass


if len(argv) != 2:
    print("Usage: python algo.py [script]")
    exit(0)

with open(argv[1], "r") as script:
    tokens = Lexer(script.read()).tokinze()
    print(tokens)
