from fastapi import FastAPI, Request
import time
import model

app = FastAPI(
    title='MLOps', debug=True,
)

@app.middleware("http")
async def measure_execution_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    execution_time = (end_time - start_time)
    print(f"Endpoint '{request.method} {request.url.path}' execution time: {execution_time}s")
    return response


@app.post("/question")
async def create_item(question:str):
    return {'quesion': question, "answer": model.getAnswer(question)}
