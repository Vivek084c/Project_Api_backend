#importing the libraries
import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
from regModel import regression



#creating the app object from fastapi
app=FastAPI()
# pickle_in=open("model.pkl","rb")
# regression=pickle.load(pickle_in)

#setting up the routes
@app.get("/")
def test():
    return {"message":"default rount working properly"}

@app.get("/Welcome")
def testRoute(name:str):
    return {"details":f"hellow, {name} welcome tho this liner regression model"}

#route to pridict the output
@app.post("/pridict")
def pridict_output(data):
    return {"value is ":regression.predict([[5]])}

#running the app
if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)
    