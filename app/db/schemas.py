from typing import List
from pydantic import BaseModel
from datetime import datetime


class Post(BaseModel):
    text: str
    created_date: datetime
    rubrics: str

    class Config:
        orm_mode = True
