from fastapi import FastAPI
app = FastAPI()

@app.get("/ii/")
def read_root():
    return {"هدف": "سامانه پاسخگویی به سوالات شرعی"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    
    return {"item_id": item_id ,"q": q}


@app.post("/Q")
async def create_item(qu:str):
    print(qu)

    return {"item": qu}


