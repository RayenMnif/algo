from runtime.environment import Environment
from src.utils import Error
from runtime.value import *
from src.ast import *


def eval_binary_operation(binop: BinaryOperation, env: Environment) -> RunTime:
    left = evaluate(binop.LeftOp, env)
    right = evaluate(binop.RightOp, env)
    if left.type == NumberValue and right.type == NumberValue:
        return eval_numeric_binary_expression(left, right, binop.op)
    return NullVal()


def eval_numeric_binary_expression(LeftOp: NumberVal, RightOp: NumberVal, op) -> NumberVal:
    left = LeftOp.value
    right = RightOp.value
    if op == "+":
        result = left + right
    elif op == "-":
        result = left - right
    elif op == "*":
        result = left * right
    elif op == "/":
        if right == 0:
            Error("ZeroDivisionError: division by zero")
        result = left / right
    elif op == "mod":
        result = left % right
    elif op == "div":
        if right == 0:
            Error("ZeroDivisionError: division by zero")
        result = left // right
    print(f"result : {result}")
    return NumberVal(result)

def eval_program(program : Program, env: Environment) -> RunTime:
    last_evaluated = NullVal()
    for statement in program.body:
        last_evaluated =  evaluate(statement, env)
    return last_evaluated


def eval_Var(var: Var, env: Environment) -> RunTime:
    return env.lookUpVar(var.name)

def eval_assignment(assig: Assignment, env: Environment):
    if assig.var.type != NodeVar: Error(f"Looks like you're wrongly assigning the variable")
    return env.assignVar(assig.var.name, evaluate(assig.value, env))

def evaluate(astNode: Statement, env: Environment) -> RunTime:
    if astNode.type == NodeBinaryOperation:
        return eval_binary_operation(astNode, env)
    elif astNode.type == NodeAssignment:
        return eval_assignment(astNode, env)
    elif astNode.type == NodeNumericLiteral:
        return NumberVal(astNode.value)
    elif astNode.type == NodeProgram:
        return eval_program(astNode, env)
    elif astNode.type == NodeNull:
        return NullVal()
    elif astNode.type == NodeVar:
        return eval_Var(astNode, env)
    else: Error("Unvalid returning value") 
