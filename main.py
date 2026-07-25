from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义接收的请求体结构
class SkinAnalysisRequest(BaseModel):
    imageUri: str
    apiLevel: str = "" # 兼容小艺可能传入的空字符串

@app.post("/analyzeSkin")
async def analyze_skin(request: SkinAnalysisRequest):
    # 1. 这里是你未来真正处理图片、调用AI视觉模型的地方
    # image_url = request.imageUri
    # analysis_result = run_ai_model(image_url) 
    
    # 2. 目前我们可以先写死一段逼真的 Markdown 格式测试数据
    # 使用 Python 的多行字符串 (triple quotes) 方便排版 Markdown
    markdown_content = """## 🩺 皮肤健康分析报告

根据您上传的图片，AI 为您进行了初步的肤质检测。以下是详细结果：

### 📊 基础肤质检测
*   **肤质倾向**：混合偏干性肌肤
*   **敏感度**：中度敏感（检测到双颊有轻微红血丝）
*   **出油情况**：T区（额头、鼻子）有少量油脂分泌，U区（脸颊、下巴）偏干燥

### ⚠️ 主要风险点
1.  **屏障受损**：脸颊区域泛红，可能近期使用了刺激性护肤品或过度清洁。
2.  **局部炎症**：下巴区域检测到 2 处闭口粉刺，存在发炎趋势。

### 💡 专属护肤建议
*   **精简护肤**：停用含有水杨酸、果酸等去角质成分的产品。
*   **温和清洁**：建议使用氨基酸洁面，避免使用清洁力过强的皂基洁面。
*   **加强保湿**：重点涂抹含有神经酰胺、泛醇（B5）成分的面霜，帮助修复皮肤屏障。

> **免责声明**：本报告由 AI 视觉分析生成，仅供日常护肤参考，不能替代专业皮肤科医生的医疗诊断。如果出现严重红肿、瘙痒等不适，请及时就医。
"""

    # 3. 严格按照小艺插件需要的 Schema 返回数据
    return {
        "name": "analyzeSkin",
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "skinmate001",
            "streamType": "final",
            "textType": "markdown"
        }
    }
