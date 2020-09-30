from requests import get, post
from json import loads, dumps
from typing import Dict


# NOTE - Is to be updated according to the URL at
# which the brainfxck API is hosted at
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
    # The most important aspect of this function; replaces
    # all the newline characters in the file with a raw string
    # containing \n so that it becomes comaptible with JSON and
    # can be evaluated by the API
    code = code.replace("\n", r"\n")

    # Creating a dictionary which is compatible with the
    # body expected by the API and using the dumps method to
    # make it JSON compatible
    data = {'code': code}
    response = post(url+"evaluate", data=dumps(data))

    return loads(response.text)
