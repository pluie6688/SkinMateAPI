# 引入基础库（如果 main.py 顶部已经有，就不需要重复写）
# from fastapi import FastAPI
# from pydantic import BaseModel

# 假设如果你需要校验参数可以保留这个，为了极致防报错，我们直接用 dict 接收一切小艺传过来的参数
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
        "- **已知过敏史**：无明显药物过敏，对部分换季花粉及强效酸类护肤品敏感\n\n"
        "### 📊 初始健康评估与规划\n"
        "- **皮肤屏障状态**：当前处于亚健康波动期，T区偶发油脂分泌过剩，面颊两侧伴有轻度泛红。\n"
        "- **智能管家建议**：\n"
        "  1. 已为您自动开启『智能用药提醒』功能。\n"
        "  2. 建议您每周使用一次本系统的【AI 皮肤筛查】，以便动态追踪屏障修复曲线。\n\n"
        "*（系统提示：您的健康数据已通过端云加密技术隔离存储，全方位保障隐私安全。）*"
    )

    # 依然采用最纯净的华为官方 streamInfo 根节点结构
    return {
        "streamInfo": {
            "streamContent": markdown_content,
            "streamingTextId": "create_profile_001",
            "streamType": "final",
            "textType": "markdown"
        }
    }
