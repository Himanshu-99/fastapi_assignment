from fastapi import FastAPI
from app.views.view import router as item_router

app = FastAPI()

app.include_router(item_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)