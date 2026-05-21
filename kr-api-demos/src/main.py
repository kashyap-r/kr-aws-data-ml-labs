from fastapi import FastAPI 
from fastapi import HTTPException
from pydantic import BaseModel 
import joblib 
import logging


logging.basicConfig(level=logging.INFO)

app = FastAPI() 

class Customer(BaseModel):
    age: int 
    balance: float 
    transactions: int

# model = joblib.load('model.pkl')
model = joblib.load(r"D:\MyGitHubSource\kr-api-demos\src\model.pkl")

@app.post("/predict")
def predict(customer: Customer):
    logging.info("Received request: {customer}")
    features = [[customer.age, customer.balance, customer.transactions]]
    prediction = model.predict(features)[0]
    if customer.balance < 0:
        raise HTTpException(status_code=400, detail="Invalid Balance")
        
    return { "prediction": int(prediction)}
