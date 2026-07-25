class SkinAnalysisAgent:


    async def execute(
        self,
        imageUri: str
    ):

        # 这里以后接真实AI模型
        # 图片分析
        # 大模型识别
        # 华为云AI服务


        result = {

            "errorCode": "0",

            "errorMessage": "",

            "reply": {

                "streamInfo": {

                    "streamContent":
                    """
## 皮肤分析结果

风险判断：
轻度痤疮风险

置信度：
92%

护理建议：
- 注意防晒
- 保持皮肤清洁
- 加强保湿
                    """,

                    "streamingTextId":
                    "skinmate001",

                    "streamType":
                    "final",

                    "textType":
                    "markdown"
                }
            }
        }


        return result
