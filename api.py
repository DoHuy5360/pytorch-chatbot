from fastapi import FastAPI, Depends
from pydantic import BaseModel
from chat import getAnswer

app = FastAPI()

class QueryIn(BaseModel):
    q: str

class QueryParams(BaseModel):
    q: str

class ResponseOut(BaseModel):
    a: str

@app.get("/")
def ping():
    return "pong"

@app.get("/ai")
def ping(params: QueryParams = Depends()):
    question = params.q

    print(question)

    answer = getAnswer(question)

    response = ResponseOut(a=answer)
    return response

@app.post("/ai")
def handle_ai_request(query: QueryIn):
    question = query.q

    response = ResponseOut(a="xyz")
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)