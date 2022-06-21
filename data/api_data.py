from pydantic import BaseModel


class AccountsData(BaseModel):
    user_name: str
    password: str

