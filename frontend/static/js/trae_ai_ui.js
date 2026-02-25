/**
 * Trae AI 功能UI组件
 * 提供代码生成、代码解释、代码优化等功能界面
 */

class TraeAIUI {
    constructor() {
        this.isInitialized = false;
        this.init();
    }
    
    init() {
        if (this.isInitialized) return;
        
        this.createTraeAIPanel();
        this.setupEventListeners();
        this.isInitialized = true;
    }
    
    createTraeAIPanel() {
        const existingPanel = document.getElementById('trae-ai-panel');
        if (existingPanel) return;
        
        const panel = document.createElement('div');
        panel.id = 'trae-ai-panel';
        panel.className = 'trae-ai-panel';
        panel.innerHTML = `
            <div class="trae-ai-header">
                <h3>🤖 Trae AI 助手</h3>
                <button class="trae-ai-toggle" onclick="traeAIUI.togglePanel()">
                    <span class="toggle-icon">▼</span>
                </button>
            </div>
            <div class="trae-ai-content">
                <div class="trae-ai-tabs">
                    <button class="tab-btn active" data-tab="generate-code" onclick="traeAIUI.switchTab('generate-code')">
                        <span>📝</span> 代码生成
                    </button>
                    <button class="tab-btn" data-tab="explain-code" onclick="traeAIUI.switchTab('explain-code')">
                        <span>💡</span> 代码解释
                    </button>
                    <button class="tab-btn" data-tab="optimize-code" onclick="traeAIUI.switchTab('optimize-code')">
                        <span>⚡</span> 代码优化
                    </button>
                    <button class="tab-btn" data-tab="debug-code" onclick="traeAIUI.switchTab('debug-code')">
                        <span>🐛</span> 代码调试
                    </button>
                    <button class="tab-btn" data-tab="chat" onclick="traeAIUI.switchTab('chat')">
                        <span>💬</span> AI对话
                    </button>
                </div>
                
                <div class="trae-ai-tab-content" id="tab-generate-code">
                    <div class="ai-input-group">
                        <label>生成提示词</label>
                        <textarea id="generate-prompt" placeholder="描述你想要生成的代码功能..."></textarea>
                    </div>
                    <div class="ai-input-group">
                        <label>编程语言</label>
                        <select id="generate-language">
                            <option value="python">Python</option>
                            <option value="javascript">JavaScript</option>
                            <option value="java">Java</option>
                            <option value="cpp">C++</option>
                            <option value="go">Go</option>
                        </select>
                    </div>
                    <div class="ai-input-group">
                        <label>上下文代码（可选）</label>
                        <textarea id="generate-context" placeholder="提供相关的代码上下文..."></textarea>
                    </div>
                    <div class="ai-input-group">
                        <label>最大Token数</label>
                        <input type="number" id="generate-max-tokens" value="2000" min="100" max="4000">
                    </div>
                    <button class="ai-action-btn" onclick="traeAIUI.generateCode()">
                        <span>🚀</span> 生成代码
                    </button>
                    <div class="ai-result" id="generate-result"></div>
                </div>
                
                <div class="trae-ai-tab-content" id="tab-explain-code" style="display: none;">
                    <div class="ai-input-group">
                        <label>需要解释的代码</label>
                        <textarea id="explain-code-input" placeholder="粘贴需要解释的代码..."></textarea>
                    </div>
                    <div class="ai-input-group">
                        <label>代码语言</label>
                        <select id="explain-language">
                            <option value="python">Python</option>
                            <option value="javascript">JavaScript</option>
                            <option value="java">Java</option>
                            <option value="cpp">C++</option>
                        </select>
                    </div>
                    <button class="ai-action-btn" onclick="traeAIUI.explainCode()">
                        <span>💡</span> 解释代码
                    </button>
                    <div class="ai-result" id="explain-result"></div>
                </div>
                
                <div class="trae-ai-tab-content" id="tab-optimize-code" style="display: none;">
                    <div class="ai-input-group">
                        <label>需要优化的代码</label>
                        <textarea id="optimize-code-input" placeholder="粘贴需要优化的代码..."></textarea>
                    </div>
                    <div class="ai-input-group">
                        <label>代码语言</label>
                        <select id="optimize-language">
                            <option value="python">Python</option>
                            <option value="javascript">JavaScript</option>
                            <option value="java">Java</option>
                        </select>
                    </div>
                    <div class="ai-input-group">
                        <label>优化类型</label>
                        <select id="optimize-type">
                            <option value="performance">性能优化</option>
                            <option value="readability">可读性优化</option>
                            <option value="security">安全优化</option>
                        </select>
                    </div>
                    <button class="ai-action-btn" onclick="traeAIUI.optimizeCode()">
                        <span>⚡</span> 优化代码
                    </button>
                    <div class="ai-result" id="optimize-result"></div>
                </div>
                
                <div class="trae-ai-tab-content" id="tab-debug-code" style="display: none;">
                    <div class="ai-input-group">
                        <label>需要调试的代码</label>
                        <textarea id="debug-code-input" placeholder="粘贴需要调试的代码..."></textarea>
                    </div>
                    <div class="ai-input-group">
                        <label>错误信息（可选）</label>
                        <textarea id="debug-error-input" placeholder="如果有错误信息，请输入..."></textarea>
                    </div>
                    <div class="ai-input-group">
                        <label>代码语言</label>
                        <select id="debug-language">
                            <option value="python">Python</option>
                            <option value="javascript">JavaScript</option>
                            <option value="java">Java</option>
                        </select>
                    </div>
                    <button class="ai-action-btn" onclick="traeAIUI.debugCode()">
                        <span>🐛</span> 调试代码
                    </button>
                    <div class="ai-result" id="debug-result"></div>
                </div>
                
                <div class="trae-ai-tab-content" id="tab-chat" style="display: none;">
                    <div class="chat-container">
                        <div class="chat-messages" id="chat-messages"></div>
                        <div class="chat-input-area">
                            <textarea id="chat-input" placeholder="与AI对话..."></textarea>
                            <button class="send-btn" onclick="traeAIUI.sendMessage()">
                                <span>发送</span>
                            </button>
                        </div>
                    </div>
                </div>
                
                <div class="trae-ai-footer">
                    <button class="config-btn" onclick="traeAIUI.showConfig()">
                        <span>⚙️</span> 配置
                    </button>
                    <button class="close-btn" onclick="traeAIUI.closePanel()">
                        <span>✕</span> 关闭
                    </button>
                </div>
            </div>
        `;
        
        document.body.appendChild(panel);
    }
    
