import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# MBTI 별 데이터 정의
mbti_data = {
    'INTJ': {
        'color': '#2E3A59',
        'animal': '부엉이',
        'it_brand': 'Apple',
        'fashion_brand': 'COS',
        'outfits': [
            'https://i.pinimg.com/564x/3d/f2/ab/3df2ab4e0fbb2f2ef8a36cb038cc1e7f.jpg',
            'https://i.pinimg.com/564x/4e/4a/70/4e4a70dd620b9a93c4529c107d47d3b4.jpg',
            'https://i.pinimg.com/564x/1d/e2/5b/1de25b1a8c2f9125dd24e1c9b6e9d62d.jpg',
            'https://i.pinimg.com/564x/f1/33/1b/f1331b351726d49e380dc875c93fc98e.jpg'
        ]
    },
    'ENFP': {
        'color': '#FFD166',
        'animal': '돌고래',
        'it_brand': 'Google',
        'fashion_brand': 'ZARA',
        'outfits': [
            'https://i.pinimg.com/564x/64/f3/31/64f331dabc3dc67677f6312a6847e1ed.jpg',
            'https://i.pinimg.com/564x/49/56/13/495613f410e0b41d0ae42799426c2031.jpg',
            'https://i.pinimg.com/564x/37/f9/2a/37f92ad16e1f7adfd37377d870c1f4c3.jpg',
            'https://i.pinimg.com/564x/c9/93/c0/c993c06fa43dfb63a3247020d21f5cb3.jpg'
        ]
    },
    # 필요하면 다른 MBTI도 추가
}

st.set_page_config(page_title="MBTI 패션 추천", layout="wide")

# 입력 섹션
st.title("💡 나의 MBTI로 알아보는 감각적인 추천")
mbti_input = st.text_input("당신의 MBTI를 입력하세요 (예: INTJ)").upper()

if st.button("🎨 결과 보러 가기"):
    if mbti_input in mbti_data:
        data = mbti_data[mbti_input]
        st.markdown(
            f"<style>body {{ background-color: {data['color']}; color: white; }}</style>",
            unsafe_allow_html=True
        )

        st.subheader(f"🎨 어울리는 색깔: {data['color']}")
        st.subheader(f"🐾 어울리는 동물: {data['animal']}")
        st.subheader(f"💻 어울리는 IT 브랜드: {data['it_brand']}")
        st.subheader(f"👗 어울리는 옷 브랜드: {data['fashion_brand']}")

        st.markdown("### 📌 추천 코디 (Pinterest에서 가져온 이미지)")
        cols = st.columns(4)
        for idx, img_url in enumerate(data['outfits']):
            with cols[idx]:
                response = requests.get(img_url)
                img = Image.open(BytesIO(response.content))
                st.image(img, use_column_width=True)
    else:
        st.error("해당 MBTI는 준비되지 않았습니다. 대문자로 입력했는지 확인해주세요.")
