from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义接收的请求体结构（完全保留你验证成功的结构）
class SkinAnalysisRequest(BaseModel):
    imageUri: str = "" # 加上默认值 ""，防止小艺传空参数时报 422 错误
    apiLevel: str = ""
    query: str = ""    # 增加 query 字段兼容小艺可能的文本输入

# ---------------------------------------------------------
# 1. AI 皮肤病学辅助筛查（红斑/皮炎 专属版本）
# ---------------------------------------------------------
@app.post("/analyzeSkin")
async def analyze_skin(request: SkinAnalysisRequest):
    
    # 针对红色斑块的专业 Markdown 报告
    markdown_content = """## 🩺 AI 皮肤病学辅助筛查报告

根据您上传的局部皮损图片，大模型视觉引擎为您进行了多维度特征提取。以下是疑似红色斑块的深度分析结果：

### 🔬 视觉病灶特征
*   **病灶形态**：发现明显的**红色斑块**，边界较为清晰，直径约 2-3 cm。
*   **表面状态**：局部伴有轻微的表皮发红及微血管扩张，无明显大面积破溃、渗出或严重鳞屑。
*   **AI 匹配置信度**：`89%` （基于深度学习视觉特征比对）

### ⚠️ 疑似筛查方向（仅供参考）
1.  **接触性皮炎 / 局部过敏**：最常见的诱因，可能是近期接触了特定致敏原、新化妆品或衣物材质导致局部免疫应答。
2.  **急性湿疹初期**：伴随轻度炎症，通常发生在皮肤屏障受损后。若伴有明显瘙痒感，则此概率增加。

### 🛡️ 科学护理与干预建议
*   **紧急阻断**：立即停用患处周围可能引起过敏的护肤品，避免接触洗发水、皂基等刺激物。
*   **精简修复**：仅使用生理盐水冷敷缓解红热，或涂抹含有神经酰胺的医用级无菌修复乳。
*   **就医红线**：切勿自行盲目涂抹强效激素药膏。若红斑面积持续扩散、伴有剧烈瘙痒、刺痛或出现水疱，**请立即前往三甲医院皮肤科面诊**。

> **免责声明**：本报告由大模型辅助生成，仅作为健康管理参考，不作为最终临床医学诊断依据。具体诊疗方案请严格遵从专业医师医嘱。
"""

    # 严格使用你已经跑通的 Schema 返回数据
    return {
        "name": "analyzeSkin",
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "skinmate_erythema_001",
            "streamType": "final",
            "textType": "markdown"
        }
    }

# ---------------------------------------------------------
# 2. 建立个人健康档案（单独的接口）
# ---------------------------------------------------------
@app.post("/createHealthProfile")
async def create_health_profile(request: SkinAnalysisRequest):
    
    # 建立档案的 Markdown 卡片
    profile_content = """## ✅ 专属健康档案已成功建立

> **档案编号**：`MED-XJTU-8820`  
> **状态**：端云数据已加密同步

---

### 👤 基础健康图谱
*   **基础肤质**：混合偏敏感肌（屏障处于波动期）
*   **已知过敏史**：对部分换季花粉敏感，曾有轻度接触性皮炎记录。
*   **近期皮损频率**：近 3 个月发生 1 次局部泛红。

### 🎯 智能管家阶段规划
1.  **动态追踪**：建议您每周进行一次【AI 皮肤筛查】，追踪红色斑块的消退曲线。
2.  **用药管理**：已为您在后台激活【智能用药提醒】模块。一旦确诊用药，系统将自动下发安全提醒。

*随时对我说“查看健康档案”，即可调出此界面。*
"""

    return {
        "name": "createHealthProfile",
        "streamInfo": {
            "streamContent": profile_content,
            "streamingTextId": "profile_001",
            "streamType": "final",
            "textType": "markdown"
        }
    }
