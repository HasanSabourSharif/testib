from fastapi import FastAPI, Request
import time
import model
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
    return {'version': version, 'description': description}

