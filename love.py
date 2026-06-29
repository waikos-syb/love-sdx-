import streamlit as st
import random
from datetime import date, datetime
import time

# 页面基础配置 - 增加页面加载动画设置
st.set_page_config(
    page_title="专属情侣小屋",
    page_icon="❤️",
    layout="centered"
)

# 自定义CSS - 提升视觉质感和交互体验
st.markdown("""
<style>
    .main-title {
        background: linear-gradient(45deg, #ff6b8b, #ff4d6d);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff4d6d, #ff6b8b);
        color: white;
        border-radius: 50px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 77, 109, 0.3);
    }
    .card {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .love-quote {
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .days-counter {
        font-size: 1.2em;
        font-weight: bold;
        color: #ff4d6d;
    }
</style>
""", unsafe_allow_html=True)

# 页面标题 - 增加渐变效果
st.markdown("""
    <h1 class='main-title'>💞 我们的专属浪漫小屋 💞</h1>
""", unsafe_allow_html=True)
st.divider()

# ========== 1、情侣信息录入交互 ==========
with st.container():
    st.subheader("📝 填写情侣信息")
    # 使用列布局让输入框更紧凑
    col1, col2 = st.columns(2)
    with col1:
        boy_name = st.text_input("男生昵称：", placeholder="输入他的名字")
    with col2:
        girl_name = st.text_input("女生昵称：", placeholder="输入她的名字")

    start_day = st.date_input("相恋纪念日：", value=date(2024, 1, 1))

    # 计算相恋时间（精确到天和小时）
    today = datetime.now()
    start_datetime = datetime.combine(start_day, datetime.min.time())
    love_duration = today - start_datetime
    love_days = love_duration.days
    love_hours = love_duration.seconds // 3600

    if boy_name and girl_name:
        st.success(f"💌 {boy_name} & {girl_name} 已经相恋 {love_days} 天 {love_hours} 小时啦！")

st.divider()

# ========== 2、随机情话生成器（优化交互） ==========
with st.container():
    st.subheader("💬 一键生成专属情话")
    love_words = [
        f"遇见你之后，{boy_name if boy_name else '我的世界'}万物都开始变得温柔",
        f"{girl_name if girl_name else '你的'}愿望很小，余生全是{boy_name if boy_name else '我'}",
        f"世界万般美好，都不及{girl_name if girl_name else '你'}眉眼带笑",
        f"攒了好久的温柔与浪漫，全部都给{boy_name if boy_name else '你'}",
        f"不用奔赴大海，{boy_name if boy_name else '我'}身边就是{girl_name if girl_name else '你'}的归宿",
        f"岁岁年年，朝朝暮暮，只想和{girl_name if girl_name else '你'}一起度过"
    ]

    # 增加加载动画效果
    if st.button("点击抽取专属情话❤️", type="primary"):
        with st.spinner("正在收集心动信号..."):
            time.sleep(0.8)  # 短暂延迟增加期待感
            pick = random.choice(love_words)
            st.markdown(
                f"<h3 class='love-quote' style='color:#ff3366;text-align:center'>{pick}</h3>",
                unsafe_allow_html=True
            )

st.divider()

# ========== 3、爱意打分滑动交互（优化反馈） ==========
with st.container():
    st.subheader("💕 爱意值打分")
    love_score = st.slider(
        "拖动滑块，给出对对方的爱意值",
        min_value=0,
        max_value=100,
        value=99,
        format="%d分"
    )

    # 更丰富的反馈内容和视觉效果
    if love_score >= 90:
        st.balloons()
        st.info(f"💘 满分挚爱！爱意值：{love_score}分，此生不渝，一眼万年！")
    elif love_score >= 80:
        st.snow()  # 爱心特效
        st.info(f"💖 浓情蜜意！爱意值：{love_score}分，点点滴滴都是爱！")
    elif love_score >= 60:
        st.info(f"💓 甜蜜热恋！爱意值：{love_score}分，好好相守，共赴未来~")
    else:
        st.warning(f"💔 要多多陪伴对方哦，当前爱意{love_score}分，需要加把劲啦！")

st.divider()

# ========== 4、纪念日倒计时（优化逻辑） ==========
with st.container():
    # 计算下一个纪念日（如果今年的已经过了，就计算明年的）
    today_date = date.today()
    this_year_anniversary = start_day.replace(year=today_date.year)

    if this_year_anniversary < today_date:
        try:
            next_anniversary = start_day.replace(year=today_date.year + 1)
        except ValueError:
            # 处理闰年2月29日的特殊情况
            next_anniversary = date(today_date.year + 1, 2, 28)
    else:
        next_anniversary = this_year_anniversary

    count_day = (next_anniversary - today_date).days
    st.metric(
        label="距离下一个周年纪念日剩余天数",
        value=f"{count_day}天",
        delta=f"{next_anniversary.strftime('%Y年%m月%d日')} 就是你们的纪念日啦~"
    )

# 底部落款 - 增加动态效果
st.markdown("""
<p style="text-align:center;color:#ff6b8b;animation: fadeIn 2s ease-in-out;">
    以爱之名，共度余生❤️
</p>
""", unsafe_allow_html=True)