from src.utils import Error


# tokens
TT_EOF = "EOF"
# --- var types ---
TT_Number = "Number"
TT_String = "String"
# --- var related ---
TT_Indentifier = "Indentifier"
TT_Asignment = "Asignment"
# --- operations ---
TT_BinaryOperator = "BinaryOperator"
TT_BooleanOperator = "BooleanOperator"
# --- keywords ---
TT_Null = "nulle"
# --- fonctions ---
TT_Procedure = "procedure"
TT_fonction = "fonction"
TT_Retourner = "retourner"
# --- symbols ---
TT_OpenParen = "OpenParen"
TT_CloseParen = "CloseParen"
TT_OpenBrace = "OpenBrace"
TT_CloseBrace = "CLoseBrace"
TT_Comma = "Comma"
TT_Colon = "Colon"
# --- keyword ---
TT_Debut = "Debut"
TT_Fin = "Fin"
# --- if Statement ----
TT_if = "si"
TT_elif = "sinon_si"
TT_else = "sinon"
TT_alors = "alors"
TT_finsi = "fin_si"
# --- loops ----
TT_tantque = "tant_que"
TT_faire = "faire"
TT_fintanque = "fin_tant_que"
TT_repeter = "repeter"
TT_jusqua = "jusqu'a"
TT_pour = "pour"
TT_pas = "pas"
TT_faire = "faire"
TT_finpour = "fin_pour"



KEYWORDS = {"div": TT_BinaryOperator,
            "mod": TT_BinaryOperator,
            "Div": TT_BinaryOperator,
            "Mod": TT_BinaryOperator,
            "nulle": TT_Null,
            "fonction": TT_fonction,
            "procédure": TT_Procedure, "procedure": TT_Procedure,
            "ou": TT_BooleanOperator,
            "et": TT_BooleanOperator,
            "si": TT_if,
            "sinon_si": TT_elif,
            "sinon": TT_else,
            "alors": TT_alors,
            "fin_si": TT_finsi,
            "tant_que": TT_tantque,
            "faire": TT_faire,
            "fin_tant_que": TT_fintanque,
            "jusqu'a": TT_jusqua, "jusqua": TT_jusqua,
            "repeter": TT_repeter, "répéter": TT_repeter,
            "debut": TT_Debut, "début": TT_Debut,
            "fin": TT_Fin,
            "pour": TT_pour,
            "pas": TT_pas,
            "fin_pour": TT_finpour,
            "retourner": TT_Retourner}

class Token:
    def __init__(self, value, type: str) -> None:
        self.value = value
        self.type = type
    def __repr__(self) -> str:
        return f" (value: {self.value}, type: {self.type})"


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
        try:
            while src[i] != src[0] and i < len(src):
                string += src[i]
                i += 1
        except:
            Error("quotes were not close", self.PosLine)
        return string

    def tokinze(self) -> list[Token]:
        tokens : list[Token] = []
        src = list(self.src)
        while src:

            if self.is_skippable(src[0]): src.pop(0)

            elif src[0] == "(":
                tokens.append(Token("(", TT_OpenParen))
                src.pop(0)

            elif src[0] == ")":
                tokens.append(Token(")", TT_CloseParen))
                src.pop(0)

            elif src[0] == "[":
                tokens.append(Token("(", TT_OpenBrace))
                src.pop(0)

            elif src[0] == "]":
                tokens.append(Token("]", TT_CloseBrace))
                src.pop(0)

            elif src[0] == ",":
                tokens.append(Token(",", TT_Comma))
                src.pop(0)


            elif src[0] == ":":
                tokens.append(Token(":", TT_Colon))
                src.pop(0)


            elif  src[0] == "<":
                if src[1] not in "-=":
                    tokens.append(Token("<", TT_BooleanOperator))
                    src.pop(0)
                elif src[1] == "=":
                    tokens.append(Token("<=", TT_BooleanOperator))
                    src.pop(0)
                    src.pop(0)
                else:
                    tokens.append(Token("<-", TT_Asignment))
                    src.pop(0)
                    src.pop(0)

            elif src[0] in ["+", "-", "*", "/"]:
                tokens.append(Token(src[0], TT_BinaryOperator))
                src.pop(0)

            elif src[0] == ">":
                if src[1] != "=":
                    tokens.append(Token(">", TT_BooleanOperator))
                    src.pop(0)
                else:
                    tokens.append(Token(">=", TT_BooleanOperator))
                    src.pop(0)
                    src.pop(0)

            elif src[0].isdigit():
                is_float = False
                number = ""
                while len(src) and (src[0].isdigit() or src[0] == "."):
                    if src[0] == ".":
                        if is_float:
                            Error("unvalid number", self.PosLine)
                        else:
                            is_float = True
                    number += src[0]
                    src.pop(0)
                tokens.append(Token(number, TT_Number))

            elif src[0] == "=":
                tokens.append(Token("=", TT_BooleanOperator))
                src.pop(0)

            elif len(src) > 2 and src[0]+src[1] == "!=":
                tokens.append(Token("!=", TT_BooleanOperator))
                src.pop(0)
                src.pop(0)

            elif src[0] in ["'", '"']:
                string = self.stringify(src)
                for i in range(len(string) + 2):
                    src.pop(0)
                tokens.append(Token(string, TT_String))

            elif src[0].isalpha() or src[0] in "_'":
                keyword =  ""
                while src and (src[0].isalpha() or src[0] in "_'"):
                    keyword += src[0]
                    src.pop(0)
                tokens.append(Token(keyword, TT_Indentifier) if keyword not in KEYWORDS.keys() else Token(keyword, KEYWORDS[keyword]))

            else:
                Error(f"Syntax Error: unkown symbol {src[0]}", self.PosLine)

        tokens.append(Token("EOF", TT_EOF))
        return tokens
