from fastapi import FastAPI, APIRouter
from .router import products 

app = FastAPI()
app.include_router(products.router)

@app.get("/")
async def read_root():
    """Root endpoint for the API.

    Returns:
        _type_: str
    """
    return {"Hello": "World"}