# Call-AI

A simple Python client for calling a remote Ollama AI server via HTTP. This library lets you connect your apps to a centralized AI server running Ollama, so you don't need to run models locally on every device.

## Features
- Minimal, single-function interface
- Portable: set the server URL via environment variable or function argument
- Works with any FastAPI/Ollama server exposing a compatible `/generate` endpoint

## Installation

Install from PyPI (after publishing):
```sh
pip install call-ai
```

Or use directly by copying `call_ai/` into your project.

## Usage

### Basic Example
```python
import call_ai

response = call_ai.ai("llama2", "Hello, AI!", "How are you?")
print(response)
```

### Set the server URL
You can set the server URL in two ways:

**1. With an environment variable:**
```sh
export CALL_AI_SERVER_URL="http://your-server:8000/generate"
```

**2. By passing it to the function:**
```python
response = call.ai("gemma3:4b", "youre a math proffessor", "hello, can you explain the Pythagorean theorem?")
print(response)
```

### Full Example
```python
import call_ai

model = "llama2"
prompt = "You are a poet."
message = "Make a poem about the sea."

response = call.ai(model, prompt, message)
print("AI Response:", response)
```

## Requirements
- Python 3.7+
- `requests` library

## License
MIT
