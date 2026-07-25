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

        "success": True,

        "message":
        "皮肤分析完成",

        "data":
        data

    }