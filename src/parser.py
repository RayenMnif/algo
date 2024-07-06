from src.lexer import *
from src.ast import *
from src.utils import Error


class Parser:
    def __init__(self, code: str) -> None:
        self.tokens = Lexer(code).tokinze()

    def produce_ast(self) -> Program:
        program: Program = Program([])
        while (self.tokens[0].type != TT_EOF):
           program.body.append(self.parse_statement())
        return program

    def advance(self) -> Token:
        token = self.tokens[0]
        self.tokens.pop(0)
        return token

    def parse_statement(self) -> Statement:
        return self.parse_expression()

    def parse_expression(self) -> Expression:
        return self.parse_additive_expressions()

    def parse_additive_expressions(self) -> Expression:
        left = self.parse_multiplicitive_expressions()
        while self.tokens[0].value in "+-":
            operator = self.advance().value
            right = self.parse_multiplicitive_expressions()
            left = BinaryOperation(left, right, operator)
        return left 

    def parse_multiplicitive_expressions(self) -> Expression:
        left = self.parse_primary_expressions()
        while self.tokens[0].value in ["*", '/', "mod", "div"]:
            operator = self.advance().value
            right = self.parse_primary_expressions()
            left = BinaryOperation(left, right, operator)
        return left 

    def parse_primary_expressions(self) -> Expression:
        token_type = self.tokens[0].type
        if token_type == TT_Number:        
            return NumericLiteral(float(self.advance().value))
        elif token_type == TT_Indentifier:
            return Indentifier(self.advance().value)
        elif token_type == NodeVar:
             return Var(self.advance().value)
        elif token_type == TT_OpenParen:
            self.advance()
            value = self.parse_expression()
            tt = self.advance()
            if tt.type != TT_CloseParen: Error("missing closing parent")
            return value
        elif token_type == TT_Null:
            return Null(self.advance().value)
        else:
            Error(f"Parser Error: Unvalid Statement {self.advance()}")
            return Expression("")



