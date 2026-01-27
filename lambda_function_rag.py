import json
import boto3

def lambda_handler(event, context):
    # Bedrockクライアントを初期化
    bedrock_agent = boto3.client(service_name='bedrock-agent-runtime', region_name='us-west-2')
    
    user_query = event["key1"]
    
    # ナレッジベースID（実際のIDに置き換え）
    knowledge_base_id = "YOUR_KNOWLEDGE_BASE_ID"
    
    # モデルARN
    model_arn = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
    
    try:
        # RetrieveAndGenerate APIを使用
        response = bedrock_agent.retrieve_and_generate(
            input={
                'text': user_query
            },
            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': knowledge_base_id,
                    'modelArn': model_arn
                }
            }
        )
        
        # 回答を取得
        answer = response['output']['text']
        
        # 参照元の情報を追加（オプション）
        citations = response.get('citations', [])
        if citations:
            answer += "\n\n【参照元】\n"
            for i, citation in enumerate(citations, 1):
                references = citation.get('retrievedReferences', [])
                for ref in references:
                    location = ref.get('location', {})
                    s3_location = location.get('s3Location', {})
                    uri = s3_location.get('uri', '')
                    if uri:
                        answer += f"{i}. {uri}\n"
        
        return answer
        
    except Exception as e:
        error_message = str(e)
        return f"エラーが発生しました: {error_message}"
