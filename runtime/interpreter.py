from src.utils import Error
from runtime.value import *
from src.ast import *


def eval_binary_operation(binop: BinaryOperation) -> RunTime:
    left = evaluate(binop.LeftOp)
    right = evaluate(binop.RightOp)
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
            Error("division by 0")
        result = left / right
    elif op == "mod":
        result = left % right
    elif op == "div":
        result = left // right
    print(f"result : {result}")
    return NumberVal(result)

def eval_program(program : Program) -> RunTime:
    last_evaluated = NullVal()
    for statement in program.body:
        last_evaluated =  evaluate(statement)
    return last_evaluated


def evaluate(astNode: Statement) -> RunTime:
    if astNode.type == NodeBinaryOperation:
        return eval_binary_operation(astNode)
    elif astNode.type == NodeNumericLiteral:
        return NumberVal(astNode.value)
    elif astNode.type == NodeProgram:
        return eval_program(astNode)
    elif astNode.type == NodeNull:
        return NullVal()
    else: Error("Unvalid returning value") 
