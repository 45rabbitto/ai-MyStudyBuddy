from fastapi import FastAPI
from pydantic import BaseModel

from inference import summarize

app = FastAPI()

class SummaryRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize_endpoint(req: SummaryRequest):

    result = summarize(req.text)

    return {
        "summary": result
    }