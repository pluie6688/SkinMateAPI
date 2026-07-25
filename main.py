import random
from fastapi import FastAPI

app = FastAPI()

# 1. 皮肤检测假数据接口
@app.post("/analyzeSkin")
async def analyze_skin(request: dict):
    lesion_size = round(random.uniform(1.2, 3.5), 1)
    confidence = random.randint(86, 95)
    
    markdown_content = (
        f"## 🩺 AI 皮肤病学辅助筛查\n\n"
        f"- **病灶形态**：局部可见边界较为清晰的红斑/红色斑块，直径约 `{lesion_size} cm`。\n"
        f"- **AI 匹配置信度**：`{confidence}%` \n"
        f"- **疑似方向**：接触性皮炎或急性湿疹倾向。\n"
        f"- **建议**：保持患处清洁干爽，若红斑面积持续扩大请及时就医。"
    )
    
    return {
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "skin_001",
            "streamType": "final",
            "textType": "markdown"
        }
    }

# 2. 建立健康档案假数据接口
@app.post("/createHealthProfile")
async def create_health_profile(request: dict):
    markdown_content = (
        "## ✅ 专属健康档案已成功建立\n\n"
        "> **档案编号**：`XJTU-MED-8820`\n"
        "> **建档时间**：2026-07-25\n\n"
        "---\n\n"
        "### 👤 基础体征信息\n"
        "- **用户**：首席体验官\n"
        "- **年龄**：20 岁\n"
        "- **基础肤质**：混合偏敏感肌\n"
        "- **已知过敏史**：对部分换季花粉敏感\n\n"
        "### 📊 初始健康评估与规划\n"
        "- **皮肤屏障状态**：T区偶发油脂分泌过剩，面颊两侧伴有轻度泛红。\n"
        "- **智能管家建议**：已为您开启智能用药提醒，建议每周进行一次AI皮肤筛查。"
    )
    
    return {
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "profile_001",
            "streamType": "final",
            "textType": "markdown"
        }
    }
