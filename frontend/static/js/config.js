// 前端配置
const CONFIG = {
    // API基础URL
    API_BASE_URL: 'http://localhost:5000/api',
    
    // 是否使用后端API（true）还是本地存储（false）
    USE_BACKEND_API: true,
    
    // 本地存储键名
    STORAGE_KEYS: {
        USERS: 'users',
        CURRENT_USER: 'currentUserId',
        LEARNING_PROGRESS: 'learningProgress'
    },
    
    // API端点
    API_ENDPOINTS: {
        USERS: '/users',
        PROGRESS: '/progress',
        HEALTH: '/health'
    },
    
    // 默认设置
    DEFAULT_SETTINGS: {
        theme: 'light',
        notifications: true,
        language: 'zh-CN'
    }
};

// API请求工具类
class ApiClient {
    constructor() {
        this.baseUrl = CONFIG.API_BASE_URL;
    }
    
    async request(endpoint, options = {}) {
        const url = this.baseUrl + endpoint;
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        };
        
        try {
            const response = await fetch(url, config);
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('API请求失败:', error);
            return { success: false, error: '网络错误' };
        }
    }
    
    async register(userData) {
        return await this.request(CONFIG.API_ENDPOINTS.USERS, {
            method: 'POST',
            body: JSON.stringify({
                action: 'register',
                ...userData
            })
        });
    }
    
    async login(credentials) {
        return await this.request(CONFIG.API_ENDPOINTS.USERS, {
            method: 'POST',
            body: JSON.stringify({
                action: 'login',
                ...credentials
            })
        });
    }
    
    async updateProgress(userId, progressData) {
        return await this.request(CONFIG.API_ENDPOINTS.PROGRESS, {
            method: 'POST',
            body: JSON.stringify({
                userId: userId,
                progress: progressData
            })
        });
    }
    
    async getProgress(userId) {
        return await this.request(CONFIG.API_ENDPOINTS.PROGRESS + `?userId=${userId}`, {
            method: 'GET'
        });
    }
    
    async updateSectionStatus(userId, sectionId, action) {
        return await this.request(CONFIG.API_ENDPOINTS.PROGRESS, {
            method: 'PUT',
            body: JSON.stringify({
                userId: userId,
                sectionId: sectionId,
                action: action
            })
        });
    }
    
    async healthCheck() {
        return await this.request(CONFIG.API_ENDPOINTS.HEALTH, {
            method: 'GET'
        });
    }
}

// 创建全局API客户端实例
const apiClient = new ApiClient();