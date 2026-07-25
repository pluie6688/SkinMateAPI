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


    result = await agent.execute(
        request.imageUri
    )


    # 防止结构变化导致500
    content = "皮肤分析完成"


    try:
        content = (
            result
            .get("reply", {})
            .get("streamInfo", {})
            .get("streamContent", content)
        )

    except Exception:
        pass


    return {

        "name": "analyzeSkin",

        "streamInfo": {

            "streamContent": content,

            "streamingTextId": "skinmate001",

            "streamType": "final",

            "textType": "markdown"

        }

    }
