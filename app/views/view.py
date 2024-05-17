from fastapi import APIRouter, HTTPException
from app.models.model import ItemRequest, ItemResponse
from app.controllers.controller import add_numbers
import logging

router = APIRouter()

@router.post("/add", response_model=ItemResponse)
async def add_items(request: ItemRequest):
    try:
        logging.info("Request numbers: %s",request.numbers)
        result = add_numbers(request.numbers)
        logging.info("result: %d", result)
        return ItemResponse(result=result)

    except Exception as e:
        logging.error("Error occurred: %s", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")
