"""
This is the most basic that the api can get. Just return the message upon invocation

Just run the below command in Command prompt with this file in the current directory
    
    uvicorn main:app --reload

After running the above command, run the below in the browser

    http://127.0.0.1:8000

"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kashyap's first API is working"}    