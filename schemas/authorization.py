import datetime
from pydantic import BaseModel


class BadResponse(BaseModel):
    code: int
    message: str


class GenerateTokenSuccess(BaseModel):
    token: str
    expires: str
    status: str
    result: str
