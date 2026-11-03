"""
Introduction de mon code
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="titre")

class MaClasse(BaseModel):
    """Schema de données par exemple"""
    text : str

@app.get("/")
async def root():
    """Route principale de l'api"""
    return {"message":"Hello World"}