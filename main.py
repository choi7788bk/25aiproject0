import streamlit as st

# 16가지 MBTI별 추천 데이터 (색깔, 동물, IT 브랜드(로고URL), 옷 브랜드(로고URL))
mbti_info = {
    "INTJ": {
        "color": "#5A3EBD",
        "animal": "🦉 부엉이",
        "it_brand": ("Apple 🍎", "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"),
        "clothing_brand": ("Uniqlo 👕", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Uniqlo_logo.svg/1200px-Uniqlo_logo.svg.png"),
    },
    "INTP": {
        "color": "#336699",
        "animal": "🦅 독수리",
        "it_brand": ("Microsoft 🪟", "https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg"),
        "clothing_brand": ("Gap 🧥", "https://upload.wikimedia.org/wikipedia/commons/3/3a/Gap_logo.svg"),
    },
    "ENTJ": {
        "color": "#FF4500",
        "animal": "🦁 사자",
        "it_brand": ("Tesla ⚡", "https://upload.wikimedia.org/wikipedia/commons/b/bd/Tesla_Motors.svg"),
        "clothing_brand": ("Nike 👟", "https://upload.wikimedia.org/wikipedia/commons/a/a6/Logo_NIKE.svg"),
    },
    "ENTP": {
        "color": "#FF69B4",
        "animal": "🦊 여우",
        "it_brand": ("Google 🔍", "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg"),
        "clothing_brand": ("Adidas 🏃‍♂️", "https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg"),
    },
    "INFJ": {
        "color": "#6A5ACD",
        "animal": "🦢 백조",
        "it_brand": ("Adobe 🎨", "https://upload.wikimedia.org/wikipedia/commons/d/d7/Adobe_Corporate_Logo.svg"),
        "clothing_brand": ("H&M 👗", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/H%26M-Logo.svg/1200px-H%26M-Logo.svg.png"),
    },
    "INFP": {
        "color": "#3CB371",
        "animal": "🦋 나비",
        "it_brand": ("Spotify 🎵", "https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg"),
        "clothing_brand": ("Forever 21 🌸", "https://upload.wikimedia.org/wikipedia/commons/7/7a/Forever_21_logo.svg"),
    },
    "ENFJ": {
        "color": "#FF6347",
        "animal": "🐦 제비",
        "it_brand": ("Facebook 📘", "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"),
        "clothing_brand": ("Zara 👚", "https://upload.wikimedia.org/wikipedia/commons/5/5a/Zara_Logo.svg"),
    },
    "ENFP": {
        "color": "#FFA500",
        "animal": "🐆 치타",
        "it_brand": ("Twitter 🐦", "https://upload.wikimedia.org/wikipedia/en/6/60/Twitter_Logo_as_of_2021.svg"),
        "clothing_brand": ("Levi's 👖", "https://upload.wikimedia.org/wikipedia/commons/2/29/Levis_logo.svg"),
    },
    "ISTJ": {
        "color": "#2E8B57",
        "animal": "🐢 거북이",
        "it_brand": ("IBM 💻", "https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg"),
        "clothing_brand": ("Dockers 👔", "https://upload.wikimedia.org/wikipedia/commons/e/e8/Dockers_logo.svg"),
    },
    "ISFJ": {
        "color": "#FFB6C1",
        "animal": "🐿️ 다람쥐",
        "it_brand": ("Canon 📷", "https://upload.wikimedia.org/wikipedia/commons/4/40/Canon_logo.svg"),
        "clothing_brand": ("GAP Kids 👕", "https://upload.wikimedia.org/wikipedia/commons/3/3a/Gap_logo.svg"),
    },
    "ESTJ": {
        "color": "#4682B4",
        "animal": "🐺 늑대",
        "it_brand": ("Intel 🖥️", "https://upload.wikimedia.org/wikipedia/commons/c/c9/Intel-logo.svg"),
        "clothing_brand": ("Tommy Hilfiger 👔", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Tommy_Hilfiger_logo.svg/1280px-Tommy_Hilfiger_logo.svg.png"),
    },
    "ESFJ": {
        "color": "#FF69B4",
        "animal": "🐩 푸들",
        "it_brand": ("Samsung 📱", "https://upload.wikimedia.org/wikipedia/commons/2/24/Samsung_Logo.svg"),
        "clothing_brand": ("Forever 21 👗", "https://upload.wikimedia.org/wikipedia/commons/7/7a/Forever_21_logo.svg"),
    },
    "ISTP": {
        "color": "#708090",
        "animal": "🦅 매",
        "it_brand": ("GoPro 📷", "https://upload.wikimedia.org/wikipedia/commons/5/5d/GoPro_logo.svg"),
        "clothing_brand": ("The North Face 🧥", "https://upload.wikimedia.org/wikipedia/commons/6/66/The_North_Face_logo.svg"),
    },
    "ISFP": {
        "color": "#FFDEAD",
        "animal": "🐰 토끼",
        "it_brand": ("Nintendo 🎮", "https://upload.wikimedia.org/wikipedia/commons/0/0d/Nintendo.svg"),
        "clothing_brand": ("Free People 🌸", "https://upload.wikimedia.org/wikipedia/commons/5/56/Free_People_Logo.svg"),
    },
    "ESTP": {
        "color": "#FF8C00",
        "animal": "🐅 호랑이",
        "it_brand": ("Snapchat 👻", "https://upload.wikimedia.org/wikipedia/en/c/c4/Snapchat_logo.svg"),
        "clothing_brand": ("Puma 👟", "https://upload.wikimedia.org/wikipedia/commons/f/fd/Puma_logo.svg"),
    },
    "ESFP": {
        "color": "#FF6F61",
        "animal": "🐆 치타",
        "it_brand": ("Samsung 📱", "https://upload.wikimedia.org/wikipedia/commons/2/24/Samsung_Logo.svg"),
        "clothing_brand": ("Zara 👗", "https://upload.wikimedia.org/wikipedia/commons/5/5a/Zara_Logo.svg"),
    },
}

mbti_list = list(mbti_info.keys())

# 페이지 설정
st.set_page_config(page_title="🌈 MBTI 스타일 추천", layout="centered")

# 기본 스타일 CSS + 귀여운 효과
def local_css():
    st.markdown(
        """
        <style>
        .stApp {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            transition: background-color 1s ease;
            padding: 30px;
        }
        h1 {
            text-align: center;
            font-weight: 900;
            color: #222;
            text-shadow: 2px 2px 5px #aaa;
        }
        .result {
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            color: white;
            margin-top: 30px;
            animation: fadeIn 1s ease forwards;
        }
        .item-row {
            display: flex;
            align-items: center;
            margin: 15px 0;
            font-size: 1.3rem;
        }
        .item-row img {
            height: 40px;
            margin-left: 15px;
            border-radius: 8px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
            cursor: pointer;
        }
        .item-row img:hover {
            transform: scale(1.1);
        }
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(20px);}
            to {opacity: 1; transform: translateY(0);}
        }
        .emoji {
            font-size: 2rem;
            margin-right: 10px;
            user-select: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

local_css()

st.title("🎉 MBTI 스타일 추천 웹앱 🥳")

selected_mbti = st.selectbox("✨ 당신의 MBTI를 선택해 주세요! ✨", mbti_list)

if st.button("결과 보러 가기 👉"):
    info = mbti_info[selected_mbti]
    bg_color = info["color"]

    # 배경색 변경 JS
    st.markdown(
        f"""
        <script>
        document.querySelector('.stApp').style.backgroundColor = '{bg_color}';
        </script>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="result" style="background-color:{bg_color};">
        <h2>🎯 {selected_mbti} 당신에게 딱 맞는 스타일은?</h2>
        <div class="item-row"><span class="emoji">🌈</span> 어울리는 색깔: <strong>{bg_color}</strong></div>
        <div class="item-row"><span class="emoji">🐾</span> 당신의 동물: <strong>{info['animal']}</strong></div>
        <div class="item-row"><span class="emoji">💻</span> IT 브랜드: <strong>{info['it_brand'][0]}</strong> <img src="{info['it_brand'][1]}" alt="IT 브랜드 로고"></div>
        <div class="item-row"><span class="emoji">👚</span> 옷 브랜드: <strong>{info['clothing_brand'][0]}</strong> <img src="{info['clothing_brand'][1]}" alt="옷 브랜드 로고"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.info("위에서 MBTI를 선택하고 '결과 보러 가기' 버튼을 눌러주세요! 🥰")
