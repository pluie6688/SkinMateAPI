import traceback
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# 1. 请在这里填入你真实的硅基流动 API Key
SILICONFLOW_API_KEY = "sk-xxxxxxxxxxxxxxxx"  # 👈 换成你的 sk-xxx

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
        # 2. 使用 7B 轻量级视觉模型，确保在小艺规定的极短超时时间内秒级响应
        response = client.chat.completions.create(
            model="Qwen/Qwen2-VL-7B-Instruct",  
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
                            "text": (
                                "你是一位专业且温和的皮肤健康护理助手。请简要分析这张图片中的皮肤状况，"
                                "从【基础肤质评估】、【潜在问题】和【护肤建议】三个方面进行总结，"
                                "并输出 Markdown 格式报告。"
                            )
                        }
                    ]
                }
            ],
            max_tokens=400  # 限制最大生成长度，防止超时
        )
        
        markdown_content = response.choices[0].message.content

    except Exception as e:
        # 如果中间出现任何异常，直接把错误信息作为 Markdown 文本返回，方便在前端排查
        error_detail = traceback.format_exc()
        markdown_content = (
            "## ⚠️ 后端调用异常\n\n"
            f"错误原因：`{str(e)}`\n\n"
            "```text\n"
            f"{error_detail}\n"
            "```"
        )

    # 3. 严格匹配小艺要求的返回格式
    return {
        "name": "analyzeSkin",
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "skinmate001",
            "streamType": "final",
            "textType": "markdown"
        }
    }
