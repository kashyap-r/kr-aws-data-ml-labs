"""
This is the second version of the basic API
"""
from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI() 

class Customer(BaseModel):
    age: int 
    balance: float 
    transactions: int

@app.post("/predict")
def predict(customer: Customer):
    score = (customer.balance / 1000) + customer.transactions * 0.1 
    if score > 10:
        label = "High value"
    else:
        label = "Low Value"
        
    return {
        "score": score,
        "label": label
    }
