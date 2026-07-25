import traceback
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# ⚠️ 请确保这里填入了你真实的硅基流动 API Key
SILICONFLOW_API_KEY = "sk-xxxxxxxxxxxxxxxx" 

client = OpenAI(
    api_key=SILICONFLOW_API_KEY,
    base_url="https://api.siliconflow.cn/v1"
)

class SkinAnalysisRequest(BaseModel):
    imageUri: str
    apiLevel: str = ""

@app.post("/analyzeSkin")
async def analyze_skin(request: SkinAnalysisRequest):
    image_url = request.imageUri
    
    try:
        # 调用视觉大模型
        response = client.chat.completions.create(
            model="Qwen/Qwen2-VL-72B-Instruct",  
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": image_url}
                        },
                        {
                            "type": "text", 
                            "text": "分析这张皮肤图片，提供 Markdown 格式的护肤建议。"
                        }
                    ]
                }
            ],
            max_tokens=500
        )
        
        markdown_content = response.choices[0].message.content

    except Exception as e:
        # 🚨 关键：把真实的错误堆栈直接传回前端，方便我们一眼看出是什么问题
        error_detail = traceback.format_exc()
        markdown_content = (
            "## ❌ 报错调试信息\n\n"
            f"捕获到异常：`{str(e)}`\n\n"
            "```text\n"
            f"{error_detail}\n"
            "```"
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
