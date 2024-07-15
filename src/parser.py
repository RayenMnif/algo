from typing import List
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

    def parse_block_statement(self, end_parsing_array: List[str]) -> BlockStatemnt:
        blockStatemnt = BlockStatemnt([])
        while self.tokens[0].type not in end_parsing_array:
            blockStatemnt.body.append(self.parse_statement())
        return blockStatemnt


    def parse_expression(self) -> Expression:
        return self.parse_assignment_expressions()

    def parse_assignment_expressions(self):
        left = self.parse_boolean_expression()
        if self.tokens[0].value == "<-":
            self.advance()
            right = self.parse_assignment_expressions()
            left = Assignment(left, right)
        return left

    def parse_boolean_expression(self) -> Expression:
        left = self.parse_additive_expressions()
        if self.tokens[0].type == TT_BooleanOperator:
            op = self.advance().value
            right = self.parse_boolean_expression()
            left = BooleanOperation(left, right, op)
        return left


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

    def parse_if_expression(self) -> Expression:
        cases = []
        else_case = None
        self.advance()
        condition = self.parse_boolean_expression()
        if condition.type != NodeBooleanOperation: Error("Is that even a condition")
        if self.tokens[0].type != TT_alors: Error("Excepted 'alors'")
        self.advance()
        statement = self.parse_block_statement([TT_elif, TT_else, TT_finsi])
        cases.append((condition, statement))
        while self.tokens[0].type == TT_elif:
            self.advance()
            condition = self.parse_boolean_expression()
            if condition.type != NodeBooleanOperation: Error("Is that even a condition")
            if self.tokens[0].type != TT_alors: Error("Excepted 'alors'")
            self.advance()
            statement = self.parse_block_statement([TT_elif, TT_else, TT_finsi])
            cases.append((condition, statement))
        if self.tokens[0].type == TT_else:
            self.advance()
            else_case = self.parse_block_statement([TT_elif, TT_else, TT_finsi])
        if self.tokens[0].type == TT_finsi:
            self.advance()
            return ifStatement(cases, else_case)
        else: Error("Excepted 'fin_si'")


    def parse_primary_expressions(self) -> Expression:
        token_type = self.tokens[0].type
        if token_type == TT_Number:        
            return NumericLiteral(float(self.advance().value))
        elif token_type == NodeVar:
             return Var(self.advance().value)
        elif token_type == TT_OpenParen:
            self.advance()
            value = self.parse_expression()
            tt = self.advance()
            if tt.type != TT_CloseParen: Error("missing closing parent")
            return value
        elif token_type == TT_if:
            return self.parse_if_expression()
        elif token_type == TT_Null:
            return Null(self.advance().value)
        else:
            Error(f"Parser Error: Unvalid Statement {self.advance()}")
            return Expression("")



