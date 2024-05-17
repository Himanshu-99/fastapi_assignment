from pydantic import  BaseModel
from typing import List

class ItemRequest(BaseModel):
    numbers: List[int]

class ItemResponse(BaseModel):
    result: int