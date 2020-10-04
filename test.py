from interpreter.interpreter import read_file, evaluate

if __name__ == "__main__":
    op = evaluate(
        read_file(file="/home/adminuser/Desktop/projects/brainfxck/examples/pow.bf"), tape_size=1000)
    print(op)
