# langchain-deep-agent

LangChain Deep Agent - A Python template project for building AI agents using LangChain.

## 概要 (Overview)

このプロジェクトは、LangChainのPython APIを使用してAIエージェントを構築するためのテンプレートです。uvを使用した依存関係管理と、複数の実用的な例が含まれています。

This project is a template for building AI agents using LangChain's Python API. It uses `uv` for dependency management and includes several practical examples.

## 特徴 (Features)

- ✅ **uv による環境管理** - 高速で信頼性の高い依存関係管理
- ✅ **LangChain統合** - 最新のLangChain、LangChain Core、LangChain OpenAI
- ✅ **実用的な例** - 基本的なエージェントからツール使用まで
- ✅ **型安全** - 完全な型ヒント付き
- ✅ **簡単なセットアップ** - すぐに始められる

---

- ✅ **Environment management with uv** - Fast and reliable dependency management
- ✅ **LangChain integration** - Latest LangChain, LangChain Core, and LangChain OpenAI
- ✅ **Practical examples** - From basic agents to tool usage
- ✅ **Type-safe** - Fully typed with hints
- ✅ **Easy setup** - Get started quickly

## 前提条件 (Prerequisites)

- Python 3.12 or higher
- uv (Python package manager)
- OpenAI API key

## クイックスタート (Quick Start)

最速で始めたい方は [QUICKSTART.md](QUICKSTART.md) をご覧ください。

For the fastest way to get started, see [QUICKSTART.md](QUICKSTART.md).

## セットアップ (Setup)

### 1. uvのインストール (Install uv)

```bash
# pipを使用してuvをインストール
pip install uv

# または、公式インストーラーを使用（UNIXシステム）
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. プロジェクトのクローン (Clone the project)

```bash
git clone https://github.com/xcnkx/langchain-deep-agent.git
cd langchain-deep-agent
```

### 3. 依存関係のインストール (Install dependencies)

```bash
# 依存関係を同期
uv sync
```

### 4. 環境変数の設定 (Set up environment variables)

```bash
# .env.exampleを.envにコピー
cp .env.example .env

# .envファイルを編集してOpenAI APIキーを設定
# Edit the .env file and add your OpenAI API key
```

`.env`ファイルの内容 (Contents of `.env`):
```env
OPENAI_API_KEY=your_actual_api_key_here
```

## 使い方 (Usage)

### 基本的なエージェントの実行 (Run basic agent)

```bash
uv run examples/basic_agent.py
```

### 対話型チャットエージェントの実行 (Run interactive chat agent)

```bash
uv run examples/chat_agent.py
```

### ツール付きエージェントの実行 (Run agent with tools)

```bash
uv run examples/agent_with_tools.py
```

## プロジェクト構造 (Project Structure)

```
langchain-deep-agent/
├── src/
│   └── langchain_deep_agent/    # メインパッケージ
│       ├── __init__.py          # パッケージ初期化
│       └── py.typed             # 型情報マーカー
├── examples/                    # 使用例
│   ├── basic_agent.py          # 基本的なエージェント
│   ├── chat_agent.py           # 対話型チャットエージェント
│   ├── agent_with_tools.py     # ツール使用例
│   └── README.md               # 例の詳細説明
├── pyproject.toml              # プロジェクト設定と依存関係
├── .env.example                # 環境変数のテンプレート
├── .python-version             # Python バージョン指定
└── README.md                   # このファイル
```

## 依存関係 (Dependencies)

主な依存関係：
- **langchain** - LangChainのコアライブラリ
- **langchain-core** - LangChainの基本コンポーネント
- **langchain-openai** - OpenAI統合
- **python-dotenv** - 環境変数管理

詳細は`pyproject.toml`を参照してください。

## 開発 (Development)

### 新しい依存関係の追加 (Add new dependencies)

```bash
uv add package-name
```

### 依存関係の削除 (Remove dependencies)

```bash
uv remove package-name
```

### Pythonスクリプトの実行 (Run Python scripts)

```bash
uv run your_script.py
```

### Makefileコマンド (Makefile Commands)

便利なMakefileコマンドも利用できます:

Convenient Makefile commands are also available:

```bash
make help       # Show all available commands
make install    # Install dependencies
make test       # Run setup verification tests
make run-basic  # Run basic agent example
make run-chat   # Run chat agent example
make run-tools  # Run tools agent example
make setup-env  # Create .env from .env.example
make clean      # Clean up generated files
```

### 仮想環境のアクティベート (Activate virtual environment)

```bash
source .venv/bin/activate  # Unix/macOS
# または
.venv\Scripts\activate  # Windows
```

## 例の詳細 (Example Details)

各例について詳しくは、`examples/README.md`を参照してください。

For more details about each example, see `examples/README.md`.

## トラブルシューティング (Troubleshooting)

### OpenAI APIキーエラー
```
ValueError: OPENAI_API_KEY not found in environment variables.
```
→ `.env`ファイルが正しく作成され、有効なAPIキーが設定されていることを確認してください。

### 依存関係のエラー
```bash
# 依存関係を再同期
uv sync --reinstall
```

## 参考リンク (References)

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [uv Documentation](https://github.com/astral-sh/uv)

## ライセンス (License)

MIT License

## 貢献 (Contributing)

プルリクエストを歓迎します！

Pull requests are welcome!
