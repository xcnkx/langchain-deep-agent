#!/usr/bin/env python
"""Test script to verify the setup without requiring API keys."""

import sys


def test_imports():
    """Test that all necessary imports work."""
    print("Testing imports...")
    
    try:
        from langchain_openai import ChatOpenAI
        from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
        from langchain_core.tools import tool
        import langchain
        from dotenv import load_dotenv
        
        print("✅ All imports successful!")
        print(f"   LangChain version: {langchain.__version__}")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False


def test_project_structure():
    """Test that the project structure is correct."""
    print("\nTesting project structure...")
    
    import os
    
    required_files = [
        "pyproject.toml",
        ".python-version",
        ".env.example",
        "README.md",
        "examples/basic_agent.py",
        "examples/chat_agent.py",
        "examples/agent_with_tools.py",
        "src/langchain_deep_agent/__init__.py",
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - NOT FOUND")
            all_exist = False
    
    return all_exist


def test_package_metadata():
    """Test package metadata."""
    print("\nTesting package metadata...")
    
    try:
        import langchain_deep_agent
        
        if hasattr(langchain_deep_agent, "__version__"):
            print(f"✅ Package version: {langchain_deep_agent.__version__}")
        else:
            print("⚠️  Package version not found")
        
        return True
    except ImportError as e:
        print(f"❌ Package import failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("LangChain Deep Agent - Setup Verification")
    print("=" * 60)
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Project Structure", test_project_structure()))
    results.append(("Package Metadata", test_package_metadata()))
    
    print("\n" + "=" * 60)
    print("Test Results:")
    print("=" * 60)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 All tests passed! The setup is complete and ready to use.")
        print("\nNext steps:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key to .env")
        print("3. Run an example: uv run examples/basic_agent.py")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please check the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
