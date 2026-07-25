import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CommonRequest(BaseModel):
    imageUri: str = ""
    apiLevel: str = ""
    query: str = ""

# 1. 皮肤检测接口（前面已验证的完美版本）
@app.post("/analyzeSkin")
async def analyze_skin(request: CommonRequest):
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
        f"### 二、 专属定制护肤与干预方案\n"
        f"- **【日间护理】**：温和氨基酸洁面 + 清爽型补水喷雾 + SPF30+ 物理防晒霜。\n"
        f"- **【夜间修护】**：高保湿神经酰胺修护乳霜 + 局部点涂修护精华。\n"
        f"- **【生活建议】**：保持每日 1500ml 以上饮水量，注意作息规律，减少高糖饮食。"
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

# 2. 智能用药提醒接口
@app.post("/medicationReminder")
async def medication_reminder(request: CommonRequest):
    markdown_content = (
        "## 💊 智能用药与健康提醒中心\n\n"
        "### 📅 今日服药计划\n"
        "- **[已完成] 08:00 AM**：维生素 C 片（1片）—— *饭后温水送服*\n"
        "- **[即将到期] 12:30 PM**：复合 B 族维生素（1粒）—— *随餐服用*\n"
        "- **[未开始] 08:00 PM**：褪黑素软糖（1粒）—— *睡前半小时服用*\n\n"
        "### ⚠️ 用药安全提示\n"
        "- 当前服用药物之间无冲突禁忌。\n"
        "- 维生素C请避免与海鲜同食过量。\n"
        "- 如有用药调整需求，请及时同步医嘱更新提醒。"
    )

    return {
        "name": "medicationReminder",
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "medmate002",
            "streamType": "final",
            "textType": "markdown"
        }
    }

# 3. 个人健康档案接口
@app.post("/healthProfile")
async def health_profile(request: CommonRequest):
    markdown_content = (
        "## 📋 个人健康电子档案\n\n"
        "### 👤 基本健康概况\n"
        "- **档案编号**：`HEALTH-8892-XJTU`\n"
        "- **健康评级**：`优良 (92分)`\n"
        "- **血压状态**：118 / 76 mmHg（正常范围）\n"
        "- **静息心率**：72 次/分（规律平稳）\n\n"
        "### 📊 近期健康趋势\n"
        "- **睡眠质量**：平均每日睡眠 7.5 小时，深度睡眠占比良好。\n"
        "- **皮肤与体质**：季节性轻微敏感，整体免疫屏障稳定。\n\n"
        "### 🎯 本阶段健康目标\n"
        "1. 保持规律有氧运动，每周至少 3 次。\n"
        "2. 增加水分摄入，改善局部皮肤干燥状况。"
    )

    return {
        "name": "healthProfile",
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "profile003",
            "streamType": "final",
            "textType": "markdown"
        }
    }
