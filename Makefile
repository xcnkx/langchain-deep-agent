.PHONY: help install test lint run-basic run-chat run-tools clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies with uv
	uv sync

test: ## Run setup verification tests
	uv run tests/test_setup.py

lint: ## Run ruff linter and formatter
	uv run ruff check .
	uv run ruff format --check .

lint-fix: ## Run ruff linter and formatter with auto-fix
	uv run ruff check --fix .
	uv run ruff format .

run-basic: ## Run basic agent example
	uv run examples/basic_agent.py

run-chat: ## Run interactive chat agent
	uv run examples/chat_agent.py

run-tools: ## Run agent with tools example
	uv run examples/agent_with_tools.py

setup-env: ## Create .env file from .env.example
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "Created .env file. Please edit it and add your OpenAI API key."; \
	else \
		echo ".env file already exists. Skipping."; \
	fi

clean: ## Remove virtual environment and cache files
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

reinstall: clean install ## Clean and reinstall dependencies

.DEFAULT_GOAL := help
