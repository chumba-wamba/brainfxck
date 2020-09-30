from fastapi import FastAPI, Path, Query, Body
from typing import Optional, List, Dict, Tuple
from interpreter.interpreter import evaluate
from API.req_models import *

app = FastAPI()


@app.get("/")
def root():
    """
        End point to send a simple response to any get
        request; the main purpose of this is to check 
        whether the API is up and running or not.
    """

    return {
        "success": True,
        "message": "An API to interpret your brainfxck code!",
        "data": {}
    }


@app.post("/evaluate")
def eval(code_in: CodeIn):
    """
        End point to evaluate the brainfxck code that is
        recieved as a post request with the help of the
        interpreter.interpreter.evaluate function.
    """

    output = evaluate(code_in.code)
    return {
        "success": True,
        "message": "Code successfully evaluated by the interpreter.",
        "data": CodeOut(output=output)
    }
