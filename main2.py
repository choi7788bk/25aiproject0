import streamlit as st
from datetime import datetime, timedelta
import time

# 🌃 페이지 설정 (짙은 남색 테마)
st.set_page_config(page_title="SleepWhen 🛌🌙", page_icon="😴", layout="centered")

# 💅 커스텀 스타일 (남색 배경, 화이트 텍스트, 둥근 카드 스타일)
st.markdown("""
    <style>
        body {
            background-color: #0d1b2a;
            color: white;
        }
        .stApp {
            background-color: #0d1b2a;
        }
        .block-container {
            padding-top: 2rem;
        }
        .title {
            color: #f0f0f0;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# 🎉 타이틀
st.markdown("<h1 class='title'>🌙 SleepWhen 🛌✨</h1>", unsafe_allow_html=True)
st.markdown("**램수면 주기(90분)를 기준으로 잠들거나 일어나기 좋은 시간을 추천해드려요!** 😴💤")

# 🕰️ 30분 단위 시간 리스트 생성
def generate_time_options():
    base_time = datetime.strptime("00:00", "%H:%M")
    return [(base_time + timedelta(minutes=30*i)).strftime("%H:%M") for i in range(48)]

time_options = generate_time_options()

# 📌 탭 선택: 수면 기준 / 기상 기준
tab1, tab2 = st.tabs(["🛌 언제 자야 할까?", "⏰ 언제 일어나야 할까?"])

# 💤 수면 기준: 기상 시간 선택 → 취침 시간 추천
with tab1:
    st.subheader("⏰ 기상 시간을 선택하면, 좋은 취침 시간을 추천해드릴게요!")
    wake_time_str = st.selectbox("기상 시간 선택 (30분 단위)", time_options, index=16)

    if st.button("잠드는 시간 추천 받기 🌙"):
        with st.spinner("✨ 수면 주기를 계산 중입니다..."):
            time.sleep(1.5)

        wake_dt = datetime.strptime(wake_time_str, "%H:%M")
        recommended_sleep_times = [wake_dt - timedelta(minutes=90*i + 15) for i in range(6, 0, -1)]

        st.balloons()
        st.success("💤 아래 시간쯤 잠들면 더 상쾌한 아침을 맞이할 수 있어요!")
        for t in recommended_sleep_times:
            st.markdown(f"🌟 **{t.strftime('%H:%M')}**")

# 🌙 취침 기준: 잠드는 시간 선택 → 기상 시간 추천
with tab2:
    st.subheader("🛏️ 잠드는 시간을 선택하면, 좋은 기상 시간을 알려드릴게요!")
    sleep_time_str = st.selectbox("잠드는 시간 선택 (30분 단위)", time_options, index=32)

    if st.button("기상 시간 추천 받기 ⏰"):
        with st.spinner("✨ 수면 주기를 계산 중입니다..."):
            time.sleep(1.5)

        sleep_dt = datetime.strptime(sleep_time_str, "%H:%M") + timedelta(minutes=15)  # 잠드는 데 15분
        recommended_wake_times = [sleep_dt + timedelta(minutes=90*i) for i in range(1, 7)]

        st.snow()
        st.success("🌞 이 시간에 일어나면 개운하게 일어날 수 있어요!")
        for t in recommended_wake_times:
            st.markdown(f"✨ **{t.strftime('%H:%M')}**")

# 📘 수면 정보
with st.expander("📚 수면 주기란?"):
    st.markdown("""
    🧠 사람은 보통 **90분 간격으로 수면 주기**를 경험해요 (Non-REM → REM).  
    **REM 수면 중 깰 경우** 머리가 덜 멍하고 훨씬 상쾌하다는 연구 결과가 있어요!  
    이를 고려해 **잠드는 시간 / 기상 시간**을 추천해드립니다. 🌙
    """)

# 👣 푸터
st.markdown("---")
st.markdown("Made with ❤️ for better sleep | Powered by Streamlit 🚀", unsafe_allow_html=True)
