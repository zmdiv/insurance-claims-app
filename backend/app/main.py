# backend/app/main.py
from fastapi import FastAPI
from app.endpoints import claims, ocr, user

app = FastAPI()

app.include_router(claims.router, prefix="/claims", tags=["claims"])
app.include_router(ocr.router, prefix="/ocr", tags=["ocr"])
app.include_router(user.router, prefix="/user", tags=["user"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Insurance Claims API"}
