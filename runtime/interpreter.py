from runtime.environment import Environment
from src.utils import Error
from runtime.value import *
from src.ast import *


def is_true(condition, env):
    return eval_boolean_operation(condition, env).value


def eval_if_statement(ifStmnt: ifStatement, env: Environment) -> RunTime:
    for condition, statement in ifStmnt.cases:
        if is_true(condition, env):
            return evaluate(statement, env)
    if ifStmnt.else_case:
        return evaluate(else_case, env)


def eval_boolean_operation(bo: BooleanOperation, env: Environment) -> RunTime:
    left = evaluate(bo.LeftOp, env)
    right = evaluate(bo.RightOp, env)
    op = bo.op
    if right.type == NumberValue and left.type == NumberValue:
        left = left.value
        right = right.value
        if op == ">": result = left > right
        elif op == "<": result = left < right
        elif op == ">=": result = left >= right
        elif op == "<=": result = left <= right
        elif op == "=": result = left == right
        elif op == "!=": result = left != right
        else: Error("or, et works only with bools")
    else:
        left = left.value
        right = right.value
        if op == "ou": result = left or right
        elif op == "et": result = left and right
        elif op == "=": result = left == right
        elif op == "!=": result = left != right
        else: Error("You can only compare Numeric values")
    return BooleanVal(result)
        

def eval_binary_operation(binop: BinaryOperation, env: Environment) -> RunTime:
    left = evaluate(binop.LeftOp, env)
    right = evaluate(binop.RightOp, env)
    if left.type == NumberValue and right.type == NumberValue:
        return eval_numeric_binary_expression(left, right, binop.op)
    return NullVal()


def eval_numeric_binary_expression(LeftOp: NumberVal, RightOp: NumberVal, op) -> NumberVal:
    left = LeftOp.value
    right = RightOp.value
    if op == "+": result = left + right
    elif op == "-": result = left - right
    elif op == "*": result = left * right
    elif op == "/":
        if right == 0:
            Error("ZeroDivisionError: division by zero")
        result = left / right
    elif op == "mod": result = left % right
    elif op == "div":
        if right == 0:
            Error("ZeroDivisionError: division by zero")
        result = left // right
    return NumberVal(result)

def eval_program(program : Program, env: Environment) -> RunTime:
    last_evaluated = NullVal()
    for statement in program.body:
        last_evaluated =  evaluate(statement, env)
    return last_evaluated


def eval_Var(var: Indentifier, env: Environment) -> RunTime:
    return env.lookUpVar(var.name)

def eval_assignment(assig: Assignment, env: Environment):
    if assig.var.type != NodeIndentifier: Error(f"Looks like you're wrongly assigning the variable")
    return env.assignVar(assig.var.name, evaluate(assig.value, env))

def eval_block_statement(block: BlockStatemnt, env: Environment) -> RunTime:
    last_evaluated = NullVal()
    for statement in block.body:
        last_evaluated = evaluate(statement, env)
    return last_evaluated

def eval_loop_tantque_repeter(loop: loopTantqueRepeter, env: Environment) -> RunTime:
    if not loop.tant_que:
        evaluate(loop.stmnt, env)
        while not is_true(loop.condition, env):
            evaluate(loop.stmnt, env)
    else:
        while is_true(loop.condition, env):
            evaluate(loop.stmnt, env)
    return NullVal()

def eval_for_loop(loop: forLoop, env: Environment) -> RunTime:
    loop_env = Environment(env)
    interval = [evaluate(num, env) for num in loop.interval]
    i = interval[0].value
    loop_env.assignVar(loop.var_name, NumberVal(i))
    if interval[1].value < interval[0].value:
        Error("Error in loop range : starting value is bigger than ending value")
    if interval[2].value > interval[1].value:
        Error("Error in loop range : pas value is bigger than ending value")
    while i != int(interval[1].value):
        evaluate(loop.stmnt, loop_env)
        if len(interval) == 3:
            i += int(interval[2].value)
            loop_env.assignVar(loop.var_name, NumberVal(i))
        else:
            i += 1
            loop_env.assignVar(loop.var_name, NumberVal(i))
    return NullVal()
    
def eval_call_expression(function: CallExpresstion, env: Environment) -> RunTime:
    caller : NativeFnVal = evaluate(function.callee, env) 
    if caller.type != NativeFnvalue : Error("You can only call functions")
    result = caller.call([evaluate(arg, env) for arg in function.args])
    return result

def evaluate(astNode: Statement, env: Environment) -> RunTime:
    if astNode.type == NodeBinaryOperation: return eval_binary_operation(astNode, env)
    elif astNode.type == NodeAssignment: return eval_assignment(astNode, env)
    elif astNode.type == NodeNumericLiteral: return NumberVal(astNode.value)
    elif astNode.type == NodeString: return StringVal(astNode.value)
    elif astNode.type == NodeProgram: return eval_program(astNode, env)
    elif astNode.type == NodeNull: return NullVal()
    elif astNode.type == NodeIndentifier: return eval_Var(astNode, env)
    elif astNode.type == NodeIfStatement: return eval_if_statement(astNode, env)
    elif astNode.type == NodeBooleanOperation: return eval_boolean_operation(astNode, env)
    elif astNode.type == NodeBlockStatement: return eval_block_statement(astNode, env)
    elif astNode.type == NodeLoopTantqueRepeter: return eval_loop_tantque_repeter(astNode, env)
    elif astNode.type == NodeCallExpresstion: return eval_call_expression(astNode, env)
    elif astNode.type == NodeForLoop: return eval_for_loop(astNode, env)
    else: Error("Unvalid returning value") 
