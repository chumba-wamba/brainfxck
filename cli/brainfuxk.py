import typer
from interpreter.interpreter import evaluate


def main(file: str):
    output = evaluate(file)
    typer.echo(output)


if __name__ == "__main__":
    typer.run(main)
