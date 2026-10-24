import os
#指定快递员，把指定网址html下载回来
import requests
#网页清洗，把标签脱除，留下纯文字
from bs4 import BeautifulSoup
from dotenv import load_dotenv
#从smolagents里面请出全能实习生codeagent，万能翻译官链接openai
from smolagents import CodeAgent, OpenAIServerModel, tool

# 1. 加载 Key
load_dotenv()

# 2. 配置 DeepSeek 大脑
model = OpenAIServerModel(
    model_id="deepseek-chat",
    api_base="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)


# 3. 自己写一个“网页抓取”工具
#此标签是 把函数打包成tool
@tool
def fetch_webpage_text(url: str) -> str:
    #工具说明书，llm看这个说明
    """
    抓取指定网址的网页纯文本。

    Args:
        url: 要抓取的网页完整网址，必须以 http 或 https 开头
    """
    try:
        # 假装自己是一个正常的浏览器
        #伪装成谷歌浏览器Mozilla
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 如果网页报错就抛出异常

        # 用 BeautifulSoup 解析网页，去掉乱七八糟的标签，只留文字
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

        # 为了防止网页太长撑爆大模型的肚子，我们只取前 4000 个字符
        return text[:4000]
    except Exception as e:
        return f"抓取网页失败，错误信息：{e}"


# 4. 召唤 Code Agent，把网页工具塞给它
agent = CodeAgent(tools=[fetch_webpage_text], model=model)

# 5. 下达任务（你可以把网址换成你喜欢的任何文章、新闻、博客）
target_url = "https://www.buaa.edu.cn/"
print(f"==== Agent 开始抓取并总结：{target_url} ====")

task = f"""
请使用 fetch_webpage_text 工具抓取这个网址的内容：{target_url}
抓取成功后，请阅读里面的文字，并用 3 句话总结这个网站的核心业务是什么。
"""

result = agent.run(task)

print("\n==== 最终总结 ====\n", result)