from requests import get, post
from json import loads, dumps
from typing import Dict


url = "http://localhost:8000/"


def get_root():
    """
        I am not even going to bother to describe this. :)
    """
    return loads(get(url).text)


def eval_code(file: str) -> str:
    """
        Helper function which reads the contents of the input file,
        parses it to a json and then is sent as the body of a post
        request to the brainfxck evaluator API.

        Parameters:
            file : str
                the location of the .bf file to be evaluated.

        Returns:
            str
    """
    if file.split(".")[-1] != "bf":
        raise ValueError("File extension is not of type brainfxck")

    with open(file) as f:
        code = f.read()
    code = code.replace("\n", r"\n")

    data = {'code': code}
    response = post(url+"evaluate", data=dumps(data))

    return loads(response.text)
