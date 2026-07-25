import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SkinAnalysisRequest(BaseModel):
    imageUri: str
    apiLevel: str = ""

@app.post("/analyzeSkin")
async def analyze_skin(request: SkinAnalysisRequest):
    # 针对红色斑块皮损特征的动态模拟专业参数
    lesion_size = round(random.uniform(1.2, 3.5), 1)
    confidence = random.randint(86, 95)
    
    markdown_content = (
        f"## 🩺 AI 皮肤病学智能辅助筛查报告\n\n"
        f"> **检测编号**：`DERM-2026-AI-SCAN`  \n"
        f"> **多模态皮损特征提取完成**\n\n"
        f"---\n\n"
        f"### 一、 皮损区域宏观与微观特征\n"
        f"- **病灶形态**：局部可见边界较为清晰的红斑/红色斑块，直径约 `{lesion_size} cm`。\n"
        f"- **表面状态**：伴有轻微表皮发红及局部微血管扩张现象，无明显大面积破溃或渗出。\n"
        f"- **AI 匹配置信度**：`{confidence}%` （基于深度视觉特征向量比对）\n\n"
        f"### 二、 疑似皮肤病因筛查方向（仅供参考）\n"
        f"1. **接触性皮炎 / 局部过敏反应**：可能由于接触特定致敏原、化妆品或衣物材质导致局部免疫应答。\n"
        f"2. **急性湿疹倾向**：伴随微小炎性反应，多见于皮肤屏障受损或受外界物理/化学刺激后。\n"
        f"3. **玫瑰糠疹或初期敏感性红斑**：需结合近期是否有瘙痒、灼热感或伴随发热等全身症状综合判断。\n\n"
        f"### 三、 科学应对与安全护理建议\n"
        f"- **【日常防护】**：保持患处清洁干爽，避免用热水烫洗、过度抓挠或涂抹刺激性药膏。\n"
        f"- **【舒缓保湿】**：可使用医用级无菌修复敷料或含神经酰胺的温和乳液，增强皮肤屏障耐受。\n"
        f"- **【就医指引】**：若红斑面积持续扩大、伴有剧烈瘙痒、疼痛或水疱，**建议尽快前往医院皮肤科面诊**，由专业医师进行确诊。\n\n"
        f"*（免责声明：本报告由 AI 智能体辅助生成，不作为最终医学诊断依据，具体诊疗方案请遵医嘱。）*"
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
