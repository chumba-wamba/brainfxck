from interpreter import op_dict, op_list
from interpreter.token import Token
from typing import List


class Lexer:
    """
        Responsible for generating a stream of tokens 
        from the input code which is then passed onto
        the parser for futher evaluation (intepretation).

            Attributes:
                code : str
                    the brainfxck code that has to be interpreted.

            Methods:
                lex()
                    generates the token stream from the input code.
    """

    def __init__(self, code: str) -> None:
        """
            Constructor method to store code as an instance variable.

            Parameters:
                code : str
                    the input code.

            Returns:
                None
        """

        # Splitting input code into lines (via "\n" delimiter)
        self.code = code.split("\n")
        # Instance variable to store the stream of tokens generated
        # by the lexer
        self.token_stream = []

    def lex(self) -> List[Token]:
        """
            Method to generate tokens from the input code.

            Parameters:
                None

            Returns:
                List[Token]
        """

        # Initialising the line and the posn ptr so that these
        # variables can be utilised by the instances of the Token
        # class
        line_ptr = 1
        for line in self.code:
            posn_ptr = 1
            for char in line:
                if char in op_list:
                    # Generating an object of the Token class for the current
                    # character
                    # Any character apart from the ones present in the op_list
                    # will be neglected and considered as a comment (as specified
                    # in the rules in the __init__.py file)
                    token = Token(op_dict.get(char), line_ptr, posn_ptr)
                    self.token_stream.append(token)
                posn_ptr += 1
            line_ptr += 1

        return self.token_stream
