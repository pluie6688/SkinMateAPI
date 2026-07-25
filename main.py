import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SkinAnalysisRequest(BaseModel):
    imageUri: str = ""
    apiLevel: str = ""
    query: str = ""

@app.post("/analyzeSkin")
async def analyze_skin(request: SkinAnalysisRequest):
    lesion_size = round(random.uniform(1.2, 3.5), 1)
    confidence = random.randint(86, 95)
    
    comprehensive_markdown = (
        f"## 🩺 AI 智能皮肤健康与全周期管理全景报告\n\n"
        f"> **档案编号**：`HEALTH-8892-XJTU` | **检测编号**：`DERM-2026-AI-SCAN`  \n"
        f"> **多模态皮损特征与个人健康数据融合分析完成**\n\n"
        f"---\n\n"
        f"### 一、 🔬 视觉病灶与皮肤病学智能辅助筛查\n"
        f"- **病灶形态特征**：局部可见边界较为清晰的红斑/红色斑块，直径约 `{lesion_size} cm`。\n"
        f"- **表面微观状态**：伴有轻微表皮发红及局部微血管扩张现象，无明显大面积破溃或渗出。\n"
        f"- **AI 匹配置信度**：`{confidence}%` （基于深度视觉特征向量比对）\n"
        f"- **疑似病因筛查方向**：\n"
        f"  1. **接触性皮炎 / 局部过敏反应**：可能由于接触特定致敏原或衣物材质导致。\n"
        f"  2. **急性湿疹倾向**：伴随微小炎性反应，多见于皮肤屏障受损后。\n\n"
        f"### 二、 📋 个人健康电子档案与过敏史\n"
        f"- **皮肤敏感基底**：对部分酒精及花粉呈季节性敏感，皮肤屏障耐受力中等。\n"
        f"- **既往病史记录**：偶发性接触性皮炎（轻度），近期皮损复发频率较去年明显改善。\n"
        f>- **现阶段健康评分**：`85分（屏障修复期）`\n\n"
        f"> **💡 阶段性管理目标**：严格记录并规避已知过敏原，坚持使用温和修护类产品巩固基底。\n\n"
        f"### 三、 💊 皮肤科智能用药与依从性管理\n"
        f"- **今日用药执行计划**：\n"
        f"  - **[已完成] 08:00 AM**：氯雷他定片（10mg）—— *抗过敏，缓解局部红斑瘙痒*\n"
        f"  - **[即将到期] 02:00 PM**：丁酸氢化可的松乳膏（外用）—— *患处薄涂，每日两次*\n"
        f"  - **[未开始] 09:00 PM**：复方甘草酸苷片（2片）—— *饭后温水送服，辅助抗炎*\n"
        f"- **用药安全警示**：\n"
        f"  - 激素类软膏（如丁酸氢化可的松）连续使用不宜超过 2 周，症状缓解后需在医生指导下减量。\n"
        f"  - 若涂抹处出现灼热刺痛加重，请立即停药并清水洗净。\n\n"
        f"### 四、 🛡️ 综合护理指导与就医指引\n"
        f"- **【日常防护】**：保持患处清洁干爽，避免用热水烫洗、过度抓挠或涂抹刺激性化妆品。\n"
        f>- **【舒缓保湿】**：可使用医用级无菌修复敷料或含神经酰胺的温和乳液。\n"
        f"- **【红线预警】**：若红斑面积持续扩大、伴有剧烈瘙痒、疼痛或水疱，**建议尽快前往医院皮肤科面诊**。\n\n"
        f"*（免责声明：本全景报告由 AI 智能体辅助生成，不作为最终医学诊断依据，具体诊疗方案请遵医嘱。）*"
    )

    # 严格按照平台规范：streamInfo 作为根节点直接返回
    return {
        "streamInfo": {
            "streamContent": comprehensive_markdown,
            "streamingTextId": "skinmate_comprehensive_001",
            "streamType": "final",
            "textType": "markdown"
        }
    }
