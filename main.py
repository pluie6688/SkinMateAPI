from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# 1. 初始化客户端（使用硅基流动的 API key 和接口地址）
SILICONFLOW_API_KEY = "sk-ahrojxfubbxuogipnruxrtijaydlbwsquidaxozpebyocjtl"  # 👈 替换成你刚刚复制的 API Key

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
        # 2. 调用免费的视觉大模型 (Qwen2-VL)
        response = client.chat.completions.create(
            model="Qwen/Qwen2-VL-7B-Instruct",  # 视觉大模型
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
                                "你是一位专业且温和的皮肤健康护理助手。请仔细分析这张图片中的面部皮肤状况，"
                                "从【基础肤质评估】、【潜在皮肤问题】和【针对性护肤建议】三个方面进行总结。"
                                "请务必直接输出排版优雅的 Markdown 格式报告，语气保持专业、客观、有陪伴感，"
                                "结尾请附带简短的免责声明（非医疗诊断）。"
                            )
                        }
                    ]
                }
            ],
            max_tokens=1000
        )
        
        # 提取模型生成的真实分析 Markdown 文本
        markdown_content = response.choices[0].message.content

    except Exception as e:
        # 增加容错：如果图片链接失效或 API 调用异常，返回优雅提示
        markdown_content = (
            "## ⚠️ 皮肤分析暂时中断\n\n"
            f"图像解析时遇到了点小状况（原因：`{str(e)}`）。\n\n"
            "建议您重新拍摄一张**光线充足、面部清晰**的照片再次上传试试。"
        )

    # 3. 按照小艺要求的规范返回
    return {
        "name": "analyzeSkin",
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "skinmate001",
            "streamType": "final",
            "textType": "markdown"
        }
    }
