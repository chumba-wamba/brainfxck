from interpreter import op_dict, op_list
from interpreter.token import Token
from interpreter.lexer import Lexer
from typing import List, Dict


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

    def __init__(self, token_stream: List[Token]) -> Dict[str, int]:
        # A stack to check for the condition written
        # in the class docstring
        self.stack = []
        # A list containing the stream of tokens generated
        # by the lexer.
        self.token_stream = token_stream

    def analyse(self):
        for token in self.token_stream:
            if token.op_name == op_dict.get("["):
                self.stack.append(token)
            elif token.op_name == op_dict.get("]"):
                if len(self.stack) and self.stack[-1].op_name == op_dict.get("["):
                    self.stack = self.stack[:-1]
                else:
                    return {
                        "is_faulty": True,
                        "faulty_token_list": [token],
                    }

        if len(self.stack):
            return {
                "is_faulty": True,
                "faulty_token_list": self.stack
            }
        return {
            "is_faulty": False,
            "faulty_token_list": None
        }
