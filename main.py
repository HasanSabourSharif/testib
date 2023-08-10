from fastapi import FastAPI
import model
app = FastAPI()

@app.post("/question")
async def create_item(question:str):
    return {'quesion': question, "answer": model.getAnswer(question)}
