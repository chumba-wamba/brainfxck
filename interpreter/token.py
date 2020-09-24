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
    """

    def __init__(self, op_name: str, line_number: int, posn_number: int) -> None:
        """
            Constructor method to store the operator name, line 
            number, and the position number of a character.
        """
        self.op_name = op_name
        self.line_number = line_number
        self.posn_number = posn_number

    def __repr__(self):
        """
            __repr__ method to print the contents of a token object
            insted of the object id whenever the object is called. 
        """
        return f"Token(op_name: {self.op_name}, line_number: {self.line_number}, posn_number: {self.posn_number})"
