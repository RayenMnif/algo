from src.lexer import *
from src.ast import *
from src.utils import Error


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens

    def produce_ast(self) -> Program:
        program: Program = Program([])
        while (self.tokens[0].type != TT_EOF):
           program.body.append(self.parse_statement(self.tokens[0]))
        return program

    def advance(self) -> Token:
        token = self.tokens[0]
        self.tokens.pop(0)
        return token

    def parse_statement(self, token: Token) -> Statement:
        return self.parse_expression(token)

    def parse_expression(self, token: Token) -> Expression:
        return self.parse_primary_expressions(token)

    def parse_primary_expressions(self, token: Token) -> Expression:
        if token.type == TT_Number:        
            return NumericLiteral(float(self.advance().value))
        elif token.type == TT_Indentifier:
            return Indentifier(self.advance().value)
        else:
            Error("Parser Error: Unvalid Statement")
            return Expression("")



