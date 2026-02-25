"""
Trae AI 集成模块
提供AI辅助功能，包括代码生成、代码解释、代码优化等
"""

import requests
import json
import os
from typing import Dict, List, Optional, Any

class TraeAI:
    """
    Trae AI 客户端类
    用于与Trae AI服务进行交互
    """
    
    def __init__(self, api_key: str = None, base_url: str = None):
        """
        初始化Trae AI客户端
        
        Args:
            api_key: Trae API密钥（可选）
            base_url: Trae API基础URL（可选）
        """
        self.api_key = api_key or os.getenv('TRAE_API_KEY', '')
        self.base_url = base_url or os.getenv('TRAE_API_URL', 'https://api.trae.ai/v1')
        self.session = requests.Session()
        
        if self.api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            })
    
    def generate_code(self, prompt: str, language: str = 'python', 
                   context: str = None, max_tokens: int = 2000) -> Dict[str, Any]:
        """
        生成代码
        
        Args:
            prompt: 代码生成提示词
            language: 目标编程语言
            context: 代码上下文
            max_tokens: 最大token数
            
        Returns:
            包含生成代码和元数据的字典
        """
        endpoint = f'{self.base_url}/code/generate'
        
        payload = {
            'prompt': prompt,
            'language': language,
            'max_tokens': max_tokens
        }
        
        if context:
            payload['context'] = context
        
        try:
            response = self.session.post(endpoint, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'code': None
            }
    
    def explain_code(self, code: str, language: str = 'python') -> Dict[str, Any]:
        """
        解释代码
        
        Args:
            code: 需要解释的代码
            language: 代码语言
            
        Returns:
            包含代码解释的字典
        """
        endpoint = f'{self.base_url}/code/explain'
        
        payload = {
            'code': code,
            'language': language
        }
        
        try:
            response = self.session.post(endpoint, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'explanation': None
            }
    
    def optimize_code(self, code: str, language: str = 'python', 
                    optimization_type: str = 'performance') -> Dict[str, Any]:
        """
        优化代码
        
        Args:
            code: 需要优化的代码
            language: 代码语言
            optimization_type: 优化类型（performance/readability/security）
            
        Returns:
            包含优化后代码的字典
        """
        endpoint = f'{self.base_url}/code/optimize'
        
        payload = {
            'code': code,
            'language': language,
            'optimization_type': optimization_type
        }
        
        try:
            response = self.session.post(endpoint, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'optimized_code': None
            }
    
    def debug_code(self, code: str, error_message: str = None, 
                 language: str = 'python') -> Dict[str, Any]:
        """
        调试代码
        
        Args:
            code: 需要调试的代码
            error_message: 错误信息
            language: 代码语言
            
        Returns:
            包含调试建议的字典
        """
        endpoint = f'{self.base_url}/code/debug'
        
        payload = {
            'code': code,
            'language': language
        }
        
        if error_message:
            payload['error_message'] = error_message
        
        try:
            response = self.session.post(endpoint, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'suggestions': None
            }
    
    def chat(self, message: str, conversation_history: List[Dict] = None,
              model: str = 'gpt-4o') -> Dict[str, Any]:
        """
        AI对话
        
        Args:
            message: 用户消息
            conversation_history: 对话历史
            model: 使用的AI模型
            
        Returns:
            包含AI回复的字典
        """
        endpoint = f'{self.base_url}/chat'
        
        payload = {
            'message': message,
            'model': model
        }
        
        if conversation_history:
            payload['conversation_history'] = conversation_history
        
        try:
            response = self.session.post(endpoint, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'response': None
            }
    
    def analyze_course_content(self, content: str, analysis_type: str = 'completeness') -> Dict[str, Any]:
        """
        分析课程内容
        
        Args:
            content: 课程内容
            analysis_type: 分析类型（completeness/quality/relevance）
            
        Returns:
            包含分析结果的字典
        """
        endpoint = f'{self.base_url}/content/analyze'
        
        payload = {
            'content': content,
            'analysis_type': analysis_type
        }
        
        try:
            response = self.session.post(endpoint, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'analysis': None
            }
    
    def generate_quiz_questions(self, topic: str, difficulty: str = 'medium',
                            count: int = 5) -> Dict[str, Any]:
        """
        生成测验题目
        
        Args:
            topic: 测验主题
            difficulty: 难度级别（easy/medium/hard）
            count: 题目数量
            
        Returns:
            包含测验题目的字典
        """
        endpoint = f'{self.base_url}/quiz/generate'
        
        payload = {
            'topic': topic,
            'difficulty': difficulty,
            'count': count
        }
        
        try:
            response = self.session.post(endpoint, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'questions': None
            }
    
    def suggest_learning_path(self, user_level: str, user_goals: List[str],
                           available_time: int = 10) -> Dict[str, Any]:
        """
        推荐学习路径
        
        Args:
            user_level: 用户水平（beginner/intermediate/advanced）
            user_goals: 用户目标列表
            available_time: 可用学习时间（小时）
            
        Returns:
            包含推荐学习路径的字典
        """
        endpoint = f'{self.base_url}/learning/path'
        
        payload = {
            'user_level': user_level,
            'user_goals': user_goals,
            'available_time': available_time
        }
        
        try:
            response = self.session.post(endpoint, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': str(e),
                'suggestions': None
            }


# 创建全局Trae AI实例
trae_ai = TraeAI()


def get_trae_ai() -> TraeAI:
    """
    获取Trae AI实例（单例模式）
    
    Returns:
        TraeAI实例
    """
    return trae_ai