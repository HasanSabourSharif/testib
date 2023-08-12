from fastapi import FastAPI, Request
import time
import model
import mlflow
import mlflow.pytorch
global version 
version = 'v1'
global description
description = 'start models'

app = FastAPI(title='MLOps')

@app.middleware("http")
async def measure_execution_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    execution_time = (end_time - start_time)
    print(f"Endpoint '{request.method} {request.url.path}' execution time: {execution_time}s")
    return response


@app.post("/question")
def create_item(question:str):
    print(question)
    return {'quesion': question, "answer": model.getAnswer(question)}

@app.get('/version')
def getVersion():
    global version
    return {'version': version}

@app.put('/metadata')
def setMetadata(metadata:str):
    des = metadata['description']
    ver = metadata['version']
    global version
    version = ver
    global description
    description = des    
    BATCH_SIZE=5
    EPOCHS=10
    with mlflow.start_run() as run:
        mlflow.log_param("model_type", "SimpleNN")
        mlflow.log_param("batch_size", BATCH_SIZE)
        mlflow.log_param("epochs", EPOCHS)
        mlflow.pytorch.log_model(model, "models")


    with mlflow.start_run():
        for epoch in range(0, 3):
            mlflow.log_metric(key="quality", value=2 * epoch, step=epoch)
            mlflow.log_metric(key="accuracy", value=2 * epoch, step=epoch)
            mlflow.log_metric(key="recall", value=2 * epoch, step=epoch)
            mlflow.log_metric(key="precision", value=2 * epoch, step=epoch)
            mlflow.log_metric(key="F1 score", value=2 * epoch, step=epoch)
            mlflow.log_metric()

    return {'version': version, 'description': description}

