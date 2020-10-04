# Brainfxck

[![](https://img.shields.io/badge/BUILT%20FOR-WEB-blue?style=for-the-badge&logo=Google-Chrome&labelColor=000000&color=4285F4&logoColor=4285F4)](https://flask.palletsprojects.com/en/1.1.x/) [![](https://img.shields.io/badge/MADE%20USING-Python-blue?style=for-the-badge&logo=python&labelColor=000000&color=blue&logoColor=ffffff)](https://flask.palletsprojects.com/en/1.1.x/) [![](https://img.shields.io/badge/IDE-VISUAL%20STUDIO%20CODE-blue?style=for-the-badge&logo=visual-studio-code&labelColor=000000&color=007ACC&logoColor=ffffff)](https://code.visualstudio.com/)

An interpreter for the esoteric programming language - brainf\*ck written in Python. The project includes a CLI, API (with the intention of building an online platform to execute brainfxck code), and a visualiser for the extremely convoluted language (in development).

To do:

- Draw sequence, architecture, and/or use-case diagrams.
- Code the interpreter (lexer, syntax analyser, parser). ✔
- Code the basic API (might still need to add some endpoints). ✔
- Design and code the front-end for the visualiser + online execution platform.
- Optimise the evaluation (Peephole optimisation).

## Understanding Brainfxck

- token.py
  - <class> Token :: serves as a structure to store metadata such as line number, character number, operator data, etc.
- lexer.py
  - <class> Lexer :: generates tokens and populates the brainfxck storage tape with these tokens.
- parser.py

  - <class> Parser :: responsbile for parsing and interpreting the code; generating error messages and other information.

- rules (refer https://gist.github.com/roachhd/dce54bec8ba55fb17d3a for a more exhaustive study of brainfxck)

  - any arbitrary character besides the 8 listed below should be ignored and considered as comments.
  - all the blocks on the memory tape are intialised with a zero and the tape pointer starts from the left-most position.
  - loops may be nested as many times as one wants but every "[" must have a corresponding "]".

- inforamation on brainfxck operators
  - \> :: moves memory pointer to the right of the current position.
  - < :: moves memory pointer to the left of the current position.
  - \+ :: increments the memory block value by one.
  - \- :: decrements the memory block value by one.
  - [ :: like c while(cur_block_value != 0) loop.]
  - ] :: if block currently pointed to's value is not zero, jump back to "[".
  - , :: used to input a character.
  - . :: used to output a character.

## Installation and General Instructions

Follow the steps to run the web-app on your local machine:

1. Clone the repository

   ```shell
   git clone https://github.com/chumba-wamba/brainfxck.git
   ```

2. Install the Dependencies

   ```shell
   cd brainfxck
   pip install -r requirements.txt
   ```

3. Run the test.py file

   ```shell
   cd python3 test.py
   ```

4. To use the API (Optional)

   1. Start the server

   ```shell
   cd API
   uvicorn server:app --reload
   ```

   2. Open a browser
   3. Visit @http://localhost:8000/docs or @http://localhost:8000/redoc

5. Recommened to user the api_client for python (solves JSON parsing issues)
6. To use the CLI (Optional)

   1. Enter the CLI dircetory and run the following command

   ```shell
     cd CLI
     python3 brainfxck.py location_of_file.bf
   ```
