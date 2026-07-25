class SkinAnalysisAgent:


    async def execute(
        self,
        imageUri: str
    ):


        # 后续这里接真实AI模型
        # 当前Demo返回模拟分析结果


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


以上结果仅供健康管理参考，如有持续或严重皮肤问题建议咨询专业医生。
                    """,


                    "streamingTextId":
                    "skinmate001",


                    "streamType":
                    "final",


                    "textType":
                    "markdown"

                },


                "items": []

            }

        }


        return result
