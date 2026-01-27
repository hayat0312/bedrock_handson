# Amazon Bedrock ハンズオン - 完全ガイド

## 概要
AWS Amplify、Lambda、API Gatewayを使ったサーバーレスアプリケーションで、Amazon Bedrockと連携する生成AIアプリケーションを構築するハンズオン。

**所要時間**: 2時間程度  
**リージョン**: us-west-2（オレゴン）  
**難易度**: 初級〜中級

## ディレクトリ構成

```
Bedrockハンズオン/
├── README.md                    # このファイル
├── 01_基本編/
│   ├── 手順.md                  # 基本編の詳細手順
│   ├── index.html               # フロントエンドファイル
│   └── lambda_function.py       # Lambda関数コード（ガードレール付き）
├── 02_RAG編/
│   ├── 手順.md                  # RAG編の詳細手順
│   ├── index.html               # RAG用フロントエンド
│   └── lambda_function_rag.py   # RAG用Lambda関数
└── 注意点とトラブルシューティング.md
```

## 基本編の流れ

1. **フロントエンドファイルの作成** (5分)
2. **AWS Amplifyへのデプロイ** (10分)
3. **ガードレールの作成** (10分)
4. **Lambda関数の作成** (15分)
5. **API Gatewayの作成** (15分)
6. **HTMLファイルの更新と再デプロイ** (10分)
7. **動作確認とテスト** (10分)

## RAG編の流れ

1. **S3バケットの作成** (5分)
2. **ナレッジベースの作成** (15分)
3. **サンプルファイルのアップロード** (5分)
4. **データソースの同期** (5分)
5. **Lambda関数の作成** (15分)
6. **API Gateway、Amplifyの設定** (15分)
7. **動作確認** (10分)

## 前提条件

- AWSアカウント
- 基本的なAWSコンソールの操作知識
- テキストエディタ

## 使用するAWSサービス

- **AWS Amplify**: Webホスティング
- **AWS Lambda**: サーバーレス関数
- **Amazon API Gateway**: REST API
- **Amazon Bedrock**: 生成AI
- **Amazon Bedrock Guardrails**: コンテンツフィルタリング
- **Amazon S3**: オブジェクトストレージ（RAG編）
- **Amazon Bedrock Knowledge Bases**: RAG機能（RAG編）
- **Amazon OpenSearch Serverless**: ベクトルデータベース（RAG編）

## 料金について

このハンズオンを実行すると、以下のサービスで料金が発生します：
- Amazon Bedrock（モデル使用料）
- Amazon Bedrock Guardrails（テキスト処理料）
- AWS Lambda（実行時間）
- Amazon API Gateway（APIコール数）
- AWS Amplify（ホスティング）
- Amazon S3（ストレージ、RAG編）
- Amazon OpenSearch Serverless（RAG編）

**重要**: ハンズオン終了後は、必ずリソースを削除してください。

## サポート

問題が発生した場合は、`注意点とトラブルシューティング.md`を参照してください。

## 参考リンク

- [公式ワークショップ](https://catalog.us-east-1.prod.workshops.aws/event/dashboard/ja-JP/workshop)
- [Amazon Bedrock ドキュメント](https://docs.aws.amazon.com/bedrock/)
- [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
