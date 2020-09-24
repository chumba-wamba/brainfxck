from interpreter import op_dict, op_list
from interpreter.token import Token
from interpreter.syntax_analyser import SyntaxAnalyser
from interpreter.lexer import Lexer
from typing import List


class Parser:
    def __init__(self, token_stream: List[Token], tape_size: int = 1000) -> None:
        self.token_stream = token_stream
        self.tape = [0 for i in range(tape_size)]
        self.tape_ptr = 0

    def parse(self):
        pass
