from interpreter import op_dict, op_list
from interpreter.token import Token
from interpreter.lexer import Lexer


class SyntaxAnalyser:
    """
        Primarily used to solve a singular purpose 
        of checking whether the "[" operator has a 
        corresponding "]" operator.

        In case the above condition is not satisfied,
        the brainfxck code does not reach the evaluation
        stage and is prematurely stopped with an error
        message. 
    """

    def __init__(self, token_stream: List[Token]) -> None:
        # A stack to check for the condition written
        # in the class docstring
        self.stack = []
        # A list containing the stream of tokens generated
        # by the lexer.
        self.token_stream = token_stream

    def syntax_analyser(self):
        pass
