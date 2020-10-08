import typer
from interpreter.interpreter import evaluate, read_file


def main(file: str):
    output = (evaluate(read_file(file)))
    typer.echo("fin; brain fxcked? :)")


if __name__ == "__main__":
    typer.run(main)
