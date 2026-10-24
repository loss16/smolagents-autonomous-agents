import os
from dotenv import load_dotenv
#从smolagents工具箱请出一个代码智能体和全能翻译官
from smolagents import CodeAgent, OpenAIServerModel

#CodeAgent将任务发给DeepSeek，DeepSeek生成代码返回。
# CodeAgent在本地执行，遇错则反馈给DeepSeek重写，成功则输出结果。
# 1. 加载你的 Key
load_dotenv()

# 2. 配置 DeepSeek 大脑
model = OpenAIServerModel(
    model_id="deepseek-chat",
    api_base="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 3. 召唤 Code Agent
# 注意：这里 tools=[] 是空的！因为我们不给它现成工具，让它自己写代码。
agent = CodeAgent(tools=[], model=model)

# 4. 给它下达一个任务
print("==== Agent 开始思考并编写代码 ====")
result = agent.run("""请完成以下任务：
1. 用 Python 生成一个包含 10 个随机数的列表（范围在1-100之间），并用代码打印出来。
2. 用 Python 计算这些数字的平均值、最大值和最小值。
3. 用 Python 把这些数字从小到大排序。
请输出最终的统计结果和排序后的列表。""")

print("\n==== 最终结果 ====")
print(result)