    setupEventListeners() {
        // 快捷键支持
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'k') {
                e.preventDefault();
                this.openPanel();
            }
            if (e.ctrlKey && e.key === 'l') {
                e.preventDefault();
                this.openPanel();
            }
        });
    }
    
    togglePanel() {
        const panel = document.getElementById('trae-ai-panel');
        const content = panel.querySelector('.trae-ai-content');
        const toggleIcon = panel.querySelector('.toggle-icon');
        
        if (content.style.display === 'none') {
            content.style.display = 'block';
            toggleIcon.textContent = '▼';
        } else {
            content.style.display = 'none';
            toggleIcon.textContent = '▶';
        }
    }
    
    openPanel() {
        const panel = document.getElementById('trae-ai-panel');
        const content = panel.querySelector('.trae-ai-content');
        content.style.display = 'block';
        const toggleIcon = panel.querySelector('.toggle-icon');
        toggleIcon.textContent = '▼';
    }
    
    closePanel() {
        const panel = document.getElementById('trae-ai-panel');
        panel.remove();
        this.isInitialized = false;
    }
    
    switchTab(tabName) {
        const tabs = document.querySelectorAll('.tab-btn');
        const contents = document.querySelectorAll('.trae-ai-tab-content');
        
        tabs.forEach(tab => {
            tab.classList.remove('active');
            if (tab.dataset.tab === tabName) {
                tab.classList.add('active');
            }
        });
        
        contents.forEach(content => {
            content.style.display = 'none';
            if (content.id === `tab-${tabName}`) {
                content.style.display = 'block';
            }
        });
    }
    
    async generateCode() {
        const prompt = document.getElementById('generate-prompt').value;
        const language = document.getElementById('generate-language').value;
        const context = document.getElementById('generate-context').value || null;
        const maxTokens = parseInt(document.getElementById('generate-max-tokens').value);
        const resultDiv = document.getElementById('generate-result');
        
        if (!prompt.trim()) {
            this.showError(resultDiv, '请输入生成提示词');
            return;
        }
        
        this.showLoading(resultDiv);
        
        try {
            const result = await window.traeAI.generateCode(prompt, language, context, maxTokens);
            
            if (result.success) {
                this.showCodeResult(resultDiv, result.code, language);
            } else {
                this.showError(resultDiv, result.error || '生成失败');
            }
        } catch (error) {
            this.showError(resultDiv, `网络错误: ${error.message}`);
        }
    }
    
    async explainCode() {
        const code = document.getElementById('explain-code-input').value;
        const language = document.getElementById('explain-language').value;
        const resultDiv = document.getElementById('explain-result');
        
        if (!code.trim()) {
            this.showError(resultDiv, '请输入需要解释的代码');
            return;
        }
        
        this.showLoading(resultDiv);
        
        try {
            const result = await window.traeAI.explainCode(code, language);
            
            if (result.success) {
                this.showTextResult(resultDiv, result.explanation);
            } else {
                this.showError(resultDiv, result.error || '解释失败');
            }
        } catch (error) {
            this.showError(resultDiv, `网络错误: ${error.message}`);
        }
    }
    
    async optimizeCode() {
        const code = document.getElementById('optimize-code-input').value;
        const language = document.getElementById('optimize-language').value;
        const optimizationType = document.getElementById('optimize-type').value;
        const resultDiv = document.getElementById('optimize-result');
        
        if (!code.trim()) {
            this.showError(resultDiv, '请输入需要优化的代码');
            return;
        }
        
        this.showLoading(resultDiv);
        
        try {
            const result = await window.traeAI.optimizeCode(code, language, optimizationType);
            
            if (result.success) {
                this.showCodeResult(resultDiv, result.optimized_code, language);
            } else {
                this.showError(resultDiv, result.error || '优化失败');
            }
        } catch (error) {
            this.showError(resultDiv, `网络错误: ${error.message}`);
        }
    }
    
    async debugCode() {
        const code = document.getElementById('debug-code-input').value;
        const errorMessage = document.getElementById('debug-error-input').value || null;
        const language = document.getElementById('debug-language').value;
        const resultDiv = document.getElementById('debug-result');
        
        if (!code.trim()) {
            this.showError(resultDiv, '请输入需要调试的代码');
            return;
        }
        
        this.showLoading(resultDiv);
        
        try {
            const result = await window.traeAI.debugCode(code, errorMessage, language);
            
            if (result.success) {
                this.showTextResult(resultDiv, result.suggestions);
            } else {
                this.showError(resultDiv, result.error || '调试失败');
            }
        } catch (error) {
            this.showError(resultDiv, `网络错误: ${error.message}`);
        }
    }
    
    async sendMessage() {
        const message = document.getElementById('chat-input').value;
        const messagesDiv = document.getElementById('chat-messages');
        
        if (!message.trim()) {
            return;
        }
        
        this.addChatMessage(message, 'user');
        document.getElementById('chat-input').value = '';
        
        try {
            const result = await window.traeAI.chat(message);
            
            if (result.success) {
                this.addChatMessage(result.response, 'ai');
            } else {
                this.addChatMessage(result.error || '发送失败', 'error');
            }
        } catch (error) {
            this.addChatMessage(`网络错误: ${error.message}`, 'error');
        }
    }
    
    addChatMessage(message, type) {
        const messagesDiv = document.getElementById('chat-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `chat-message chat-message-${type}`;
        messageDiv.innerHTML = `
            <div class="chat-content">${this.escapeHtml(message)}</div>
            <div class="chat-time">${new Date().toLocaleTimeString()}</div>
        `;
        messagesDiv.appendChild(messageDiv);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }
    
    showCodeResult(resultDiv, code, language) {
        resultDiv.innerHTML = `
            <div class="result-success">
                <div class="result-header">
                    <span class="result-icon">✅</span>
                    <span class="result-title">生成成功</span>
                </div>
                <pre class="code-display"><code class="language-${language}">${this.escapeHtml(code)}</code></pre>
                <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.querySelector('code').textContent)">
                    <span>📋</span> 复制
                </button>
            </div>
        `;
    }
    
    showTextResult(resultDiv, text) {
        resultDiv.innerHTML = `
            <div class="result-success">
                <div class="result-header">
                    <span class="result-icon">✅</span>
                    <span class="result-title">处理成功</span>
                </div>
                <div class="text-display">${this.escapeHtml(text)}</div>
                <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.querySelector('.text-display').textContent)">
                    <span>📋</span> 复制
                </button>
            </div>
        `;
    }
    
    showError(resultDiv, message) {
        resultDiv.innerHTML = `
            <div class="result-error">
                <div class="result-header">
                    <span class="result-icon">❌</span>
                    <span class="result-title">错误</span>
                </div>
                <div class="error-message">${this.escapeHtml(message)}</div>
            </div>
        `;
    }
    
    showLoading(resultDiv) {
        resultDiv.innerHTML = `
            <div class="result-loading">
                <div class="loading-spinner"></div>
                <div class="loading-text">处理中...</div>
            </div>
        `;
    }
    
    showConfig() {
        const configPanel = document.createElement('div');
        configPanel.className = 'trae-config-panel';
        configPanel.innerHTML = `
            <div class="config-header">
                <h3>⚙️ Trae AI 配置</h3>
                <button class="close-btn" onclick="this.parentElement.remove()">✕</button>
            </div>
            <div class="config-content">
                <div class="config-group">
                    <label>API密钥</label>
                    <input type="password" id="config-api-key" placeholder="输入Trae API密钥">
                </div>
                <div class="config-group">
                    <label>默认模型</label>
                    <select id="config-default-model">
                        <option value="gpt-4o">GPT-4o</option>
                        <option value="claude-3.5">Claude 3.5</option>
                        <option value="sonnet">Sonnet</option>
                    </select>
                </div>
                <div class="config-actions">
                    <button class="config-action-btn" onclick="traeAIUI.saveConfig()">
                        <span>💾</span> 保存配置
                    </button>
                    <button class="config-action-btn secondary" onclick="traeAIUI.resetConfig()">
                        <span>🔄</span> 重置默认
                    </button>
                </div>
            </div>
        `;
        
        document.body.appendChild(configPanel);
    }
    
    async saveConfig() {
        const apiKey = document.getElementById('config-api-key').value;
        const defaultModel = document.getElementById('config-default-model').value;
        
        if (apiKey.trim()) {
            await window.traeAI.setApiKey(apiKey);
        }
        
        await window.traeAI.setModel('default', defaultModel);
        
        alert('配置已保存！');
        document.querySelector('.trae-config-panel').remove();
    }
    
    async resetConfig() {
        await window.traeAI.resetConfig();
        alert('配置已重置为默认值！');
        document.querySelector('.trae-config-panel').remove();
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// 创建全局Trae AI UI实例
const traeAIUI = new TraeAIUI();

// 导出到全局作用域
window.traeAIUI = traeAIUI;