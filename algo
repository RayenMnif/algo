#!/usr/bin/env python3

from rich import print
from runtime.environment import setup_global_env
from src.parser import *
from src.lexer import * 
from sys import argv, exit
from runtime.interpreter import *

"""
    sorry for the bad code that i wrote :')
                                 - Rayen Mnif 
"""

def main():

    dev = True

    env = setup_global_env()

    if len(argv) not in [2, 1]:
        print("Usage: algo [script]")
        exit(0)

    if len(argv) == 2:
        try:
            with open(argv[1], "r") as script:
                src = script.read()
                program = Parser(src).produce_ast()
                if dev:
                    print(program)
                    print("-----------------------------")
                evaluate(program, env)
        except FileNotFoundError: Error(f"fichier non valide: on ne peut pas trouver le fichier '{argv[1]}'")
        except KeyboardInterrupt: exit(0)
        except EOFError: exit(0)

    else:
        print(""" 
         ▄▄▄       ██▓      ▄████  ▒█████  
        ▒████▄    ▓██▒     ██▒ ▀█▒▒██▒  ██▒
        ▒██  ▀█▄  ▒██░    ▒██░▄▄▄░▒██░  ██▒
        ░██▄▄▄▄██ ▒██░    ░▓█  ██▓▒██   ██░
        ▓█   ▓██▒░██████▒░▒▓███▀▒░ ████▓▒░
        ▒▒   ▓▒█░░ ▒░▓  ░ ░▒   ▒ ░ ▒░▒░▒░ 
         ▒   ▒▒ ░░ ░ ▒  ░  ░   ░   ░ ▒ ▒░ 
         ░   ▒     ░ ░   ░ ░   ░ ░ ░ ░ ▒  
             ░  ░    ░  ░      ░     ░ ░  
                                          
     Tunisian shitty pseudo/programming language

    Type "exit", "quit" to quit 
         "help", "credits" for more information

    Algo v0.0.1 (Beta)
    """)
        while True:
            try:
                prompt = input(">> ")
                if prompt.upper() in ["EXIT", "QUIT"]: exit()
                if prompt.upper() == "CREDITS": print("project by Rayen Mnif")
                if prompt.upper() == "HELP": print("the docs are not available at the moment")
                program = Parser(prompt).produce_ast()
                if dev:
                    print(program)
                    print("------------------------------------")
                print(evaluate(program, env))
            except KeyboardInterrupt:
                exit()
            except EOFError:
                exit()


if __name__ == "__main__":
    main()
