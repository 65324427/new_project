// 学习进度跟踪系统
class LearningProgressTracker {
    constructor() {
        this.progressData = this.loadProgressData();
        this.currentSessionStartTime = null;
        this.currentSection = null;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.updateProgressDisplay();
        this.startSessionTracking();
        
        // 定期保存学习时长（每30秒）
        this.saveInterval = setInterval(() => {
            this.saveCurrentSession();
        }, 30000);
        
        // 等待内容加载完成后再次更新
        setTimeout(() => {
            this.updateProgressDisplay();
        }, 1000);
    }

    loadProgressData() {
        if (window.userManager && window.userManager.currentUser) {
            return window.userManager.getProgress() || this.getDefaultProgressData();
        }
        
        const saved = localStorage.getItem('learningProgress');
        if (saved) {
            return JSON.parse(saved);
        }
        return this.getDefaultProgressData();
    }

    getDefaultProgressData() {
        return {
            totalProgress: 0,
            completedSections: [],
            sectionProgress: {},
            totalTime: 0,
            lastStudied: null,
            sessions: []
        };
    }

    saveProgressData() {
        if (window.userManager && window.userManager.currentUser) {
            window.userManager.updateProgress(this.progressData);
        } else {
            localStorage.setItem('learningProgress', JSON.stringify(this.progressData));
        }
    }

