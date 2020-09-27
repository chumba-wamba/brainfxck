from interpreter.interpreter import evaluate

if __name__ == "__main__":
    op = evaluate(
        file="/home/adminuser/Desktop/projects/brainfxck/examples/fib.bf", tape_size=1000)
    print(op)
