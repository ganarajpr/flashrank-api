from fastapi import FastAPI
from fastapi.responses import JSONResponse
from flashrank import Ranker, RerankRequest
from pydantic import BaseModel
from typing import List
import json

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
    # print(request.query, request.passages)
    passages_dict = [passage.model_dump() for passage in request.passages]
    rerankrequest = RerankRequest(query=request.query, passages=passages_dict)
    result = ranker.rerank(rerankrequest)
    # print(result)

    final_result = []
    for item in result:
        final_result.append({
            "id": item.get("id"),
            "text": item.get("text"),
            "meta": item.get("meta"),
            "score": float(item.get("score"))
        })
    print(final_result)

    return JSONResponse(content=json.dumps(final_result))
