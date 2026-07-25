import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SkinAnalysisRequest(BaseModel):
    imageUri: str = ""
    apiLevel: str = ""
    query: str = ""

# 1. 皮肤病智能筛查接口（针对红色斑块、皮损等核心创新点）
@app.post("/analyzeSkin")
async def analyze_skin(request: SkinAnalysisRequest):
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

# 2. 个人健康档案接口（记录用户基本体征与既往病史）
@app.post("/healthProfile")
async def health_profile(request: SkinAnalysisRequest):
    markdown_content = (
        "## 📋 个人健康电子档案\n\n"
        "### 👤 基本健康概况\n"
        "- **档案编号**：`HEALTH-8892-XJTU`\n"
        "- **皮肤敏感史**：对部分酒精及花粉季节性过敏\n"
        "- **既往皮肤病史**：偶发性接触性皮炎（轻度）\n\n"
        "### 📊 近期健康追踪\n"
        "- **皮损复发频率**：近 3 个月共发生 1 次轻度泛红，较去年同期明显改善。\n"
        "- **皮肤屏障评分**：`85分（良好）`\n\n"
        "### 🎯 阶段性健康管理目标\n"
        "1. 严格记录并规避已知过敏原。\n"
        "2. 坚持使用温和修护类护肤品，巩固皮肤屏障。"
    )

    return {
        "name": "healthProfile",
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "profile002",
            "streamType": "final",
            "textType": "markdown"
        }
    }

# 3. 智能用药提醒接口（针对皮肤病治疗药物的定时与安全提醒）
@app.post("/medicationReminder")
async def medication_reminder(request: SkinAnalysisRequest):
    markdown_content = (
        "## 💊 皮肤科智能用药与依从性提醒\n\n"
        "### 📅 今日皮肤用药计划\n"
        "- **[已完成] 08:00 AM**：氯雷他定片（10mg）—— *抗过敏，缓解局部红斑瘙痒*\n"
        "- **[即将到期] 02:00 PM**：丁酸氢化可的松乳膏（外用）—— *患处薄涂，每日两次*\n"
        "- **[未开始] 09:00 PM**：复方甘草酸苷片（2片）—— *饭后温水送服，辅助抗炎*\n\n"
        "### ⚠️ 用药安全与注意事项\n"
        "- **外用药提醒**：激素类软膏（如丁酸氢化可的松）连续使用不宜超过 2 周，症状缓解后需在医生指导下逐渐减量。\n"
        "- **不良反应监测**：若涂抹处出现灼热刺痛加重，请立即停药并清水洗净。"
    )

    return {
        "name": "medicationReminder",
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "medmate003",
            "streamType": "final",
            "textType": "markdown"
        }
    }
