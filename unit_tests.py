from interpreter import op_dict, op_list
from interpreter.lexer import Lexer
from interpreter.syntax_analyser import SyntaxAnalyser
from interpreter.parser import Parser

if __name__ == "__main__":
    code = "+++++--[[[]c+++++ //Incrementing cell 1 from 0 to 10"

    lex = Lexer(code)
    token_stream = lex.lex()

    print(token_stream, end="\n\n\n")

    syn_anal = SyntaxAnalyser(token_stream=token_stream)
    fault_dict = syn_anal.analyse()

    print(fault_dict)
