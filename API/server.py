from fastapi import FastAPI, Path, Query, Body
from typing import Optional, List, Dict, Tuple
from interpreter.interpreter import evaluate


app = FastAPI()


@app.get("/")
def root():
    return {
        "success": True,
        "message": "An API to interpret your brainfxck code!",
        "data": {}
    }


@app.post("/evaluate")
def evaluate():
    pass
