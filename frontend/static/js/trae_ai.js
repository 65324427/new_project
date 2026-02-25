/**
 * Trae AI 前端集成模块
 * 提供与后端Trae AI API交互的功能
 */

class TraeAIClient {
    constructor() {
        this.apiBaseUrl = 'http://localhost:5000/api/trae';
    }
    
    /**
     * 生成代码
     */
    async generateCode(prompt, language = 'python', context = null, maxTokens = 2000) {
        const response = await fetch(`${this.apiBaseUrl}/generate-code`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                prompt: prompt,
                language: language,
                context: context,
                max_tokens: maxTokens
            })
        });
        
        return await response.json();
    }
    
    /**
     * 解释代码
     */
    async explainCode(code, language = 'python') {
        const response = await fetch(`${this.apiBaseUrl}/explain-code`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                code: code,
                language: language
            })
        });
        
        return await response.json();
    }
    
    /**
     * 优化代码
     */
    async optimizeCode(code, language = 'python', optimizationType = 'performance') {
        const response = await fetch(`${this.apiBaseUrl}/optimize-code`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                code: code,
                language: language,
                optimization_type: optimizationType
            })
        });
        
        return await response.json();
    }
    
    /**
     * 调试代码
     */
    async debugCode(code, errorMessage = null, language = 'python') {
        const response = await fetch(`${this.apiBaseUrl}/debug-code`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                code: code,
                error_message: errorMessage,
                language: language
            })
        });
        
        return await response.json();
    }
    
    /**
     * AI对话
     */
    async chat(message, conversationHistory = null, model = 'gpt-4o') {
        const response = await fetch(`${this.apiBaseUrl}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                conversation_history: conversationHistory,
                model: model
            })
        });
        
        return await response.json();
    }
    
    /**
     * 分析课程内容
     */
    async analyzeContent(content, analysisType = 'completeness') {
        const response = await fetch(`${this.apiBaseUrl}/analyze-content`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                content: content,
                analysis_type: analysisType
            })
        });
        
        return await response.json();
    }
    
    /**
     * 生成测验题目
     */
    async generateQuiz(topic, difficulty = 'medium', count = 5) {
        const response = await fetch(`${this.apiBaseUrl}/generate-quiz`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                topic: topic,
                difficulty: difficulty,
                count: count
            })
        });
        
        return await response.json();
    }
    
    /**
     * 推荐学习路径
     */
    async suggestPath(userLevel, userGoals, availableTime = 10) {
        const response = await fetch(`${this.apiBaseUrl}/suggest-path`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_level: userLevel,
                user_goals: userGoals,
                available_time: availableTime
            })
        });
        
        return await response.json();
    }
    
    /**
     * 获取配置
     */
    async getConfig() {
        const response = await fetch(`${this.apiBaseUrl}/config`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        return await response.json();
    }
    
    /**
     * 设置API密钥
     */
    async setApiKey(apiKey) {
        const response = await fetch(`${this.apiBaseUrl}/config`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                action: 'set_api_key',
                api_key: apiKey
            })
        });
        
        return await response.json();
    }
    
    /**
     * 设置模型
     */
    async setModel(modelType, modelName) {
        const response = await fetch(`${this.apiBaseUrl}/config`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                action: 'set_model',
                model_type: modelType,
                model_name: modelName
            })
        });
        
        return await response.json();
    }
    
    /**
     * 启用功能
     */
    async enableFeature(feature) {
        const response = await fetch(`${this.apiBaseUrl}/config`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                action: 'enable_feature',
                feature: feature
            })
        });
        
        return await response.json();
    }
    
    /**
     * 禁用功能
     */
    async disableFeature(feature) {
        const response = await fetch(`${this.apiBaseUrl}/config`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                action: 'disable_feature',
                feature: feature
            })
        });
        
        return await response.json();
    }
    
    /**
     * 重置配置
     */
    async resetConfig() {
        const response = await fetch(`${this.apiBaseUrl}/config`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                action: 'reset'
            })
        });
        
        return await response.json();
    }
}

// 创建全局Trae AI客户端实例
const traeAI = new TraeAIClient();

// 导出到全局作用域
window.traeAI = traeAI;