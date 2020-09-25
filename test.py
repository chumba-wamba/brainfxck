from interpreter import op_dict, op_list
from interpreter.lexer import Lexer
from interpreter.syntax_analyser import SyntaxAnalyser
from interpreter.parser import Parser
from interpreter.getch import interpret

if __name__ == "__main__":
    op = interpret(
        file="/home/adminuser/Desktop/projects/brainfxck/examples/faulty_brace.bf")
    print(op)
