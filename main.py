from fastapi import FastAPI
from pydantic import BaseModel

from agent import SkinAnalysisAgent


app = FastAPI(
    title="SkinMate Agent API"
)


class SkinRequest(BaseModel):

    imageUri: str



@app.post("/analyzeSkin")
async def analyze_skin(
    request: SkinRequest
):

    agent = SkinAnalysisAgent()


    data = await agent.execute(
        request.imageUri
    )


    return {

        "name": "analyzeSkin",

        "streamInfo": {

            "streamContent":
            data["reply"]["streamInfo"]["streamContent"],

            "streamingTextId":
            "skinmate001",

            "streamType":
            "final",

            "textType":
            "markdown"

        }

    }
