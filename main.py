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


    # 直接返回小艺插件需要的格式
    return result
