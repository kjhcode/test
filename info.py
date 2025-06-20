# main.py
import streamlit as st
from modules.subjects import display_subject_area
from modules.faq import display_faq
from modules.quiz import display_quiz
from modules.aptitude import display_aptitude_test

# 페이지 설정
st.set_page_config(layout="wide", page_title="정보과 안내", page_icon="💻")

# --- 공통 스타일 설정 ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');
html, body, [class*="st-"] {
    font-family: 'Gowun Dodum', sans-serif;
}
h1 { color: #4B088A; text-align: center; }
h2, h3, h4 { color: #800080; margin-top: 2rem; }
.stExpander { border: 1px solid #DDA0DD; border-radius: 5px; padding: 10px; margin-bottom: 10px; }
.stButton>button { background-color: #EE82EE; color: white; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# --- 탭 구조 ---
tabs = st.tabs(["과목 소개", "FAQ", "퀴즈", "적성 테스트"])

with tabs[0]:
    # 예시 과목 내용
    example_subjects = {
        "<span style='font-size: 0.7em;'>💻 컴퓨팅 사고력</span>": "문제를 단계적으로 분석하고 해결하는 힘을 길러요.",
        "<span style='font-size: 0.7em;'>📊 데이터 분석</span>": "데이터를 활용해 세상을 더 깊이 이해할 수 있어요.",
        "<span style='font-size: 0.7em;'>🤖 인공지능 기초</span>": "AI 기술을 배우고 활용하는 능력을 길러요."
    }
    display_subject_area("📚 정보과목에서 배우는 핵심 영역", example_subjects)

with tabs[1]:
    display_faq()

with tabs[2]:
    display_quiz()

with tabs[3]:
    display_aptitude_test()
