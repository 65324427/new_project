"""
本地模型连接模块
支持多种本地模型连接方式：Ollama、vLLM、LM Studio等
"""

import requests
import json
from typing import Optional, Dict, Any
import os

class LocalModelClient:
    """本地模型客户端基类"""
    
    def __init__(self, host: str = "localhost", port: int = 8000):
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}"
    
    def generate(self, prompt: str, **kwargs) -> str:
        """生成文本"""
        raise NotImplementedError
    
    def chat(self, messages: list, **kwargs) -> str:
        """对话生成"""
        raise NotImplementedError

class OllamaClient(LocalModelClient):
    """Ollama客户端"""
    
    def __init__(self, host: str = "localhost", port: int = 11434, model: str = "llama2"):
        super().__init__(host, port)
        self.model = model
        self.api_url = f"{self.base_url}/api/generate"
        self.chat_url = f"{self.base_url}/api/chat"
    
    def generate(self, prompt: str, stream: bool = False, **kwargs) -> str:
        """使用Ollama生成文本"""
        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream,
            **kwargs
        }
        response = requests.post(self.api_url, json=data)
        result = response.json()
        return result.get('response', '')
    
    def chat(self, messages: list, stream: bool = False, **kwargs) -> str:
        """使用Ollama进行对话"""
        data = {
            "model": self.model,
            "messages": messages,
            "stream": stream,
            **kwargs
        }
        response = requests.post(self.chat_url, json=data)
        result = response.json()
        return result.get('message', {}).get('content', '')

class VLLMClient(LocalModelClient):
    """vLLM客户端（兼容OpenAI API）"""
    
    def __init__(self, host: str = "localhost", port: int = 8000, model: str = "local-model"):
        super().__init__(host, port)
        self.model = model
        self.chat_url = f"{self.base_url}/v1/chat/completions"
    
    def chat(self, messages: list, temperature: float = 0.7, **kwargs) -> str:
        """使用vLLM进行对话"""
        data = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            **kwargs
        }
        response = requests.post(self.chat_url, json=data)
        result = response.json()
        return result['choices'][0]['message']['content']

class LMStudioClient(LocalModelClient):
    """LM Studio客户端（兼容OpenAI API）"""
    
    def __init__(self, host: str = "localhost", port: int = 1234, model: str = "local-model"):
        super().__init__(host, port)
        self.model = model
        self.chat_url = f"{self.base_url}/v1/chat/completions"
    
    def chat(self, messages: list, temperature: float = 0.7, **kwargs) -> str:
        """使用LM Studio进行对话"""
        data = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            **kwargs
        }
        response = requests.post(self.chat_url, json=data)
        result = response.json()
        return result['choices'][0]['message']['content']

class LocalModelFactory:
    """本地模型工厂类"""
    
    @staticmethod
    def create_client(model_type: str, **kwargs) -> LocalModelClient:
        """创建本地模型客户端
        
        Args:
            model_type: 模型类型 ('ollama', 'vllm', 'lmstudio')
            **kwargs: 其他配置参数
            
        Returns:
            LocalModelClient: 本地模型客户端实例
        """
        model_type = model_type.lower()
        
        if model_type == 'ollama':
            return OllamaClient(**kwargs)
        elif model_type == 'vllm':
            return VLLMClient(**kwargs)
        elif model_type == 'lmstudio':
            return LMStudioClient(**kwargs)
        else:
            raise ValueError(f"不支持的模型类型: {model_type}")

# 使用示例
if __name__ == "__main__":
    # 示例1: 使用Ollama
    print("=== Ollama示例 ===")
    try:
        ollama_client = LocalModelFactory.create_client('ollama', model='llama2')
        response = ollama_client.generate("你好，请介绍一下Python")
        print(f"Ollama响应: {response}")
    except Exception as e:
        print(f"Ollama连接失败: {e}")
    
    # 示例2: 使用vLLM
    print("\n=== vLLM示例 ===")
    try:
        vllm_client = LocalModelFactory.create_client('vllm')
        messages = [
            {"role": "user", "content": "你好，请介绍一下Python"}
        ]
        response = vllm_client.chat(messages)
        print(f"vLLM响应: {response}")
    except Exception as e:
        print(f"vLLM连接失败: {e}")
    
    # 示例3: 使用LM Studio
    print("\n=== LM Studio示例 ===")
    try:
        lmstudio_client = LocalModelFactory.create_client('lmstudio')
        messages = [
            {"role": "user", "content": "你好，请介绍一下Python"}
        ]
        response = lmstudio_client.chat(messages)
        print(f"LM Studio响应: {response}")
    except Exception as e:
        print(f"LM Studio连接失败: {e}")