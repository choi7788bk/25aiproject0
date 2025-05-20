import streamlit as st
import time

# 🎨 스타일 설정
st.set_page_config(page_title="MBTI 궁합 테스트 💕", page_icon="💖", layout="centered")

# 🎉 타이틀
st.title("✨ MBTI 궁합 테스트 💕")
st.markdown("당신의 MBTI를 입력하면, 잘 어울리는 궁합 MBTI를 알려드릴게요! 😘")

# 🎁 MBTI 궁합 데이터
mbti_matches = {
    "INTJ": "ENFP 😄",
    "INTP": "ENTJ 🧠",
    "ENTJ": "INFP 💫",
    "ENTP": "INFJ 🎨",
    "INFJ": "ENFP 💕",
    "INFP": "ENFJ 🌟",
    "ENFJ": "INFP 💖",
    "ENFP": "INFJ 🌈",
    "ISTJ": "ESFP 🎉",
    "ISFJ": "ESTP 🕺",
    "ESTJ": "ISFP 🌿",
    "ESFJ": "ISFP 🌸",
    "ISTP": "ESFJ 🍀",
    "ISFP": "ESTJ 📋",
    "ESTP": "ISFJ 🎀",
    "ESFP": "ISTJ 📚",
}

# 📝 MBTI 입력 받기
user_mbti = st.selectbox(
    "당신의 MBTI를 선택하세요! 🔍", 
    list(mbti_matches.keys()), 
    index=0
)

# 🚀 결과 버튼
if st.button("궁합 MBTI 보기 💘"):
    with st.spinner("궁합 계산 중...🧮"):
        time.sleep(2)
    match = mbti_matches.get(user_mbti, "모두와 잘 어울려요! 🌍")
    st.balloons()
    st.success(f"당신과 찰떡궁합인 MBTI는... 🥁 **{match}** 입니다! 🎊")
    st.markdown("💡 이 조합은 서로의 부족한 면을 채워주며, 깊은 관계를 형성할 수 있어요!")

# 🧠 부가 설명 (선택 사항)
with st.expander("📚 MBTI 궁합이란?"):
    st.markdown("""
    MBTI 궁합은 성격 유형 간의 상호작용과 소통 스타일을 기반으로 조화를 이룰 수 있는 조합을 말해요.  
    물론, 사람마다 다르기 때문에 참고용으로만 봐주세요 😉  
    """)

# 🎨 푸터
st.markdown("---")
st.markdown("Made with ❤️ by [Your Name]")
