import streamlit as st
from datetime import datetime, timedelta
import time

# 🛏️ 기본 설정
SLEEP_CYCLE_MINUTES = 90
FALL_ASLEEP_TIME = 15

# 🌙 페이지 설정
st.set_page_config(page_title="SleepWhen 🛌🌙", page_icon="😴", layout="centered")

# 🌌 스타일: 짙은 남색 배경
st.markdown("""
    <style>
        body {
            background-color: #0d1b2a;
            color: white;
        }
        .stApp {
            background-color: #0d1b2a;
            color: white;
        }
        .title {
            color: #f0f0f0;
            text-align: center;
        }
        .stSelectbox > div {
            background-color: #1b263b;
            color: white;
        }
        .stButton > button {
            background-color: #415a77;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# 🎉 타이틀
st.markdown("<h1 class='title'>🌙 SleepWhen 🛌✨</h1>", unsafe_allow_html=True)
st.markdown("람수면 주기를 고려한 **최적의 수면/기상 시간**을 알려드릴게요! 😴💤")

# 🕰️ 시간 리스트 생성 함수 (오전/오후 포함)
def generate_ampm_times():
    times = []
    dt = datetime.strptime("00:00", "%H:%M")
    for i in range(48):
        t = dt + timedelta(minutes=30*i)
        hour = t.hour
        minute = t.minute
        ampm = "오전" if hour < 12 else "오후"
        display_hour = hour if 1 <= hour <= 12 else (hour - 12 if hour > 12 else 12)
        times.append(f"{ampm} {display_hour:02d}:{minute:02d}")
    return times

# 문자열을 datetime 객체로 변환
def parse_ampm_time(ampm_str):
    ampm, hm = ampm_str.split()
    hour, minute = map(int, hm.split(":"))
    if ampm == "오후" and hour != 12:
        hour += 12
    elif ampm == "오전" and hour == 12:
        hour = 0
    return datetime.strptime(f"{hour:02d}:{minute:02d}", "%H:%M")

# 시간 옵션
time_options = generate_ampm_times()

# 🔹 컬럼 1: 기상 시간 → 수면 시간
st.subheader("⏰ 기상 시간을 입력하면, 추천 수면 시간이 나와요!")
wake_time_str = st.selectbox("기상 시간 선택 (30분 단위)", time_options, index=16, key="wake_time")

if st.button("잠들기 좋은 시간 보기 🌙"):
    with st.spinner("계산 중... 😪"):
        time.sleep(1)
    wake_dt = parse_ampm_time(wake_time_str)
    recommended_sleep_times = [
        wake_dt - timedelta(minutes=90*i + FALL_ASLEEP_TIME) for i in range(6, 0, -1)
    ]
    st.success("🛏️ 잠드는 데 가장 좋은 시간:")
    for t in recommended_sleep_times:
        ampm = "오전" if t.hour < 12 else "오후"
        display_hour = t.strftime("%I:%M")
        st.markdown(f"🌟 **{ampm} {display_hour}**")

# 🔹 컬럼 2: 수면 시간 → 기상 시간
st.markdown("---")
st.subheader("🛌 잠드는 시간을 입력하면, 추천 기상 시간이 나와요!")
sleep_time_str = st.selectbox("잠드는 시간 선택 (30분 단위)", time_options, index=32, key="sleep_time")

if st.button("일어나기 좋은 시간 보기 ⏰"):
    with st.spinner("계산 중... 😴"):
        time.sleep(1)
    sleep_dt = parse_ampm_time(sleep_time_str) + timedelta(minutes=FALL_ASLEEP_TIME)
    recommended_wake_times = [
        sleep_dt + timedelta(minutes=90*i) for i in range(1, 7)
    ]
    st.success("🌞 일어나기 좋은 시간:")
    for t in recommended_wake_times:
        ampm = "오전" if t.hour < 12 else "오후"
        display_hour = t.strftime("%I:%M")
        st.markdown(f"✨ **{ampm} {display_hour}**")

# ℹ️ 수면 주기 설명
with st.expander("📘 수면 주기란?"):
    st.markdown("""
    🧠 사람은 평균적으로 **90분 주기로 수면 단계**를 바꿔요.  
    **REM 수면 상태에서 일어날 때** 가장 개운하다고 알려져 있어요!  
    SleepWhen은 이 점을 고려해 추천해드립니다. 🌙
    """)

# 푸터
st.markdown("---")
st.markdown("Made with 💤 by SleepWhen Team | Powered by Streamlit 🚀", unsafe_allow_html=True)
