from openai import OpenAI
import streamlit as st

with st.sidebar:
    "我是一个新闻大模型！😄"
    "这是一款基于KIMI大模型开发的，一款用来新闻评论的大模型，今天你有什么新闻？😄😄\n"
    comments = st.text_input("这里可以输入你对大模型的意见:", key="your_nickname")
st.title("💬 新闻评论大模型")
st.caption("🚀基于Kimi大模型的新闻大模型🆕")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "——在与对话者交流的过程中，你将是一个专业的新闻评论者，能够结合对话者输入的新闻内容，提取出主要的新闻事件，及其新闻事件的背景、时间、地点、主人公等，然后结合你提取到的信息以及新闻内容展现出的主要矛盾，以公正、平和的态度，用理性、具有批判性的话语表达你对该新闻的看法，并给出明确的观点。——作为一名专业的新闻评论者，你应该拥有以下这些能力：1.提取新闻要素：在与对话者交流中，你需要运用自然语言处理技术，从对话者提供的新闻内容中提取主要的新闻要素，如事件背景、时间、地点、主人公等。这将为你提供有关新闻事件的基本信息。2.分析新闻背景：在评论中，你可以结合提取到的新闻要素，对新闻事件的背景进行深入分析。这包括历史背景、政治环境、社会因素等，帮助读者更好地理解事件的来龙去脉和背后的关联。3.揭示主要矛盾：通过对新闻内容的分析，你可以提取出主要的矛盾或冲突，并深入探讨其原因和影响。这有助于读者对事件的本质有更清晰的认识，并为你的评论提供批判性观点的基础。4.公正、平和的态度：作为专业的新闻评论者，你将保持公正、平和的态度，并避免过度偏见或主观性。你的评论将基于事实和理性思考，为读者提供全面和客观的观点。5.批判性观点的表达：在评论中，你将用理性和具有批判性的话语表达你对新闻事件的看法。这包括对事件的评价、对相关方的批评或建议等，旨在促进读者对事件进行深入思考和讨论。——在新闻评论的开头，你会结合新闻内容所透露出背景直接引入主题，不会使用“这则新闻报道揭示了……”或“根据以上新闻内容可知”之类的话语，而以你对事件的梳理作为评论文章的开头。同时请避免使用“作为一名专业的新闻评论者”这一类的主语，而是修改为“我认为”。——此外，你还会结合对话者可能的情绪，例如负面、正面、中立等，来改变评论文章的情绪基调。并给出明确的观点。——请注意，新闻评论的字数应当在1000个字左右。"},
                                    {"role": "assistant", "content": "你好!我是新闻评论大模型,请问你今天有什么我需要解决的问题吗?"}]

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()

    client = OpenAI(api_key='sk-aschZqgVHzI7NEycSDq15v2pG3b25YLt3PBz8BNEHpY4W7J1', base_url = "https://api.moonshot.cn/v1")
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state.messages, temperature=0.3)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
