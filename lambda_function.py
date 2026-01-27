import json
import boto3


def lambda_handler(event, context):
    # Bedrockクライアントを初期化
    bedrock = boto3.client(service_name='bedrock-runtime',
                           region_name='us-west-2')

    user_prompt = event["key1"]
    model_id = 'us.anthropic.claude-sonnet-4-5-20250929-v1:0'
    system_prompts = [{"text": "あなたは生成AIのエージェントです。ユーザからの質問に日本語で丁寧に回答してください。"}]

    messages = [
        {
            "role": "user",
            "content": [{"text": user_prompt}],
        }
    ]

    inferenceConfig = {
        "temperature": 0.1,
        "maxTokens": 3000,
        "stopSequences": []
    }

    # ガードレール設定（日本語対応版 - Standard tier）
    guardrail_id = "iw6zsasnirkc"  # 実際のIDに置き換え
    guardrail_version = "1"

    try:
        response = bedrock.converse(
            modelId=model_id,
            messages=messages,
            system=system_prompts,
            inferenceConfig=inferenceConfig,
            guardrailConfig={
                'guardrailIdentifier': guardrail_id,
                'guardrailVersion': guardrail_version
            }
        )

        return response["output"]["message"]["content"][0]["text"]

    except Exception as e:
        error_message = str(e)
        if 'GuardrailIntervened' in error_message or 'GUARDRAIL_INTERVENED' in error_message:
            return "申し訳ございません。この質問には回答できません。ガードレールによりブロックされました。"
        else:
            return f"エラーが発生しました: {error_message}"
