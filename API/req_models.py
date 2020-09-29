from fastapi import FastAPI, Body
from pydantic import BaseModel, Field


class CodeIn(BaseModel):
    code: str = Field(...,
                      description="The brainfxck code that has to be evaluated")


class CodeOut(BaseModel):
    output: str = Field(..., description="The output of the brainfxck code")