    setupEventListeners() {
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('section-title') || 
                e.target.closest('.section-title')) {
                this.trackSectionView(e.target);
            }
        });

        window.addEventListener('beforeunload', () => {
            this.endSessionTracking();
        });
        
        window.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                this.saveCurrentSession();
            }
        });
    }

    startSessionTracking() {
        this.currentSessionStartTime = Date.now();
    }

    saveCurrentSession() {
        if (this.currentSessionStartTime) {
            const sessionDuration = Math.floor((Date.now() - this.currentSessionStartTime) / 1000 / 60);
            if (sessionDuration > 0) {
                this.progressData.totalTime += sessionDuration;
                this.progressData.lastStudied = new Date().toISOString();
                this.saveProgressData();
                this.updateProgressDisplay();
                // 重置会话开始时间，避免重复计算
                this.currentSessionStartTime = Date.now();
            }
        }
    }

    endSessionTracking() {
        this.saveCurrentSession();
        if (this.saveInterval) {
            clearInterval(this.saveInterval);
        }
    }

    trackSectionView(element) {
        const sectionId = element.id || element.closest('[id]')?.id;
        if (!sectionId) return;

        this.currentSection = sectionId;
        
        if (!this.progressData.sectionProgress[sectionId]) {
            this.progressData.sectionProgress[sectionId] = {
                viewCount: 0,
                totalTime: 0,
                completed: false,
                lastViewed: null
            };
        }

        this.progressData.sectionProgress[sectionId].viewCount++;
        this.progressData.sectionProgress[sectionId].lastViewed = new Date().toISOString();
        this.saveProgressData();
    }

    markSectionCompleted(sectionId) {
        if (!this.progressData.completedSections.includes(sectionId)) {
            this.progressData.completedSections.push(sectionId);
        }
        
        if (this.progressData.sectionProgress[sectionId]) {
            this.progressData.sectionProgress[sectionId].completed = true;
        }

        this.calculateTotalProgress();
        this.saveProgressData();
        this.updateProgressDisplay();
    }

    markSectionIncomplete(sectionId) {
        const index = this.progressData.completedSections.indexOf(sectionId);
        if (index > -1) {
            this.progressData.completedSections.splice(index, 1);
        }
        
        if (this.progressData.sectionProgress[sectionId]) {
            this.progressData.sectionProgress[sectionId].completed = false;
        }

        this.calculateTotalProgress();
        this.saveProgressData();
        this.updateProgressDisplay();
    }

    calculateTotalProgress() {
        const totalSections = this.getTotalSectionsCount();
        const completedCount = this.progressData.completedSections.length;
        this.progressData.totalProgress = totalSections > 0 
            ? Math.round((completedCount / totalSections) * 100) 
            : 0;
    }

    getTotalSectionsCount() {
        const sections = document.querySelectorAll('.section');
        return sections.length;
    }

    updateProgressDisplay() {
        this.updateProgressCircle();
        this.updateProgressStats();
        this.updateSectionProgressList();
    }

    updateProgressCircle() {
        const circle = document.getElementById('total-progress-circle');
        const text = document.getElementById('total-progress-text');
        
        if (circle && text) {
            const percentage = this.progressData.totalProgress;
            text.textContent = percentage + '%';
            
            circle.style.background = `conic-gradient(#4CAF50 ${percentage}%, #e0e0e0 ${percentage}%)`;
        }
    }

    updateProgressStats() {
        const completedSectionsEl = document.getElementById('completed-sections');
        const totalTimeEl = document.getElementById('total-time');
        const lastStudiedEl = document.getElementById('last-studied');

        if (completedSectionsEl) {
            completedSectionsEl.textContent = this.progressData.completedSections.length;
        }

        if (totalTimeEl) {
            const hours = Math.floor(this.progressData.totalTime / 60);
            const minutes = this.progressData.totalTime % 60;
            totalTimeEl.textContent = hours > 0 
                ? `${hours}小时${minutes}分钟` 
                : `${minutes}分钟`;
        }

        if (lastStudiedEl) {
            if (this.progressData.lastStudied) {
                const lastStudied = new Date(this.progressData.lastStudied);
                const now = new Date();
                const diffDays = Math.floor((now - lastStudied) / (1000 * 60 * 60 * 24));
                
                if (diffDays === 0) {
                    lastStudiedEl.textContent = '今天';
                } else if (diffDays === 1) {
                    lastStudiedEl.textContent = '昨天';
                } else if (diffDays < 7) {
                    lastStudiedEl.textContent = `${diffDays}天前`;
                } else {
                    lastStudiedEl.textContent = lastStudied.toLocaleDateString('zh-CN');
                }
            } else {
                lastStudiedEl.textContent = '-';
            }
        }
    }

    updateSectionProgressList() {
        const container = document.getElementById('section-progress-list');
        if (!container) return;

        const sections = document.querySelectorAll('.section');
        let html = '';

        sections.forEach((section, index) => {
            const sectionId = section.id || `section-${index}`;
            const sectionTitle = section.querySelector('h3, h4, h5')?.textContent || `章节 ${index + 1}`;
            const isCompleted = this.progressData.completedSections.includes(sectionId);
            const progress = this.progressData.sectionProgress[sectionId];

            html += `
                <div class="section-progress-item">
                    <div class="section-info">
                        <input type="checkbox" 
                               class="section-checkbox" 
                               data-section-id="${sectionId}"
                               ${isCompleted ? 'checked' : ''}
                               onchange="progressTracker.toggleSectionCompletion('${sectionId}')">
                        <span class="section-title-text">${sectionTitle}</span>
                    </div>
                    <div class="section-status">
                        ${isCompleted 
                            ? '<span class="status-badge completed">已完成</span>' 
                            : '<span class="status-badge pending">未完成</span>'}
                        ${progress && progress.viewCount > 0 
                            ? `<span class="view-count">浏览${progress.viewCount}次</span>` 
                            : ''}
                    </div>
                </div>
            `;
        });

        container.innerHTML = html;
    }

    toggleSectionCompletion(sectionId) {
        if (this.progressData.completedSections.includes(sectionId)) {
            this.markSectionIncomplete(sectionId);
        } else {
            this.markSectionCompleted(sectionId);
        }
    }

    resetProgress() {
        if (confirm('确定要重置所有学习进度吗？此操作不可撤销。')) {
            this.progressData = this.getDefaultProgressData();
            this.saveProgressData();
            this.updateProgressDisplay();
        }
    }

    exportProgress() {
        const dataStr = JSON.stringify(this.progressData, null, 2);
        const dataBlob = new Blob([dataStr], {type: 'application/json'});
        const url = URL.createObjectURL(dataBlob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `learning-progress-${new Date().toISOString().split('T')[0]}.json`;
        link.click();
        URL.revokeObjectURL(url);
    }

    importProgress(file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const importedData = JSON.parse(e.target.result);
                if (this.validateProgressData(importedData)) {
                    this.progressData = importedData;
                    this.saveProgressData();
                    this.updateProgressDisplay();
                    alert('学习进度导入成功！');
                } else {
                    alert('导入失败：文件格式不正确');
                }
            } catch (error) {
                alert('导入失败：无法解析文件');
            }
        };
        reader.readAsText(file);
    }

    validateProgressData(data) {
        return data && 
               typeof data.totalProgress === 'number' &&
               Array.isArray(data.completedSections) &&
               typeof data.sectionProgress === 'object' &&
               typeof data.totalTime === 'number';
    }
}

// 初始化进度跟踪器
let progressTracker;

document.addEventListener('DOMContentLoaded', function() {
    // 延迟初始化，确保用户管理器已经加载
    setTimeout(() => {
        progressTracker = new LearningProgressTracker();
        
        // 将进度跟踪器暴露到全局作用域，以便HTML中的onchange可以访问
        window.progressTracker = progressTracker;
    }, 100);
});