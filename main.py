import streamlit as st

# MBTI별 추천 정보 (예시 데이터)
mbti_info = {
    "INTJ": {
        "color": "#5A3EBD",  # 보라
        "animal": "🦉 부엉이",
        "it_brand": "Apple 🍎",
        "clothing_brand": "Uniqlo 👕",
        "coordi_imgs": [
            "https://i.pinimg.com/564x/4f/18/aa/4f18aa3c1c5e5a6e70ac54997f8e68a8.jpg",
            "https://i.pinimg.com/564x/7b/5b/0b/7b5b0bfde287b4cc8e647e6d0a30b91a.jpg",
            "https://i.pinimg.com/564x/c6/1e/fd/c61efdc251c40e365f76432d7f64f6bb.jpg",
        ],
    },
    "ESFP": {
        "color": "#FF6F61",  # 밝은 빨강
        "animal": "🐆 치타",
        "it_brand": "Samsung 📱",
        "clothing_brand": "Zara 👗",
        "coordi_imgs": [
            "https://i.pinimg.com/564x/9b/3a/84/9b3a8435ff5d6c111a28a858b64f97d7.jpg",
            "https://i.pinimg.com/564x/fd/c7/c2/fdc7c2b1f08c2f191d3a2a9d54d0efec.jpg",
            "https://i.pinimg.com/564x/3c/39/3a/3c393a3f75c9887ab03445d8f65d1ac1.jpg",
        ],
    },
    # ... 여기에 16가지 MBTI 전부 추가 가능
}

# 전체 MBTI 리스트 (예시)
mbti_list = list(mbti_info.keys())

# 페이지 제목과 스타일
st.set_page_config(page_title="🎨 MBTI 스타일 추천 웹앱", layout="centered")

# CSS for 감각적 스타일링 및 애니메이션
st.markdown(
    """
    <style>
    .stApp {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        transition: background-color 0.8s ease;
        padding: 20px;
    }
    h1 {
        text-align: center;
        font-weight: 900;
        color: #333;
    }
    .result-section {
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        margin-top: 20px;
        color: white;
        font-size: 1.2rem;
        animation: fadeIn 1s ease-in forwards;
    }
    .emoji {
        font-size: 2.5rem;
        margin-right: 10px;
    }
    .coordi-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit,minmax(150px,1fr));
        gap: 15px;
        margin-top: 20px;
    }
    .coordi-grid img {
        width: 100%;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transition: transform 0.3s ease;
        cursor: pointer;
    }
    .coordi-grid img:hover {
        transform: scale(1.05);
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎉 MBTI 기반 스타일 & 코디 추천 웹앱 💖")

# MBTI 선택 UI
selected_mbti = st.selectbox("✨ 당신의 MBTI를 선택해 주세요! ✨", options=mbti_list)

# 결과 보기 버튼
if st.button("결과 보러 가기 👉"):
    info = mbti_info[selected_mbti]
    # 배경색 변경을 위해 JS 사용 (스트림릿 자체에서 스타일 변경 제한적)
    bg_color = info["color"]
    js = f"""
    <script>
    document.querySelector('.stApp').style.backgroundColor = '{bg_color}';
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)

    # 결과 출력 영역
    st.markdown(
        f"""
        <div class="result-section" style="background-color:{bg_color};">
        <h2>🎯 {selected_mbti} 당신에게 딱 맞는 스타일은?</h2>
        <p>🌈 어울리는 색깔: <strong>{info['color']}</strong></p>
        <p>🐾 당신의 동물: <span class="emoji">{info['animal']}</span></p>
        <p>💻 잘 어울리는 IT 브랜드: <strong>{info['it_brand']}</strong></p>
        <p>👚 추천 옷 브랜드: <strong>{info['clothing_brand']}</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 코디 이미지 그리드
    st.markdown("<h3 style='color:white; margin-top:30px;'>👗 핀터레스트 느낌 귀여운 코디 추천 💕</h3>", unsafe_allow_html=True)
    cols = st.columns(3)
    for idx, img_url in enumerate(info["coordi_imgs"]):
        with cols[idx]:
            st.image(img_url, use_column_width=True, caption=f"코디 {idx + 1}")

else:
    st.info("위에서 MBTI를 선택하고 '결과 보러 가기' 버튼을 눌러주세요! 🥰")
