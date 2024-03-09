from fastapi import FastAPI
import pickle


#creating the instance of fast api app

app=FastAPI()

pickle_in=open("multipleLinearRegression.pkl","rb")
regression=pickle.load(pickle_in)

#setting up the rouyers
@app.get("/vivi")
def test():
    return {"details": " this is the test route"}

@app.post("/vivek")
def predict(Low_price,Close_price,WAP,Spread_High_Low):
    prediction=regression.predict([[float(Low_price),float(Close_price),float(WAP),float(Spread_High_Low)]])
    return {"the predicted value is ":f"here is the predictions {prediction}"}
    


