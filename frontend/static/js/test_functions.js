// 前后端功能测试脚本

const API_BASE_URL = 'http://127.0.0.1:5000/api';

async function testAPI() {
    console.log('=== 开始API功能测试 ===\n');
    
    const tests = [
        {
            name: '健康检查',
            url: `${API_BASE_URL}/health`,
            method: 'GET',
            expectedStatus: 200
        },
        {
            name: '用户注册',
            url: `${API_BASE_URL}/users`,
            method: 'POST',
            body: {
                action: 'register',
                username: 'testuser',
                email: 'test@example.com',
                password: 'test123456',
                confirmPassword: 'test123456'
            },
            expectedStatus: 200
        },
        {
            name: '用户登录',
            url: `${API_BASE_URL}/users`,
            method: 'POST',
            body: {
                action: 'login',
                usernameOrEmail: 'test@example.com',
                password: 'test123456'
            },
            expectedStatus: 200
        },
        {
            name: '获取用户进度',
            url: `${API_BASE_URL}/progress?userId=test_user_id`,
            method: 'GET',
            expectedStatus: 200
        }
    ];
    
    let passedTests = 0;
    let failedTests = 0;
    
    for (const test of tests) {
        console.log(`\n测试: ${test.name}`);
        console.log(`URL: ${test.url}`);
        console.log(`方法: ${test.method}`);
        
        try {
            const options = {
                method: test.method,
                headers: {
                    'Content-Type': 'application/json'
                }
            };
            
            if (test.body) {
                options.body = JSON.stringify(test.body);
            }
            
            const response = await fetch(test.url, options);
            const data = await response.json();
            
            if (response.status === test.expectedStatus) {
                console.log(`✅ 通过 - 状态码: ${response.status}`);
                if (data.success) {
                    console.log(`   响应: ${JSON.stringify(data, null, 2)}`);
                }
                passedTests++;
            } else {
                console.log(`❌ 失败 - 期望状态码: ${test.expectedStatus}, 实际: ${response.status}`);
                failedTests++;
            }
        } catch (error) {
            console.log(`❌ 失败 - 错误: ${error.message}`);
            failedTests++;
        }
    }
    
    console.log(`\n=== 测试结果 ===`);
    console.log(`总测试数: ${tests.length}`);
    console.log(`通过: ${passedTests}`);
    console.log(`失败: ${failedTests}`);
    console.log(`成功率: ${((passedTests / tests.length) * 100).toFixed(1)}%`);
    
    if (failedTests === 0) {
        console.log('\n🎉 所有测试通过！');
    } else {
        console.log('\n⚠️  部分测试失败，请检查后端服务');
    }
}

// 测试前端文件加载
function testFrontendFiles() {
    console.log('\n=== 前端文件加载测试 ===\n');
    
    const files = [
        { name: '配置文件', path: '../static/js/config.js' },
        { name: '样式文件', path: '../static/css/styles.css' },
        { name: '主脚本', path: '../static/js/script.js' },
        { name: '进度跟踪', path: '../static/js/progress_tracker.js' },
        { name: '用户管理', path: '../static/js/user_manager.js' }
    ];
    
    let loadedFiles = 0;
    let failedFiles = 0;
    
    for (const file of files) {
        console.log(`检查: ${file.name}`);
        try {
            const script = document.createElement('script');
            script.src = file.path;
            script.onload = () => {
                console.log(`✅ ${file.name} 加载成功`);
                loadedFiles++;
            };
            script.onerror = () => {
                console.log(`❌ ${file.name} 加载失败`);
                failedFiles++;
            };
            document.head.appendChild(script);
            
            setTimeout(() => {
                document.head.removeChild(script);
            }, 100);
        } catch (error) {
            console.log(`❌ ${file.name} 检查失败: ${error.message}`);
            failedFiles++;
        }
    }
    
    setTimeout(() => {
        console.log(`\n=== 前端文件测试结果 ===`);
        console.log(`总文件数: ${files.length}`);
        console.log(`加载成功: ${loadedFiles}`);
        console.log(`加载失败: ${failedFiles}`);
    }, 2000);
}

// 测试本地存储功能
function testLocalStorage() {
    console.log('\n=== 本地存储功能测试 ===\n');
    
    const testData = {
        key: 'test_key',
        value: 'test_value'
    };
    
    try {
        localStorage.setItem(testData.key, testData.value);
        console.log(`✅ 写入本地存储: ${testData.key} = ${testData.value}`);
        
        const retrieved = localStorage.getItem(testData.key);
        if (retrieved === testData.value) {
            console.log(`✅ 读取本地存储: ${testData.key} = ${retrieved}`);
        } else {
            console.log(`❌ 读取本地存储失败: 期望 ${testData.value}, 实际 ${retrieved}`);
        }
        
        localStorage.removeItem(testData.key);
        console.log(`✅ 删除本地存储: ${testData.key}`);
        
        const afterRemove = localStorage.getItem(testData.key);
        if (afterRemove === null) {
            console.log(`✅ 验证删除成功: ${testData.key} 不存在`);
        } else {
            console.log(`❌ 删除验证失败: ${testData.key} 仍然存在`);
        }
        
        console.log('\n🎉 本地存储功能正常！');
    } catch (error) {
        console.log(`❌ 本地存储测试失败: ${error.message}`);
    }
}

// 测试DOM元素
function testDOMElements() {
    console.log('\n=== DOM元素测试 ===\n');
    
    const elements = [
        { name: '容器', selector: '.container' },
        { name: '头部', selector: 'header' },
        { name: '用户信息区域', selector: '#user-info' },
        { name: '登录按钮', selector: '#login-btn' },
        { name: '注册按钮', selector: '#register-btn' },
        { name: '进度面板', selector: '#progress-panel' },
        { name: '进度圆环', selector: '#total-progress-circle' }
    ];
    
    let foundElements = 0;
    let missingElements = 0;
    
    for (const element of elements) {
        const el = document.querySelector(element.selector);
        if (el) {
            console.log(`✅ 找到元素: ${element.name}`);
            foundElements++;
        } else {
            console.log(`❌ 未找到元素: ${element.name}`);
            missingElements++;
        }
    }
    
    console.log(`\n=== DOM元素测试结果 ===`);
    console.log(`总元素数: ${elements.length}`);
    console.log(`找到: ${foundElements}`);
    console.log(`缺失: ${missingElements}`);
    
    if (missingElements === 0) {
        console.log('\n🎉 所有DOM元素正常！');
    } else {
        console.log('\n⚠️  部分DOM元素缺失');
    }
}

// 运行所有测试
function runAllTests() {
    console.log('🧪 AI课程学习平台 - 功能测试\n');
    console.log('========================================\n');
    
    testLocalStorage();
    testDOMElements();
    testFrontendFiles();
    
    setTimeout(() => {
        testAPI();
    }, 3000);
}

// 页面加载完成后运行测试
if (document.readyState === 'complete') {
    runAllTests();
} else {
    document.addEventListener('DOMContentLoaded', runAllTests);
}