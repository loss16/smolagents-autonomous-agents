# 多能力自主智能体套件 (Multi-Capability Agent Suite)

本项目基于 HuggingFace 开源轻量级框架 `smolagents` 构建，接入了 DeepSeek 大模型，探索并验证了 Code Agent（代码智能体）在不同业务场景下的落地能力。

## 📂 包含的 Agent 模块：

### 1. `run_code_agent.py` - 复杂计算任务 Agent
- **能力**：在无预定义工具（`tools=[]`）的情况下，根据自然语言指令，实时编写多行 Python 代码并执行。
- **场景**：完成包含多维随机数组生成、平均值/极值计算、数据排序等复合型的数据处理任务。

### 2. `web_summary_agent.py` - 网页解析与总结 Agent
- **能力**：通过自定义的 `@tool` 工具抓取指定网页内容（内置 User-Agent 伪装与 BeautifulSoup 标签清洗），并自动提炼生成 3 句话总结。
- **高光时刻（Self-Correction）**：在抓取过程中遇到目标网页编码错误（乱码）时，Agent 能够触发自我纠错机制，自主生成 Python 代码（`latin-1 -> utf-8`）修复数据，并最终完成摘要，展现了极强的鲁棒性。

## 🛠️ 技术栈
- **核心框架**：smolagents
- **大语言模型**：DeepSeek API (通过 `OpenAIServerModel` 适配)
- **网络请求与解析**：requests, BeautifulSoup4
- **运行环境**：Python 3.11, PyCharm, Virtualenv

## 🚀 如何运行
1. 安装依赖：
   ```bash
   pip install smolagents openai python-dotenv requests beautifulsoup4