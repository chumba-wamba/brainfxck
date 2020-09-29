from fastapi import FastAPI, Path, Query, Body
from typing import Optional, List, Dict, Tuple
from interpreter.interpreter import evaluate
from API.req_models import *

app = FastAPI()


@app.get("/")
def root():
    return {
        "success": True,
        "message": "An API to interpret your brainfxck code!",
        "data": {}
    }


@app.post("/evaluate")
def eval(code_in: CodeIn):
    output = evaluate(code_in.code)
    return {
        "success": True,
        "message": "Code successfully executed!",
        "data": CodeOut(output=output)
    }
