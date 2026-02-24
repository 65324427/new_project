// 用户管理系统
class UserManager {
    constructor() {
        this.currentUser = null;
        this.users = this.loadUsers();
        this.init();
    }

    init() {
        this.checkLoginStatus();
        this.setupEventListeners();
        this.updateUserDisplay();
    }

    loadUsers() {
        const saved = localStorage.getItem('users');
        if (saved) {
            return JSON.parse(saved);
        }
        return {};
    }

    saveUsers() {
        localStorage.setItem('users', JSON.stringify(this.users));
    }

    checkLoginStatus() {
        const currentUserId = localStorage.getItem('currentUserId');
        if (currentUserId && this.users[currentUserId]) {
            this.currentUser = this.users[currentUserId];
        }
    }

    setupEventListeners() {
        const loginBtn = document.getElementById('login-btn');
        const registerBtn = document.getElementById('register-btn');
        const logoutBtn = document.getElementById('logout-btn');

        if (loginBtn) {
            loginBtn.addEventListener('click', () => this.showLoginModal());
        }

        if (registerBtn) {
            registerBtn.addEventListener('click', () => this.showRegisterModal());
        }

        if (logoutBtn) {
            logoutBtn.addEventListener('click', () => this.logout());
        }
    }

    register(username, email, password, confirmPassword) {
        const errors = this.validateRegistration(username, email, password, confirmPassword);
        if (errors.length > 0) {
            return { success: false, errors };
        }

        const userId = this.generateUserId();
        const user = {
            id: userId,
            username: username,
            email: email,
            password: this.hashPassword(password),
            createdAt: new Date().toISOString(),
            lastLogin: null,
            settings: {
                theme: 'light',
                notifications: true,
                language: 'zh-CN'
            },
            progress: {
                totalProgress: 0,
                completedSections: [],
                sectionProgress: {},
                totalTime: 0,
                lastStudied: null,
                sessions: []
            },
            statistics: {
                totalSessions: 0,
                averageSessionTime: 0,
                longestSession: 0,
                streakDays: 0,
                lastStudyDate: null
            }
        };

        this.users[userId] = user;
        this.saveUsers();
        
        return { success: true, user };
    }

    validateRegistration(username, email, password, confirmPassword) {
        const errors = [];

        if (!username || username.length < 3) {
            errors.push('用户名至少需要3个字符');
        }

        if (!email || !this.isValidEmail(email)) {
            errors.push('请输入有效的邮箱地址');
        }

        if (!password || password.length < 6) {
            errors.push('密码至少需要6个字符');
        }

        if (password !== confirmPassword) {
            errors.push('两次输入的密码不一致');
        }

        if (this.isUsernameTaken(username)) {
            errors.push('用户名已被使用');
        }

        if (this.isEmailTaken(email)) {
            errors.push('邮箱已被注册');
        }

        return errors;
    }

    isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    isUsernameTaken(username) {
        return Object.values(this.users).some(user => user.username === username);
    }

    isEmailTaken(email) {
        return Object.values(this.users).some(user => user.email === email);
    }

    login(usernameOrEmail, password) {
        const user = this.findUserByUsernameOrEmail(usernameOrEmail);
        
        if (!user) {
            return { success: false, error: '用户名或邮箱不存在' };
        }

        if (user.password !== this.hashPassword(password)) {
            return { success: false, error: '密码错误' };
        }

        user.lastLogin = new Date().toISOString();
        this.users[user.id] = user;
        this.saveUsers();

        this.currentUser = user;
        localStorage.setItem('currentUserId', user.id);

        return { success: true, user };
    }

    logout() {
        if (this.currentUser) {
            this.currentUser = null;
            localStorage.removeItem('currentUserId');
            this.updateUserDisplay();
            this.showLoginModal();
        }
    }

    findUserByUsernameOrEmail(usernameOrEmail) {
        return Object.values(this.users).find(user => 
            user.username === usernameOrEmail || user.email === usernameOrEmail
        );
    }

