class Token:
    """
        Class for defining a token which stores the
        name of the token as specified in the 'op_dict'
        dictionary within the __init__.py file, the 
        line number where the token exists, and the position
        of the token within that file.

        Serves as the base class for the stream of tokens
        that are to be generated upon lexical analysis of
        the input code.

            Attributes:
                op_name : str
                    name of the token.
                line_number : int
                    the line in the code where the token exists.
                posn_number : int
                    the position number of the line in which the token exists.

            Methods:
                __repr__ ()
                    prints the token object in a human readable format.

    """

    def __init__(self, op_name: str, line_number: int, posn_number: int) -> None:
        """
            Constructor method to store the operator name, line 
            number, and the position number of a character.

            Parameters:
                op_name : str
                    name of the token operator.
                line_number : int
                    the line in the code where the token exists.
                posn_number : int
                    the position number of the line in which the token exists.

            Returns:
                None
        """
        self.op_name = op_name
        self.line_number = line_number
        self.posn_number = posn_number

    def __repr__(self) -> str:
        """
            __repr__ method to print the contents of a token object
            insted of the id whenever the object is referenced in
            the code. 

            Parameters:
                None

            Returns:
                str
        """
        return f"Token(op_name: {self.op_name}, line_number: {self.line_number}, posn_number: {self.posn_number})"
