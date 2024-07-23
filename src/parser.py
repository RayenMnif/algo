from src.lexer import *
from src.ast import *
from src.utils import *


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

    def parse_block_statement(self, end_parsing_array: list[str]) -> BlockStatemnt:
        blockStatemnt = BlockStatemnt([])
        while self.tokens[0].type not in end_parsing_array:
            if self.tokens[0].type == TT_EOF: Error("you forgot to close the statement")
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
        left = self.parse_call_expression()
        while self.tokens[0].value in BinaryOperator:
            operator = self.advance().value
            right = self.parse_primary_expressions()
            left = BinaryOperation(left, right, operator)
        return left

    def parse_call_expression(self) -> Expression:
        callee = self.parse_primary_expressions()
        if self.tokens[0].type == TT_OpenParen and callee.type == NodeIndentifier:
            self.advance()
            args = self.parse_args()
            return CallExpresstion(callee, args)
        return callee

    def parse_args(self):
        if self.tokens[0].type == TT_CloseParen:
            self.advance()
            return []
        args = [self.parse_assignment_expressions()]
        while self.tokens[0].type == TT_Comma and self.advance():
            args.append(self.parse_assignment_expressions())
            if len(args) > 100: Error("Function Call is taking more than 100 argument")
        if self.tokens[0].type == TT_CloseParen:
            self.advance()
            return args
        Error("missing closing parenthesis '('")

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

    def parse_tantque_loop(self):
        self.advance()
        condition = self.parse_boolean_expression()
        if condition.type != NodeBooleanOperation: Error("Is that even a condition")
        if self.tokens[0].type != TT_faire: Error("Excepted 'faire'")
        self.advance()
        statement = self.parse_block_statement([TT_fintanque])
        if self.tokens[0].type == TT_fintanque:
            self.advance()
            return loopTantqueRepeter(condition, statement, True)
        else: Error("Excepted 'fin_tant_que'")

    def parse_repeter_loop(self):
        self.advance()
        statement = self.parse_block_statement([TT_jusqua])
        print(f"statement : {statement}")
        if self.tokens[0].type != TT_jusqua: Error("Excepted 'jusqu\'a'")
        self.advance()
        condition = self.parse_boolean_expression()
        if condition.type != NodeBooleanOperation: Error("Is that even a condition")
        return loopTantqueRepeter(condition, statement, False)

    def parse_for_loop(self):
        self.advance()
        i = self.advance()
        if i.type != TT_Indentifier:
            Error("ForLoopError: unvalid for loops structure\npour <var> de <number> a <number> (pas <number>)? faire\n\t<statement>\nfin_pour")
        de = self.advance()
        if de.type != TT_Indentifier and de.value != "de":
            Error("ForLoopError: unvalid for loops structure\npour <var> de <number> a <number> (pas <number>)? faire\n\t<statement>\nfin_pour")
        num1 = self.parse_additive_expressions()
        a = self.advance()
        if a.type != TT_Indentifier and a.value != "a":
            Error("ForLoopError: unvalid for loops structure\npour <var> de <number> a <number> (pas <number>)? faire\n\t<statement>\nfin_pour")
        num2 = self.parse_additive_expressions()
        if self.tokens[0].type != TT_pas:
            faire = self.advance()
            if faire.type != TT_faire:
                Error("ForLoopError: Expected 'faire'")
            statement = self.parse_block_statement([TT_finpour])
            self.advance()
            return forLoop(i.value,[num1, num2], statement)
        else:
            self.advance()
            pas = self.parse_additive_expressions()
            faire = self.advance()
            if faire.type != TT_faire:
                Error("ForLoopError: Expected 'faire'")
            statement = self.parse_block_statement([TT_finpour])
            self.advance()
            return forLoop(i.value, [num1, num2, pas], statement)

    def parse_fonction(self) -> Expression:
        self.advance()
        callee = self.parse_primary_expressions()
        if callee.type != NodeIndentifier: Error(f"Unvalid function name '{callee}'")
        if self.advance().type != TT_OpenParen: Error("Expected open parenthesis '('")
        parameters = self.parse_parameters_list()
        if self.advance().type != TT_Colon: Error("Expected a Colon ':'")
        return_type = self.parse_primary_expressions()
        self.check_argType(return_type)
        if self.advance().type != TT_Debut: Error("Expected 'Debut'")
        statement = self.parse_block_statement([TT_Fin])
        self.advance()
        return Function(callee, parameters, return_type.name, statement)

    def parse_parameters_list(self) -> list[tuple[str, str]]:
        if self.tokens[0].type == TT_CloseParen:
            self.advance()
            return []
        parameters = [self.parse_parameter()]
        while self.tokens[0].type == TT_Comma and self.advance():
            parameters.append(self.parse_parameter())
            if len(parameters) > 100: Error("Function is taking more than 100 parameter")
        if self.advance().type != TT_CloseParen: Error("Expected closing parenthesis '('")
        return parameters

    def parse_parameter(self) -> tuple[str, str]:
        param = self.parse_primary_expressions()
        if param.type != NodeIndentifier: Error(f"Unvalid paramaeter '{param}'")
        if self.advance().type != TT_Colon: Error("Expected a Colon ':'")
        argType = self.parse_primary_expressions()

        return (param.name, argType.name)

    def check_argType(self, argType: Expression) -> None:
        if argType.type != NodeIndentifier:
            if argType.name not in VarValues.keys() :
                Error(f"Unvalid argument type '{argType.name}'")
            Error(f"Unvalid argument type '{argType}'")

    def parse_return_statement(self):
        self.advance()
        return ReturnStatement(self.parse_statement())


    def parse_primary_expressions(self) -> Expression:
        token_type = self.tokens[0].type
        if token_type == TT_Number: return NumericLiteral(float(self.advance().value))
        elif token_type == NodeIndentifier: return Indentifier(self.advance().value)
        elif token_type == TT_String: return String(self.advance().value)
        elif token_type == TT_OpenParen:
            self.advance()
            value = self.parse_expression()
            tt = self.advance()
            if tt.type != TT_CloseParen: Error("missing closing parenthesis ')'")
            return value
        elif token_type == TT_if:
            return self.parse_if_expression()
        elif token_type == TT_Null:
            return Null(self.advance().value)
        elif token_type == TT_tantque: return self.parse_tantque_loop()
        elif token_type == TT_repeter: return self.parse_repeter_loop()
        elif token_type == TT_pour: return self.parse_for_loop()
        elif token_type == TT_fonction: return self.parse_fonction()
        elif token_type == TT_Retourner: return self.parse_return_statement()
        else:
            Error(f"Parser Error: Unvalid Statement {self.advance()}")
            return Expression("")
