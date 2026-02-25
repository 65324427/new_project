"""
Trae AI 配置管理
管理Trae AI的API密钥和配置参数
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional

class TraeAIConfig:
    """
    Trae AI 配置管理类
    """
    
    CONFIG_FILE = Path(__file__).parent / 'trae_config.json'
    
    def __init__(self):
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """
        加载配置文件
        
        Returns:
            配置字典
        """
        if self.CONFIG_FILE.exists():
            try:
                with open(self.CONFIG_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f'加载配置文件失败: {e}')
                return self.get_default_config()
        else:
            return self.get_default_config()
    
    def save_config(self) -> bool:
        """
        保存配置文件
        
        Returns:
            保存是否成功
        """
        try:
            with open(self.CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
            return True
        except IOError as e:
            print(f'保存配置文件失败: {e}')
            return False
    
    def get_default_config(self) -> Dict[str, Any]:
        """
        获取默认配置
        
        Returns:
            默认配置字典
        """
        return {
            'api': {
                'api_key': os.getenv('TRAE_API_KEY', ''),
                'base_url': os.getenv('TRAE_API_URL', 'https://api.trae.ai/v1'),
                'timeout': 30,
                'max_retries': 3
            },
            'models': {
                'default_model': 'gpt-4o',
                'code_model': 'gpt-4o',
                'chat_model': 'gpt-4o',
                'explanation_model': 'claude-3.5'
            },
            'features': {
                'enable_code_generation': True,
                'enable_code_explanation': True,
                'enable_code_optimization': True,
                'enable_quiz_generation': True,
                'enable_learning_path_suggestion': True
            },
            'limits': {
                'max_tokens': 2000,
                'max_context_length': 4000,
                'temperature': 0.7
            }
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        获取配置值
        
        Args:
            key: 配置键（支持点号分隔的嵌套键，如'api.api_key'）
            default: 默认值
            
        Returns:
            配置值
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value if value is not None else default
    
    def set(self, key: str, value: Any) -> bool:
        """
        设置配置值
        
        Args:
            key: 配置键（支持点号分隔的嵌套键，如'api.api_key'）
            value: 配置值
            
        Returns:
            设置是否成功
        """
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        return self.save_config()
    
    def get_api_key(self) -> str:
        """
        获取API密钥
        
        Returns:
            API密钥字符串
        """
        return self.get('api.api_key', '')
    
    def set_api_key(self, api_key: str) -> bool:
        """
        设置API密钥
        
        Args:
            api_key: API密钥字符串
            
        Returns:
            设置是否成功
        """
        return self.set('api.api_key', api_key)
    
    def get_model(self, model_type: str = 'default') -> str:
        """
        获取模型配置
        
        Args:
            model_type: 模型类型（default/code/chat/explanation）
            
        Returns:
            模型名称
        """
        model_key = f'models.{model_type}_model'
        return self.get(model_key, 'gpt-4o')
    
    def set_model(self, model_type: str, model_name: str) -> bool:
        """
        设置模型
        
        Args:
            model_type: 模型类型（default/code/chat/explanation）
            model_name: 模型名称
            
        Returns:
            设置是否成功
        """
        model_key = f'models.{model_type}_model'
        return self.set(model_key, model_name)
    
    def is_feature_enabled(self, feature: str) -> bool:
        """
        检查功能是否启用
        
        Args:
            feature: 功能名称（code_generation/code_explanation等）
            
        Returns:
            功能是否启用
        """
        feature_key = f'features.enable_{feature}'
        return self.get(feature_key, True)
    
    def enable_feature(self, feature: str) -> bool:
        """
        启用功能
        
        Args:
            feature: 功能名称
            
        Returns:
            设置是否成功
        """
        feature_key = f'features.enable_{feature}'
        return self.set(feature_key, True)
    
    def disable_feature(self, feature: str) -> bool:
        """
        禁用功能
        
        Args:
            feature: 功能名称
            
        Returns:
            设置是否成功
        """
        feature_key = f'features.enable_{feature}'
        return self.set(feature_key, False)
    
    def get_limits(self) -> Dict[str, Any]:
        """
        获取所有限制配置
        
        Returns:
            限制配置字典
        """
        return self.config.get('limits', {})
    
    def set_limit(self, limit_name: str, value: Any) -> bool:
        """
        设置限制值
        
        Args:
            limit_name: 限制名称（max_tokens/temperature等）
            value: 限制值
            
        Returns:
            设置是否成功
        """
        limit_key = f'limits.{limit_name}'
        return self.set(limit_key, value)
    
    def validate_config(self) -> Dict[str, Any]:
        """
        验证配置
        
        Returns:
            验证结果字典，包含'valid'布尔值和'errors'列表
        """
        errors = []
        
        # 验证API密钥
        api_key = self.get_api_key()
        if not api_key:
            errors.append('API密钥未设置')
        
        # 验证URL
        base_url = self.get('api.base_url', '')
        if not base_url:
            errors.append('API基础URL未设置')
        
        # 验证模型配置
        models = ['default_model', 'code_model', 'chat_model', 'explanation_model']
        for model in models:
            model_name = self.get(f'models.{model}', '')
            if not model_name:
                errors.append(f'{model}未设置')
        
        # 验证限制值
        max_tokens = self.get('limits.max_tokens', 0)
        if max_tokens <= 0:
            errors.append('max_tokens必须大于0')
        
        temperature = self.get('limits.temperature', 0)
        if not (0 <= temperature <= 2):
            errors.append('temperature必须在0到2之间')
        
        return {
            'valid': len(errors) == 0,
            'errors': errors
        }
    
    def reset_to_default(self) -> bool:
        """
        重置为默认配置
        
        Returns:
            重置是否成功
        """
        self.config = self.get_default_config()
        return self.save_config()
    
    def export_config(self) -> str:
        """
        导出配置为JSON字符串
        
        Returns:
            配置JSON字符串
        """
        return json.dumps(self.config, ensure_ascii=False, indent=2)
    
    def import_config(self, config_str: str) -> bool:
        """
        从JSON字符串导入配置
        
        Args:
            config_str: 配置JSON字符串
            
        Returns:
            导入是否成功
        """
        try:
            config = json.loads(config_str)
            self.config = config
            return self.save_config()
        except json.JSONDecodeError as e:
            print(f'导入配置失败: {e}')
            return False


# 创建全局配置实例
trae_config = TraeAIConfig()


def get_trae_config() -> TraeAIConfig:
    """
    获取Trae AI配置实例（单例模式）
    
    Returns:
        TraeAIConfig实例
    """
    return trae_config