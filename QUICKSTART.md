# Quick Start Guide

このガイドでは、最速で LangChain Deep Agent を始める方法を説明します。

This guide shows you how to get started with LangChain Deep Agent as quickly as possible.

## 1. インストール (Installation)

```bash
# uvをインストール (Install uv)
pip install uv

# プロジェクトをクローン (Clone the project)
git clone https://github.com/xcnkx/langchain-deep-agent.git
cd langchain-deep-agent

# 依存関係をインストール (Install dependencies)
uv sync
```

## 2. APIキーの設定 (API Key Setup)

```bash
# .envファイルを作成 (Create .env file)
cp .env.example .env

# エディタで.envを開いてAPIキーを追加 (Edit .env and add your API key)
# OPENAI_API_KEY=sk-your-actual-key-here
```

OpenAI APIキーは以下から取得できます:
Get your OpenAI API key from: https://platform.openai.com/api-keys

## 3. セットアップの確認 (Verify Setup)

```bash
# テストスクリプトを実行 (Run test script)
uv run tests/test_setup.py
```

すべてのテストが通れば準備完了です！
If all tests pass, you're ready to go!

## 4. 最初のエージェントを実行 (Run Your First Agent)

```bash
# 基本的なエージェントを実行 (Run basic agent)
uv run examples/basic_agent.py
```

## 5. 他の例を試す (Try Other Examples)

```bash
# 対話型チャットエージェント (Interactive chat)
uv run examples/chat_agent.py

# ツール付きエージェント (Agent with tools)
uv run examples/agent_with_tools.py
```

## トラブルシューティング (Troubleshooting)

### APIキーエラー (API Key Error)

```
ValueError: OPENAI_API_KEY not found in environment variables.
```

→ `.env`ファイルが存在し、正しいAPIキーが設定されていることを確認してください。
→ Make sure the `.env` file exists and contains a valid API key.

### 依存関係エラー (Dependency Error)

```bash
# 依存関係を再インストール (Reinstall dependencies)
uv sync --reinstall
```

### Pythonバージョンエラー (Python Version Error)

このプロジェクトはPython 3.12以上が必要です。
This project requires Python 3.12 or higher.

```bash
# Pythonバージョンを確認 (Check Python version)
python --version
```

## 次のステップ (Next Steps)

- 📖 [README.md](README.md) - 完全なドキュメント
- 📁 [examples/README.md](examples/README.md) - 例の詳細説明
- 🔗 [LangChain Documentation](https://python.langchain.com/) - LangChainの公式ドキュメント

## よくある質問 (FAQ)

### Q: OpenAI以外のLLMを使えますか？
A: はい！LangChainは多くのLLMプロバイダーをサポートしています。`langchain-anthropic`、`langchain-google-genai`などを追加できます。

### Q: Can I use LLMs other than OpenAI?
A: Yes! LangChain supports many LLM providers. You can add `langchain-anthropic`, `langchain-google-genai`, etc.

### Q: より複雑なエージェントを構築するには？
A: `examples/`ディレクトリの例を参考にして、ツールやチェーンを追加してカスタマイズしてください。

### Q: How do I build more complex agents?
A: Check the examples in `examples/` directory and customize by adding tools and chains.