    generateUserId() {
        return 'user_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }

    hashPassword(password) {
        let hash = 0;
        for (let i = 0; i < password.length; i++) {
            const char = password.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash;
        }
        return hash.toString();
    }

    updateUserDisplay() {
        const userInfo = document.getElementById('user-info');
        const loginBtn = document.getElementById('login-btn');
        const registerBtn = document.getElementById('register-btn');
        const logoutBtn = document.getElementById('logout-btn');

        if (this.currentUser) {
            if (userInfo) {
                userInfo.innerHTML = `
                    <div class="user-avatar" onclick="userManager.showProfileModal()" style="cursor: pointer;">
                        <span class="avatar-text">${this.currentUser.username.charAt(0).toUpperCase()}</span>
                    </div>
                    <div class="user-details">
                        <span class="user-name">${this.currentUser.username}</span>
                        <span class="user-email">${this.currentUser.email}</span>
                    </div>
                `;
            }

            if (loginBtn) loginBtn.style.display = 'none';
            if (registerBtn) registerBtn.style.display = 'none';
            if (logoutBtn) logoutBtn.style.display = 'none';
        } else {
            if (userInfo) {
                userInfo.innerHTML = `
                    <p>请登录或注册以保存学习进度</p>
                `;
            }

            if (loginBtn) loginBtn.style.display = 'block';
            if (registerBtn) registerBtn.style.display = 'block';
            if (logoutBtn) logoutBtn.style.display = 'none';
        }
    }

    showLoginModal() {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.id = 'login-modal';
        modal.style.display = 'block';
        modal.innerHTML = `
            <div class="modal-content" style="max-width: 400px;">
                <span class="close" onclick="this.closest('.modal').remove()">&times;</span>
                <h3>用户登录</h3>
                <form id="login-form">
                    <div class="form-group">
                        <label for="login-username">用户名或邮箱</label>
                        <input type="text" id="login-username" required>
                    </div>
                    <div class="form-group">
                        <label for="login-password">密码</label>
                        <input type="password" id="login-password" required>
                    </div>
                    <div class="form-error" id="login-error"></div>
                    <button type="submit">登录</button>
                    <p class="form-footer">
                        还没有账号？<a href="#" onclick="userManager.showRegisterModal(); this.closest('.modal').remove(); return false;">立即注册</a>
                    </p>
                </form>
            </div>
        `;

        document.body.appendChild(modal);

        document.getElementById('login-form').addEventListener('submit', (e) => {
            e.preventDefault();
            const username = document.getElementById('login-username').value;
            const password = document.getElementById('login-password').value;
            
            const result = this.login(username, password);
            
            if (result.success) {
                modal.remove();
                this.updateUserDisplay();
                this.showSuccessMessage('登录成功！');
            } else {
                document.getElementById('login-error').textContent = result.error;
            }
        });
    }

    showRegisterModal() {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.id = 'register-modal';
        modal.style.display = 'block';
        modal.innerHTML = `
            <div class="modal-content" style="max-width: 400px;">
                <span class="close" onclick="this.closest('.modal').remove()">&times;</span>
                <h3>用户注册</h3>
                <form id="register-form">
                    <div class="form-group">
                        <label for="register-username">用户名</label>
                        <input type="text" id="register-username" required minlength="3">
                    </div>
                    <div class="form-group">
                        <label for="register-email">邮箱</label>
                        <input type="email" id="register-email" required>
                    </div>
                    <div class="form-group">
                        <label for="register-password">密码</label>
                        <input type="password" id="register-password" required minlength="6">
                    </div>
                    <div class="form-group">
                        <label for="register-confirm-password">确认密码</label>
                        <input type="password" id="register-confirm-password" required>
                    </div>
                    <div class="form-error" id="register-error"></div>
                    <button type="submit">注册</button>
                    <p class="form-footer">
                        已有账号？<a href="#" onclick="userManager.showLoginModal(); this.closest('.modal').remove(); return false;">立即登录</a>
                    </p>
                </form>
            </div>
        `;

        document.body.appendChild(modal);

        document.getElementById('register-form').addEventListener('submit', (e) => {
            e.preventDefault();
            const username = document.getElementById('register-username').value;
            const email = document.getElementById('register-email').value;
            const password = document.getElementById('register-password').value;
            const confirmPassword = document.getElementById('register-confirm-password').value;
            
            const result = this.register(username, email, password, confirmPassword);
            
            if (result.success) {
                modal.remove();
                this.showSuccessMessage('注册成功！请登录');
                this.showLoginModal();
            } else {
                document.getElementById('register-error').innerHTML = result.errors.map(e => `<p>${e}</p>`).join('');
            }
        });
    }

    showSuccessMessage(message) {
        const toast = document.createElement('div');
        toast.className = 'toast success';
        toast.textContent = message;
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.classList.add('show');
        }, 10);
        
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }

    updateProgress(progressData) {
        if (this.currentUser) {
            this.currentUser.progress = progressData;
            this.users[this.currentUser.id] = this.currentUser;
            this.saveUsers();
        }
    }

    getProgress() {
        return this.currentUser ? this.currentUser.progress : null;
    }

    updateSettings(settings) {
        if (this.currentUser) {
            this.currentUser.settings = { ...this.currentUser.settings, ...settings };
            this.users[this.currentUser.id] = this.currentUser;
            this.saveUsers();
        }
    }

    getSettings() {
        return this.currentUser ? this.currentUser.settings : null;
    }

    showSettingsModal() {
        if (!this.currentUser) {
            this.showLoginModal();
            return;
        }

        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.id = 'settings-modal';
        modal.style.display = 'block';
        modal.innerHTML = `
            <div class="modal-content" style="max-width: 500px;">
                <span class="close" onclick="this.closest('.modal').remove()">&times;</span>
                <h3>用户设置</h3>
                <form id="settings-form">
                    <div class="form-group">
                        <label for="settings-theme">主题</label>
                        <select id="settings-theme" class="form-select">
                            <option value="light" ${this.currentUser.settings.theme === 'light' ? 'selected' : ''}>浅色</option>
                            <option value="dark" ${this.currentUser.settings.theme === 'dark' ? 'selected' : ''}>深色</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="settings-language">语言</label>
                        <select id="settings-language" class="form-select">
                            <option value="zh-CN" ${this.currentUser.settings.language === 'zh-CN' ? 'selected' : ''}>简体中文</option>
                            <option value="en-US" ${this.currentUser.settings.language === 'en-US' ? 'selected' : ''}>English</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>
                            <input type="checkbox" id="settings-notifications" 
                                   ${this.currentUser.settings.notifications ? 'checked' : ''}>
                            启用通知
                        </label>
                    </div>
                    <div class="form-group">
                        <label>用户信息</label>
                        <div class="user-info-display">
                            <p><strong>用户名：</strong>${this.currentUser.username}</p>
                            <p><strong>邮箱：</strong>${this.currentUser.email}</p>
                            <p><strong>注册时间：</strong>${new Date(this.currentUser.createdAt).toLocaleString('zh-CN')}</p>
                            <p><strong>最后登录：</strong>${this.currentUser.lastLogin ? new Date(this.currentUser.lastLogin).toLocaleString('zh-CN') : '首次登录'}</p>
                        </div>
                    </div>
                    <button type="submit">保存设置</button>
                </form>
            </div>
        `;

        document.body.appendChild(modal);

        document.getElementById('settings-form').addEventListener('submit', (e) => {
            e.preventDefault();
            
            const settings = {
                theme: document.getElementById('settings-theme').value,
                language: document.getElementById('settings-language').value,
                notifications: document.getElementById('settings-notifications').checked
            };
            
            this.updateSettings(settings);
            modal.remove();
            this.showSuccessMessage('设置已保存！');
        });
    }

    showProfileModal() {
        if (!this.currentUser) {
            this.showLoginModal();
            return;
        }

        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.id = 'profile-modal';
        modal.style.display = 'block';
        modal.innerHTML = `
            <div class="modal-content" style="max-width: 500px;">
                <span class="close" onclick="this.closest('.modal').remove()">&times;</span>
                <h3>用户资料</h3>
                <div class="profile-content">
                    <div class="profile-avatar-large">
                        <span class="avatar-text-large">${this.currentUser.username.charAt(0).toUpperCase()}</span>
                    </div>
                    <div class="profile-info">
                        <h4>${this.currentUser.username}</h4>
                        <p>${this.currentUser.email}</p>
                    </div>
                    <div class="profile-stats">
                        <div class="stat-card">
                            <span class="stat-value">${this.currentUser.progress.completedSections.length}</span>
                            <span class="stat-label">已完成章节</span>
                        </div>
                        <div class="stat-card">
                            <span class="stat-value">${this.currentUser.progress.totalProgress}%</span>
                            <span class="stat-label">总进度</span>
                        </div>
                        <div class="stat-card">
                            <span class="stat-value">${Math.floor(this.currentUser.progress.totalTime / 60)}h</span>
                            <span class="stat-label">学习时长</span>
                        </div>
                    </div>
                    <div class="profile-actions">
                        <button type="button" class="btn btn-primary" onclick="userManager.showSettingsModal(); this.closest('.modal').remove();">设置</button>
                        <button type="button" class="btn btn-danger" onclick="userManager.logout(); this.closest('.modal').remove();">退出登录</button>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(modal);
    }
}

// 初始化用户管理器
let userManager;

document.addEventListener('DOMContentLoaded', function() {
    userManager = new UserManager();
    window.userManager = userManager;
});