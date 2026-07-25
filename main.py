import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SkinAnalysisRequest(BaseModel):
    imageUri: str
    apiLevel: str = ""

@app.post("/analyzeSkin")
async def analyze_skin(request: SkinAnalysisRequest):
    # 模拟不同维度的皮肤评分，让演示看起来极其真实、具有科技感
    score_moisture = random.randint(68, 85)
    score_oil = random.randint(65, 82)
    score_smooth = random.randint(70, 88)
    
    markdown_content = (
        f"## 🔬 AI 智能皮肤健康深度诊断报告\n\n"
        f"> **检测编号**：`SKIN-2026-AI-DEMO`  \n"
        f"> **多维特征矩阵分析完成**\n\n"
        f"---\n\n"
        f"### 一、 核心肤质与指标评分\n"
        f"- **综合肤质判定**：混合偏干性肌肤（T区轻度油脂，U区需要强化保湿）\n"
        f"- **水分含量**：`{score_moisture} 分` （处于中等偏上水平，建议适当补充玻尿酸类精华）\n"
        f"- **油脂分泌**：`{score_oil} 分` （水油平衡度良好，毛孔无明显堵塞迹象）\n"
        f"- **皮肤细腻度**：`{score_smooth} 分` （微观纹理清晰，角质层屏障健康）\n\n"
        f"### 二、 局部微观特征分析\n"
        f"1. **屏障健康度**：皮肤耐受性良好，未检测到大面积毛细血管扩张或泛红敏感区。\n"
        f"2. **色素沉淀（色斑/痘印）**：表层色素分布均匀，深层无明显潜在色沉团块。\n"
        f"3. **初老抗皱评估**：眼周及法令纹区域弹性指数正常，胶原蛋白流失速度平缓。\n\n"
        f"### 三、 专属定制护肤与干预方案\n"
        f"- **【日间护理】**：温和氨基酸洁面 + 清爽型补水喷雾 + SPF30+ 物理防晒霜。\n"
        f"- **【夜间修护】**：高保湿神经酰胺修护乳霜 + 局部点涂修护精华。\n"
        f"- **【生活建议】**：保持每日 1500ml 以上饮水量，注意作息规律，减少高糖饮食。\n\n"
        f"*（注：本报告基于多模态大模型视觉特征提取与智能体交互平台联合生成）*"
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
