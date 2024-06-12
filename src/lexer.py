from src.utils import Error


# tokens 
TT_EOF = "EOF"
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
# --- symbols ---
TT_OpenParen = "OpenParen"
TT_CloseParen = "CloseParen"


class Token:
    def __init__(self, value, type: str) -> None:
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
                tokens.append(Token(float(number), TT_Number))
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
                Error(f"Syntax Error: unkown symbol {src[0]}", self.PosLine)

        tokens.append(Token("EOF", TT_EOF))
        return tokens



