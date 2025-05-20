import streamlit as st

# MBTI별 추천 색상 및 옷 코디 이미지
mbti_styles = {
    "INTJ": {"color": "#5A3EBD", "style_desc": "세련된 미니멀 블랙룩 🖤", "image": "https://i.pinimg.com/originals/34/1f/5f/341f5f98cf57b84e7125b0c2f645c54f.jpg"},
    "INTP": {"color": "#336699", "style_desc": "편안한 스트릿룩 😎", "image": "https://i.pinimg.com/originals/59/82/6d/59826d7bc4c61a84d8418d68c9c8ac31.jpg"},
    "ENTJ": {"color": "#FF4500", "style_desc": "시크한 수트 스타일 👔", "image": "https://i.pinimg.com/originals/27/ef/3a/27ef3aa7d6a19a68fc84ff22efc4a6cf.jpg"},
    "ENTP": {"color": "#FF69B4", "style_desc": "개성만점 컬러풀 캐주얼 ✨", "image": "https://i.pinimg.com/originals/63/91/57/6391575c13d5c7f0b999ac4b8dc80da1.jpg"},
    "INFJ": {"color": "#6A5ACD", "style_desc": "몽환적인 레이어드룩 🌙", "image": "https://i.pinimg.com/originals/fc/56/9a/fc569a97b3b92d81c3c69f8a14f6e11b.jpg"},
    "INFP": {"color": "#3CB371", "style_desc": "빈티지 로맨틱 무드 🌼", "image": "https://i.pinimg.com/originals/f7/3d/cd/f73dcd201c46477be4073e7b05f2c94e.jpg"},
    "ENFJ": {"color": "#FF6347", "style_desc": "우아한 오피스룩 💼", "image": "https://i.pinimg.com/originals/c3/b6/e3/c3b6e3e62148e7eeff3426c65ceec597.jpg"},
    "ENFP": {"color": "#FFA500", "style_desc": "발랄한 캐주얼 믹스룩 🧡", "image": "https://i.pinimg.com/originals/42/14/4f/42144f64c4d56f849725510cfda0b7b3.jpg"},
    "ISTJ": {"color": "#2E8B57", "style_desc": "정갈한 클래식룩 🟢", "image": "https://i.pinimg.com/originals/b3/3f/0f/b33f0f29d39d68c4b50cf3aa4c9d2973.jpg"},
    "ISFJ": {"color": "#FFB6C1", "style_desc": "따뜻한 내추럴룩 🌸", "image": "https://i.pinimg.com/originals/9e/f3/91/9ef391f597c08c75a16390df68edda3d.jpg"},
    "ESTJ": {"color": "#4682B4", "style_desc": "깔끔한 셋업 스타일 💼", "image": "https://i.pinimg.com/originals/b0/f8/33/b0f833b60f84c73e08b4802e7e5c2c95.jpg"},
    "ESFJ": {"color": "#FF69B4", "style_desc": "화사한 데이트룩 💖", "image": "https://i.pinimg.com/originals/2d/c4/1b/2dc41bc4f4746409e3fa2bd14a9c57c9.jpg"},
    "ISTP": {"color": "#708090", "style_desc": "심플한 워크웨어룩 🛠️", "image": "https://i.pinimg.com/originals/6e/2b/f4/6e2bf45a31e61aef207b3dfb2019ab4b.jpg"},
    "ISFP": {"color": "#FFDEAD", "style_desc": "귀여운 내추럴 캐주얼 🐰", "image": "https://i.pinimg.com/originals/4c/c7/c3/4cc7c3e931145f85d2dfaf9ae5dfbd7e.jpg"},
    "ESTP": {"color": "#FF8C00", "style_desc": "트렌디한 스트릿룩 🧢", "image": "https://i.pinimg.com/originals/38/2d/c6/382dc69c5e725be8c02fbb998d6f53b1.jpg"},
    "ESFP": {"color": "#FF6F61", "style_desc": "큐티 & 화려한 파티룩 🎉", "image": "https://i.pinimg.com/originals/5b/c6/31/5bc631f7de933dbd589c3153f47f3a4b.jpg"},
}

st.set_page_config(page_title="MBTI 스타일 추천 💖", layout="centered")

st.markdown("""
    <style>
    .stApp {
        transition: background-color 1s ease;
        font-family: "Comic Sans MS", cursive;
    }
    h1, h2 {
        text-align: center;
    }
    img {
        display: block;
        margin: 0 auto;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        max-width: 80%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 MBTI별 어울리는 스타일 추천 💃")

mbti = st.selectbox("당신의 MBTI는 무엇인가요? 🤔", list(mbti_styles.keys()))

if st.button("결과 보러 가기! 🎁"):
    color = mbti_styles[mbti]["color"]
    style = mbti_styles[mbti]["style_desc"]
    image = mbti_styles[mbti]["image"]

    st.markdown(f"""
        <script>
        document.querySelector('.stApp').style.backgroundColor = '{color}';
        </script>
    """, unsafe_allow_html=True)

    st.markdown(f"<h2>✨ {mbti}에게 어울리는 색깔은 <span style='color:white'>{color}</span> 💗</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3>👗 추천 스타일: {style}</h3>", unsafe_allow_html=True)
    st.image(image, caption="감각적인 코디 예시 ✨")
