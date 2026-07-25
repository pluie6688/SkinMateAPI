from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SkinAnalysisRequest(BaseModel):
    imageUri: str
    apiLevel: str = ""

@app.post("/analyzeSkin")
async def analyze_skin(request: SkinAnalysisRequest):
    # 纯原生响应，没有任何外部网络请求，绝对不可能超时！
    markdown_content = (
        "## 🔬 智能皮肤检测报告（极速测试版）\n\n"
        "### 1. 基础肤质评估\n"
        "- **肤质类型**：混合性皮肤\n"
        "- **水分状态**：轻度水分不足\n\n"
        "### 2. 皮肤特征提示\n"
        "- 皮肤整体纹理细腻，T区油脂分泌正常。\n"
        "- 未检测到敏感泛红现象。\n\n"
        "### 3. 护肤建议\n"
        "- 建议加强夜间补水保湿，选择质地清爽的乳液。\n"
    )

    return {
        "name": "analyzeSkin",
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "skinmate001",
            "streamType": "final",
            "textType": "markdown"
        }
    }
