---
name: "ai-agent"
description: "AI Agent装技能和自动化工具。Invoke when user asks for AI agent setup, automation tools, or agent orchestration."
---

# AI Agent Skill

This skill provides AI Agent装技能和自动化工具，帮助用户设置和管理AI智能体。

## When to Invoke

- User asks for "AI agent setup"
- User requests "agent orchestration"
- User wants to "create AI agents"
- User mentions "multi-agent system"
- User needs "agent workflow automation"

## Description

This skill helps with:
- AI Agent装技能配置
- 智能体创建和管理
- 自动化工作流设置
- 多智能体协调
- Agent间通信

### 核心功能

#### 1. Agent配置
- 定义Agent的能力和限制
- 设置Agent的输入输出
- 配置Agent的执行环境
- 管理Agent的生命周期

#### 2. 工作流自动化
- 创建Agent工作流
- 定义Agent间的协作
- 设置触发条件和执行规则
- 管理Agent的状态和错误处理

#### 3. 多智能体系统
- 创建多个专门的Agent
- 定义Agent间的通信协议
- 实现Agent间的任务分配
- 管理Agent的负载均衡

#### 4. 集成和扩展
- 与外部API集成
- 支持自定义工具
- 实现插件系统
- 支持Agent的动态加载

## Usage Examples

### Example 1: 创建简单的AI Agent
```python
class SimpleAgent:
    """
    简单的AI Agent类
    """
    
    def __init__(self, name, capabilities):
        self.name = name
        self.capabilities = capabilities
        self.state = "idle"
        self.memory = {}
    
    def process(self, input_data):
        """
        处理输入数据
        """
        if self.state == "idle":
            self.state = "processing"
            result = self.execute_task(input_data)
            self.state = "idle"
            return result
        else:
            return {"status": "busy", "message": "Agent正在处理其他任务"}
    
    def execute_task(self, task):
        """
        执行任务
        """
        for capability in self.capabilities:
            if capability in task:
                return self.capabilities[capability](task)
        
        return {"status": "error", "message": "无法处理该任务"}

# 创建Agent实例
code_agent = SimpleAgent(
    name="代码助手",
    capabilities={
        "code_generation": lambda task: f"def {task['function_name']}():\n    pass",
        "code_explanation": lambda task: f"这个函数用于{task['description']}",
        "code_optimization": lambda task: "# 优化后的代码"
    }
)

# 使用Agent
result = code_agent.process({
    "type": "code_generation",
    "function_name": "calculate_sum",
    "description": "计算列表中所有数字的总和"
})

print(result)
```

### Example 2: 多智能体系统
```python
class MultiAgentSystem:
    """
    多智能体系统
    """
    
    def __init__(self):
        self.agents = {}
        self.task_queue = []
        self.results = {}
    
    def register_agent(self, agent_id, agent):
        """
        注册智能体
        """
        self.agents[agent_id] = agent
        print(f"Agent {agent_id} 已注册")
    
    def assign_task(self, task):
        """
        分配任务
        """
        for agent_id, agent in self.agents.items():
            if agent.can_handle(task):
                result = agent.process(task)
                self.results[task['id']] = result
                print(f"任务 {task['id']} 已分配给 Agent {agent_id}")
                return True
        
        print(f"没有Agent可以处理任务 {task['id']}")
        return False
    
    def get_results(self, task_id):
        """
        获取任务结果
        """
        return self.results.get(task_id, {"status": "pending"})

# 创建多智能体系统
system = MultiAgentSystem()

# 注册多个Agent
system.register_agent("researcher", ResearchAgent())
system.register_agent("coder", CodeAgent())
system.register_agent("tester", TestAgent())

# 分配任务
task = {
    "id": "task_001",
    "type": "research",
    "description": "研究最新的AI技术趋势"
}

if system.assign_task(task):
    result = system.get_results("task_001")
    print(f"任务结果: {result}")
```

### Example 3: 工作流自动化
```python
class AgentWorkflow:
    """
    Agent工作流自动化
    """
    
    def __init__(self):
        self.steps = []
        self.current_step = 0
    
    def add_step(self, step):
        """
        添加工作流步骤
        """
        self.steps.append(step)
        print(f"添加步骤: {step['name']}")
    
    def execute_workflow(self, input_data):
        """
        执行工作流
        """
        results = []
        for step in self.steps:
            print(f"执行步骤 {self.current_step + 1}: {step['name']}")
            result = step['execute'](input_data)
            results.append(result)
            input_data = result.get('output', input_data)
            self.current_step += 1
        
        return {"status": "completed", "results": results}

# 创建工作流
workflow = AgentWorkflow()

# 添加步骤
workflow.add_step({
    "name": "数据收集",
    "execute": lambda data: {"status": "success", "output": {"data": "collected_data"}}
})

workflow.add_step({
    "name": "数据分析",
    "execute": lambda data: {"status": "success", "output": {"analysis": "data_analyzed"}}
})

workflow.add_step({
    "name": "生成报告",
    "execute": lambda data: {"status": "success", "output": {"report": "generated"}}
})

# 执行工作流
result = workflow.execute_workflow({"input": "initial_data"})
print(f"工作流执行结果: {result}")
```

## Best Practices

### 1. Agent设计原则
- 单一职责：每个Agent只负责一个特定领域
- 可扩展性：设计Agent使其易于添加新功能
- 可测试性：每个Agent都应该可以独立测试
- 错误处理：Agent应该能够优雅地处理错误
- 状态管理：Agent应该跟踪自己的状态

### 2. 工作流设计
- 模块化：将复杂工作流分解为简单步骤
- 可重用性：设计可重用的工作流组件
- 可监控性：跟踪工作流的执行进度
- 错误恢复：工作流应该能够从错误中恢复

### 3. 多智能体系统
- 负载均衡：合理分配任务给可用的Agent
- 通信协议：定义清晰的Agent间通信协议
- 容错性：系统应该能够处理Agent失败
- 可扩展性：系统应该支持动态添加新Agent

### 4. 性能优化
- 异步执行：使用异步执行提高性能
- 资源管理：合理管理系统资源
- 缓存：缓存常用结果
- 并行处理：并行执行独立任务

## Troubleshooting

### 常见问题

1. **Agent不响应**
   - 检查Agent是否正确注册
   - 验证Agent的状态
   - 检查Agent的输入输出配置

2. **工作流卡住**
   - 检查每个步骤的执行时间
   - 设置合理的超时
   - 实现步骤跳过机制

3. **任务分配失败**
   - 检查Agent的能力匹配
   - 验证任务格式
   - 检查Agent的可用性

4. **多智能体冲突**
   - 实现Agent间的协调机制
   - 设置优先级规则
   - 实现任务队列管理

## Advanced Features

### 1. 动态Agent加载
- 支持运行时添加新Agent
- 动态配置Agent能力
- 热重载Agent配置

### 2. Agent学习
- 从执行历史中学习
- 自动优化Agent行为
- 适应新的任务类型
- 持续改进性能

### 3. 可视化监控
- 实时监控Agent状态
- 可视化工作流执行
- 性能指标监控
- 错误日志和报警

## Conclusion

AI Agent技能是2026年最火的技术趋势之一。这个skill提供了创建、管理和优化AI Agent的完整框架，帮助用户构建强大的多智能体系统。