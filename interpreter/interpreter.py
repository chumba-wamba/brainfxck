from interpreter import op_dict, op_list
from interpreter.token import Token
from interpreter.lexer import Lexer
from interpreter.syntax_analyser import SyntaxAnalyser
from interpreter.parser import Parser


def read_file(file: str) -> str:
    """
        Helper function which reads the contents of the input file
        and returns the brainfxck code if the file has a .bf extension.

        Parameters:
            file : str
                the location of the .bf file to be evaluated. 

        Returns:
            str
    """

    if file.split(".")[-1] != "bf":
        raise ValueError("File extension is not of type brainfxck")

    with open(file) as f:
        code = f.read()
    return code


def evaluate(code: str, tape_size: int = 1000) -> str:
    """
            Helper function which combines the process of lexing,
            syntax analysis, and parsing/evaluation to return either
            the finaly output or an error message.

            Parameters:
                code : str
                    the brainfxck code to be evaluated. 

            Returns:
                str
        """
    lexer = Lexer(code)
    token_stream = lexer.lex()

    syntax_analyser = SyntaxAnalyser(token_stream)
    error_dic = syntax_analyser.analyse()
    if error_dic["is_faulty"]:
        op_string = "\n"
        for token in error_dic["faulty_token_list"]:
            op_string += (
                f"Error for {token.op_name} at :: line : {token.line_number} position : {token.posn_number}\n")
        return op_string

    parser = Parser(token_stream, tape_size)
    parser.parse()
    output = parser.output_string
    return output
