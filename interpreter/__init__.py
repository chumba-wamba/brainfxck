"""
- lexer.py
    - <class> Token :: serves as a structure to store metadata such as line number, character number, operator data, etc.
    - <class> Lexer :: generates tokens and populates the brainfxck storage tape with these tokens.
- parser.py
    - <class> Parser :: responsbile for parsing and interpreting the code; generating error messages and other information.

- rules (refer https://gist.github.com/roachhd/dce54bec8ba55fb17d3a)
    - any arbitrary character besides the 8 listed below should be ignored and considered as comments.
    - all the blocks on the memory tape are intialised with a zero and the tape pointer starts from the left-most position. 
    - loops may be nested as many times as one wants but every "[" must have a corresponding "]".

- inforamtion on brainfxck operators
    > :: moves memory pointer to the right of the current position.
    < :: moves memory pointer to the left of the current position.
    + :: increments the memory block value by one.
    - :: decrements the memory block value by one.
    [ :: like c while(cur_block_value != 0) loop.
    ] :: if block currently pointed to's value is not zero, jump back to "[".
    , :: used to input a character.
    . :: used to output a character.
"""

op_dict = {
    ">": "RIGHT_SHIFT",
    "<": "LEFT_SHIFT",
    "+": "INC",
    "-": "DEC",
    "[": "LOOP_OPEN",
    "]": "LOOP_CLOSE",
    ",": "INPUT",
    ".": "OUTPUT"
}

op_list = {
    ">",
    "<",
    "+",
    "-",
    "[",
    "]",
    ",",
    "."
}
