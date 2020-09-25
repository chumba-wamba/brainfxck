from interpreter import op_dict, op_list
from interpreter.token import Token
from interpreter.lexer import Lexer
from interpreter.syntax_analyser import SyntaxAnalyser
from interpreter.parser import Parser


def interpret(file):
    if file.split(".")[-1] != "bf":
        return("File extension is not of type brainfxck")

    with open(file) as f:
        code = f.read()

    lexer = Lexer(code)
    token_stream = lexer.lex()

    syntax_analyser = SyntaxAnalyser(token_stream)
    error_dic = syntax_analyser.analyse()
    if error_dic["is_faulty"]:
        op_string = ""
        for token in error_dic["faulty_token_list"]:
            op_string += (
                f"Error for {token.op_name} at :: line : {token.line_number} position : {token.posn_number}\n")
        return op_string

    parser = Parser(token_stream)
    parser.parse()
    output = parser.output_string
    return output
