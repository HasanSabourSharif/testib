from fastapi import FastAPI
app = FastAPI()
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.models import load_model
import numpy as np


model = load_model('mnist_model.h5')


(x_test, y_test) = mnist.load_data()[1]
x_test = x_test / 255.0


num_samples = 5
random_indices = np.random.choice(x_test.shape[0], num_samples, replace=False)
images = x_test[random_indices]


predictions = model.predict(images)


@app.get("/testi/")
def read_root():
    k=[]
    for i in range(num_samples):
        predicted_label = np.argmax(predictions[i])
        actual_label = y_test[random_indices[i]]
    k.append(f"Predicted: {predicted_label}, Actual: {actual_label}")

    return k

@app.get("/mtesti/")
def read_root():
    
    return 

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    
    return {"item_id": item_id ,"q": q}


@app.post("/Q")
async def create_item(qu:str):
    print(qu)

    return {"item": qu}


