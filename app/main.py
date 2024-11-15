from fastapi import FastAPI
from .routers import auth



app=FastAPI()

@app.get("/")
def welcome_to_api():
    return {"Message":"Welcome to Ticket Management API.."}

