import typer
from interpreter.interpreter import interpret


def main(file: str):
    output = interpret(file)
    typer.echo(output)


if __name__ == "__main__":
    typer.run(main)
