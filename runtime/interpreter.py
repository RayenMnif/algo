from runtime.environment import Environment
from src.utils import *
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
    if left.type in [MatriceValue, TableauValue]:
        left = get_data_structure_value(left)
    if right.type in [MatriceValue, TableauValue]:
        right = get_data_structure_value(right)
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
        else: Error("les op 'ou' et 'et' sont seulement pour les bouleean (vrai/faux)")
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
    if left.type == StringValue and right.type == StringValue:
        return eval_string_binary_expression(left, right, binop.op)
    return NullVal()


def eval_string_binary_expression(LeftOp: StringVal, RightOp: StringVal, op) -> StringVal:
    left = LeftOp.value
    right = RightOp.value
    if op == "+": result = left + right
    elif op == "-": 
        Error("Unvalid operation for strings")
    elif op == "*": 
        Error("Unvalid operation for strings")
    elif op == "/":
        Error("Unvalid operation for strings")
    elif op in ["mod", "Mod"]: 
        Error("Unvalid operation for strings")
    elif op in ["Div", "div"]:
        Error("Unvalid operation for strings")
    return StringVal(result)


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
    elif op in ["mod", "Mod"]: result = left % right
    elif op in ["Div", "div"]:
        if right == 0:
            Error("ZeroDivisionError: division by zero")
        result = left // right
    return NumberVal(result)

def eval_program(program : Program, env: Environment) -> RunTime:
    last_evaluated = NullVal()
    for statement in program.body:
        last_evaluated =  evaluate(statement, env)
    return last_evaluated

def get_data_structure_value(ds: MatriceVal | TableauVal):
    if ds.pos != None:
        return ds.value[ds.pos[0]][ds.pos[1]] if ds.type == MatriceValue else ds.value[ds.pos]
    else:
        Error(f"If faut specifier les paramametre pour {"la matrice" if ds.type == MatriceValue else "le tableau"} '{ds.name}'")


def eval_Var(var: Indentifier, env: Environment) -> RunTime:
    return env.lookUpVar(var.name)

def eval_assignment(assig: Assignment, env: Environment):
    if assig.var.type != NodeIndentifier: 
        # assigning data structures (matrice/tableau)
        evaluated_assignee = evaluate(assig.var, env)
        if evaluated_assignee.type in [MatriceValue, TableauValue]:
            if evaluated_assignee.pos != None:
                evaluated_value = evaluate(assig.value, env)
                if evaluated_assignee.type == MatriceValue:
                    evaluated_assignee.value[evaluated_assignee.pos[0]][evaluated_assignee.pos[1]] = get_data_structure_value(evaluated_value) if evaluated_value.type in [MatriceValue, TableauValue] else evaluated_value
                else:
                    evaluated_assignee.value[evaluated_assignee.pos] = get_data_structure_value(evaluated_value) if evaluated_value.type in [MatriceValue, TableauValue] else evaluated_value
                return env.assignVar(evaluated_assignee.name, MatriceVal(evaluated_assignee.name, evaluated_assignee.value) if evaluated_assignee.type == MatriceValue else TableauVal(evaluated_assignee.name, evaluated_assignee.value))
            else:
                Error(f"on dirait que vous attribuez la {"matrice" if evaluated_assignee.type == MatriceValue else "tableau"} '{assig.var}' de manière incorrecte")
        else:
            Error(f"on dirait que vous attribuez la variable '{assig.var}' de manière incorrecte")
    return env.assignVar(assig.var.name, evaluate(assig.value, env))

def eval_block_statement(block: BlockStatemnt, env: Environment) -> RunTime:
    last_evaluated = NullVal()
    for statement in block.body:
        if statement.type == NodeReturn:
            return evaluate(statement.value, env)
        last_evaluated = evaluate(statement, env)
    return last_evaluated

def eval_loop_tantque_repeter(loop: loopTantqueRepeter, env: Environment) -> RunTime:
    loop_env = Environment(env)
    if not loop.tant_que:
        evaluate(loop.stmnt, loop_env)
        while not is_true(loop.condition, loop_env):
            evaluate(loop.stmnt, loop_env)
    else:
        while is_true(loop.condition, loop_env):
            evaluate(loop.stmnt, loop_env)
    return NullVal()

