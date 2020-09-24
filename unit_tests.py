from interpreter import op_dict, op_list
from interpreter.lexer import Lexer
from interpreter.syntax_analyser import SyntaxAnalyser
from interpreter.parser import Parser

if __name__ == "__main__":
    code = "+++++--[[[]c+++++ //Incrementing cell 1 from 0 to 10"
    lex = Lexer(code)
    token_list = lex.lex()
    for token in token_list:
        print(token.op_name)
    syn_anal = SyntaxAnalyser(token_list)
    fault_dict = syn_anal.analyse()
    print(fault_dict["faulty_token_list"])
    for token in fault_dict["faulty_token_list"]:
        print(token.op_name, token.line_number, token.posn_number)
