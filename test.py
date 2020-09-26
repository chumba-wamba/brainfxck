from interpreter.getch import interpret

if __name__ == "__main__":
    op = interpret(
        file="/home/adminuser/Desktop/projects/brainfxck/examples/fib.bf", tape_size=1000)
    print(op)
