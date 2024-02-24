from fastapi import FastAPI
from flashrank import Ranker, RerankRequest
from pydantic import BaseModel
from typing import List

app = FastAPI()

ranker = Ranker()


class Passage(BaseModel):
    id: str
    text: str
    meta: dict


class RankRequest(BaseModel):
    query: str
    passages: List[Passage]

@app.post("/rank")
async def rank(request: RankRequest):
    print(request.query, request.passages)
    passages_dict = [passage.model_dump() for passage in request.passages]
    rerankrequest = RerankRequest(query=request.query, passages=passages_dict)
    result = ranker.rerank(rerankrequest)
    return result
