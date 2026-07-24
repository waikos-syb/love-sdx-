import streamlit as st
import time

# 设置页面
st.set_page_config(page_title="在线聊天室", layout="wide")
st.title("🌐 双向在线聊天室")

# 初始化聊天记录（存在会话缓存）
if "message_list" not in st.session_state:
    st.session_state.message_list = []

# 侧边栏输入昵称
nickname = st.sidebar.text_input("输入你的昵称", value="访客")

# 发送消息区域
msg_input = st.chat_input("输入消息，按下回车发送")
if msg_input and nickname.strip()!="":
    new_msg = {
        "name": nickname,
        "text": msg_input,
        "time": time.strftime("%H:%M:%S")
    }
    st.session_state.message_list.append(new_msg)

st.divider()
st.subheader("📜 聊天记录")

# 渲染所有聊天消息
for msg in st.session_state.message_list:
    st.markdown(f"**[{msg['time']}] {msg['name']}：** {msg['text']}")

# 提示限制
st.info("⚠️免费版限制：服务器重启后记录清空；其他人需要手动刷新页面看到新消息")
