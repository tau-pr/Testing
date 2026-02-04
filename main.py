from fastapi import FastAPI

app = FastAPI()

@app.get("/aman")
def hello():
    return {"message": "this is my first api"}


@app.get("/back")
def hellova():
    return{"message_1":"this is core back whole "}