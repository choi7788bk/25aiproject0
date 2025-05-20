import streamlit as st
import time

# 🌈 페이지 설정
st.set_page_config(page_title="MBTI 궁합 분석 💞", page_icon="🧠", layout="centered")

# 🎉 타이틀
st.title("🔮 MBTI 궁합 분석기 💕")
st.markdown("당신의 MBTI를 입력하면...\n👉 성격 유형 설명\n👉 다른 MBTI와의 궁합 분석\n👉 최고의 궁합 상대를 알려줄게요! 😘")

# 📘 MBTI 성격 설명
mbti_traits = {
    "INTJ": "전략가 🧠 | 분석적이고 독립적인 성격. 미래를 계획하는 걸 좋아해요.",
    "INTP": "논리술사 🧪 | 호기심 많고 독창적인 아이디어 뱅크예요.",
    "ENTJ": "지휘관 📣 | 리더십 강하고 목표 지향적인 성격이에요.",
    "ENTP": "변론가 💬 | 재치 있고 새로운 것에 도전하는 걸 즐겨요.",
    "INFJ": "옹호자 🌌 | 조용하지만 강한 신념과 비전을 가진 타입이에요.",
    "INFP": "중재자 🕊️ | 감성적이고 이상주의적인 마음의 소유자예요.",
    "ENFJ": "선도자 🌟 | 사람들을 이끄는 따뜻한 리더예요.",
    "ENFP": "활동가 🎈 | 열정 넘치고 창의적인 자유 영혼이에요.",
    "ISTJ": "논리주의자 📏 | 책임감 강하고 체계적인 성격이에요.",
    "ISFJ": "수호자 🛡️ | 따뜻하고 세심한 배려왕이에요.",
    "ESTJ": "관리자 🧱 | 현실적이고 조직적인 타입이에요.",
    "ESFJ": "집정관 👑 | 사교적이고 타인을 도우려는 마음이 커요.",
    "ISTP": "장인 🔧 | 실용적이고 조용하지만 문제 해결에 강해요.",
    "ISFP": "예술가 🎨 | 감각적이고 조용한 낭만주의자예요.",
    "ESTP": "사업가 💼 | 모험을 즐기고 에너지가 넘쳐요.",
    "ESFP": "연예인 🎤 | 분위기 메이커! 모두와 잘 어울리는 성격이에요.",
}

# 💘 MBTI 궁합 추천
mbti_compatibility = {
    "INTJ": ("ENFP", ["ENTP", "INFJ", "INFP"]),
    "INTP": ("ENTJ", ["ENFP", "INTJ", "INFJ"]),
    "ENTJ": ("INFP", ["INTP", "ENFP", "ISFP"]),
    "ENTP": ("INFJ", ["INFP", "INTJ", "ENFP"]),
    "INFJ": ("ENFP", ["INFP", "ENTP", "ENFJ"]),
    "INFP": ("ENFJ", ["INFJ", "ENFP", "ENTP"]),
    "ENFJ": ("INFP", ["INFJ", "ENFP", "ISFP"]),
    "ENFP": ("INFJ", ["INFP", "INTJ", "ENFJ"]),
    "ISTJ": ("ESFP", ["ISFJ", "ESTJ", "ISTP"]),
    "ISFJ": ("ESTP", ["ESFJ", "ISTJ", "ISFP"]),
    "ESTJ": ("ISFP", ["ISTJ", "ESFJ", "ESTP"]),
    "ESFJ": ("ISFP", ["ESFP", "ESTJ", "ISFJ"]),
    "ISTP": ("ESFJ", ["ESTP", "ISFP", "ISTJ"]),
    "ISFP": ("ESTJ", ["ISFJ", "ESFP", "ISTP"]),
    "ESTP": ("ISFJ", ["ESFP", "ESTJ", "ISTP"]),
    "ESFP": ("ISTJ", ["ESFJ", "ISFP", "ESTP"]),
}

# 🔍 MBTI 입력
user_mbti = st.selectbox("당신의 MBTI를 선택해주세요 👇", list(mbti_traits.keys()))

# 🎯 분석 버튼
if st.button("결과 보기 💘"):
    with st.spinner("당신의 성격과 궁합 분석 중...🧬"):
        time.sleep(2)

    # 🎈 풍선 효과
    st.balloons()

    # 🔍 성격 설명
    st.header("🧠 당신의 성격 유형")
    st.markdown(f"**{user_mbti}**: {mbti_traits[user_mbti]}")

    # 💞 궁합 설명
    best_match, other_matches = mbti_compatibility[user_mbti]
    st.header("💞 찰떡궁합 MBTI")
    st.success(f"당신과 최고의 궁합은 바로... **{best_match}** 💖")

    st.subheader("💌 잘 맞는 다른 유형들")
    st.markdown(" | ".join([f"🌟 **{mbti}**" for mbti in other_matches]))

    # 📚 설명 추가
    st.markdown("💡 이 결과는 MBTI 심리유형 간 상호보완과 커뮤니케이션 특성을 바탕으로 제공됩니다. 사람마다 차이가 있어요 😊")

# 📘 참고 정보
with st.expander("📖 MBTI 궁합이란?"):
    st.markdown("""
    MBTI 궁합은 각 성격 유형이 어떻게 소통하고 갈등을 조율하는지를 바탕으로 분석돼요.  
    예를 들어, 감성형(F)이 이성형(T)과 만나면 서로의 부족한 면을 채워줄 수 있어요.  
    이상형은 참고용이고, 진짜 인연은 서로를 이해하려는 마음에서 시작된답니다 💕
    """)

# 👣 푸터
st.markdown("---")
st.markdown("Made with 💗 by [Your Name] | Powered by Streamlit 🚀")