def eval_for_loop(loop: forLoop, env: Environment) -> RunTime:
    loop_env = Environment(env)
    interval = [evaluate(num, env) for num in loop.interval]
    i = interval[0].value
    loop_env.assignVar(loop.var_name, NumberVal(i))
    if interval[1].value < interval[0].value:
        Error("Erreur de la plage de boucle pour: la valueur initial est plus que la valeur final")
    if len(interval) == 3:
        if interval[2].value > interval[1].value:
            Error("Erreur de la plage de boucle pour: la valeur du pas est plus grand que la valueur final")
    while i != int(interval[1].value + 1):
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
    if caller.type not in [NativeFnvalue, FunctionValue, ProcedureValue] : Error("You can only call functions")
    if caller.type == NativeFnvalue:
        result = caller.call([evaluate(arg, env) for arg in function.args], env)
    elif caller.type in [FunctionValue, ProcedureValue]:
        func_env = Environment(env)
        # looking for matrice et tableau for predefining them
        if len(caller.param) != len(function.args):
            Error(f"FunctionError: number of args not matching in function '{caller.name}' ")

        for i in range(len(caller.param)):

            if function.args[i].type == NodeIndentifier:

                if caller.param[i][1] in ["Mat", "matrice"]:
                    if not env.available(function.args[i].name):
                        env.assignVar(function.args[i].name, MatriceVal(function.args[i].name, [[NullVal()]]))

                if caller.param[i][1] in ["Tab", "tableau"]:
                    if not env.available(function.args[i].name):
                        env.assignVar(function.args[i].name, TableauVal(function.args[i].name, [NullVal()]))

                if caller.param[i][1] == "entier":
                    if not env.available(function.args[i].name):
                        env.assignVar(function.args[i].name, NumberVal(0))

                if caller.param[i][1] in ["reel", "réel"]:
                    if not env.available(function.args[i].name):
                        env.assignVar(function.args[i].name, NumberVal(0.0))

                if caller.param[i][1] in ["chaine", "chaine_de_caractere", "chaine_de_caractère"]:
                    if not env.available(function.args[i].name):
                        env.assignVar(function.args[i].name, StringVal(""))


        # evaluating call args 
        args = [evaluate(arg, env) for arg in function.args]
        # assigning variables in the function scope (environment)
        for i in range(len(args)):
            func_env.assignVar(caller.param[i][0], args[i])
        check_parameters(caller.param, func_env)
        func_return = evaluate(caller.body , func_env)
        if caller.type == FunctionValue:
            if func_return.type != VarValues[caller.return_type]:
                Error(f"la valeur de retour de la fonction '{caller.name}' ne correspond pas")
            return func_return
        return NullVal()
    return result

def eval_fonction(function: Function, env: Environment) -> RunTime:
    return env.assignVar(function.callee.name, FunctionVal(function.callee.name, function.parameters, function.statement, function.return_type, env))
    
def eval_procedure(function: Function, env: Environment) -> RunTime:
    return env.assignVar(function.callee.name, ProcedureVal(function.callee.name, function.parameters, function.statement, env))

def check_parameters(parameters, env):
    """ checks the parameters types retunrs an error if parameter type not matching"""
    for param, paramType in parameters:
        if env.lookUpVar(param).type != VarValues[paramType]:
            Error(f"la valeur de paramètere '{param}' ne correspond pas, le parametere '{param}' doit etre de type '{paramType}'")
        if isinstance(env.lookUpVar(param).value, int) and paramType != "entier":
            Error(f"la valeur de paramètere '{param}' ne correspond pas, le parametere '{param}' doit etre de type '{paramType}'")
        if isinstance(env.lookUpVar(param).value, float) and paramType not in ["reel", "réel"]:
            Error(f"la valeur de paramètere '{param}' ne correspond pas, le parametere '{param}' doit etre de type '{paramType}'")

def eval_ds_call(call: DsCall, env: Environment):
    arguments = call.args
    args = []
    for arg in arguments:
        evaluated_agrument =  evaluate(arg ,env)
        if evaluated_agrument.type != NumberValue and not isinstance(evaluated_agrument.value, int):
            Error(f"type d'argument est invalide '{args[0].type}' dans structure '{DsCall.callee.name}', le argument doit etre un  entier")
        args.append(evaluated_agrument)
    # args 
    i = args[0].value
    if len(args) == 2:
        j = args[1].value
    # matrice
    if len(args) == 2:
        matrice = env.lookUpVar(call.callee.name)
        if matrice.type == TableauValue:
            Error(f"'{matrice.name}' est un tableau, c'est pas une matrice")
        if len(matrice.value) < (i + 1):
            for a in range(((i + 1) - len(matrice.value))):
                matrice.value.append([NullVal()])
        try:
            if len(matrice.value[i]) < (j + 1):
                for a in range(((j + 1) - len(matrice.value[i]))):
                    matrice.value[i].append(NullVal())
        except TypeError: Error(f"you didn't specify the parameters in the matrice '{matrice.name}'")
        matrice.pos = i, j 
        env.assignVar(call.callee.name, matrice)
        return matrice
    # tableau
    else :
        tableau = env.lookUpVar(call.callee.name)
        if tableau.type == MatriceValue:
            Error(f"'{tableau.name}' est une matrice, c'est pas un tableau")
        while len(tableau.value) < ( i + 1 ) :
            tableau.value.append([NullVal()]*(i - len(tableau.value) ))
        tableau.pos = args[0].value
        env.assignVar(call.callee.name, tableau)
        return tableau


def evaluate(astNode: Statement, env: Environment) -> RunTime:
    if astNode.type == NodeBinaryOperation: return eval_binary_operation(astNode, env)
    elif astNode.type == NodeAssignment: return eval_assignment(astNode, env)
    elif astNode.type in [NodeReel, NodeEntier]: return NumberVal(astNode.value)
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
    elif astNode.type == NodeFunction: return eval_fonction(astNode, env)
    elif astNode.type == NodeProcedure: return eval_procedure(astNode, env)
    elif astNode.type == NodeDSCall: return eval_ds_call(astNode, env)
    else: Error(f"Unvalid returning value (ast node : {astNode})")
