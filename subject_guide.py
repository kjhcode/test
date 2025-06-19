# informatics_guide.py (리팩토링 버전)
import streamlit as st
from PIL import Image

# ---------------------- 페이지 설정 ----------------------
st.set_page_config(layout="wide", page_title="정보과 안내", page_icon="💻")

# ---------------------- CSS 스타일 ----------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');
html, body, [class*="st-"] {
    font-family: 'Gowun Dodum', sans-serif;
}
h1, h2, h3, h4 { color: #800080; }
.stExpander { border: 1px solid #DDA0DD; border-radius: 5px; padding: 10px; margin-bottom: 10px; }
.stButton>button { background-color: #EE82EE; color: white; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# ---------------------- 사이드바 ----------------------
st.sidebar.header("📚 이 가이드에 대해")
st.sidebar.write("2022 개정 교육과정의 정보과 내용을 모두 담은 것입니다.")
st.sidebar.markdown("---")
st.sidebar.header("🔗 참고 자료")
st.sidebar.markdown("""
- [• 정보과 - 나무위키](https://namu.wiki/w/2022%20개정%20교육과정/정보과)
- [• 개정 교육과정 포스팅 블로그](https://m.blog.naver.com/math_rani/223294591331)
- [• 과목선택 안내서 등](https://www.jinhak.or.kr/subList/20000000271)
""")

# ---------------------- 공통 함수 정의 ----------------------
def render_subject_section(title, description, info_areas):
    st.subheader(title)
    st.markdown(description, unsafe_allow_html=True)
    cols = st.columns(min(len(info_areas), 3))
    for i, (area, detail) in enumerate(info_areas.items()):
        with cols[i % 3]:
            st.markdown(f"### {area}", unsafe_allow_html=True)
            st.write(detail)

# ---------------------- 메인 콘텐츠 ----------------------
st.title("💻 미래를 코딩하다! 정보과 소개")
st.markdown("""
<span style="font-size: 1.1em;">
정보과는 단순한 코딩 수업이 아니라 문제 해결력과 사고력을 키우는 교과입니다. <br>
AI, 빅데이터 시대를 살아갈 여러분에게 꼭 필요한 과목이에요!<br>
왜 정보과를 선택해야 할까요? 지금 함께 알아보아요!
</span>
""", unsafe_allow_html=True)

# ---------------------- 과목별 영역 ----------------------
subject_contents = [
    {
        "title": "📚 정보(일반선택) 과목 소개",
        "desc": """
        5가지 영역을 통해 <span style='color:red;'>컴퓨팅 사고력과 문제 해결 역량</span>을 기를 수 있어요!
        """,
        "areas": {
            "<span style='font-size: 0.8em;'>💻 컴퓨팅 시스템</span>": "하드웨어와 소프트웨어 원리 이해",
            "<span style='font-size: 0.8em;'>📈 데이터</span>": "데이터 수집, 분석, 시각화",
            "<span style='font-size: 0.8em;'>🧩 알고리즘과 프로그래밍</span>": "문제 해결 알고리즘과 파이썬 실습",
            "<span style='font-size: 0.8em;'>🤖 인공지능</span>": "AI 기초 개념과 사례 탐색",
            "<span style='font-size: 0.8em;'>🌐 디지털 문화</span>": "디지털 윤리 및 시민 역량"
        }
    },
    {
        "title": "📚 인공지능 기초(진로선택)",
        "desc": """
        <span style='color:red;'>지속가능발전목표와 AI 문제 해결 절차</span>를 중심으로 배우는 과목이에요!
        """,
        "areas": {
            "<span style='font-size: 0.8em;'>💻 AI 이해</span>": "탐색, 표현, 추론 원리",
            "<span style='font-size: 0.8em;'>📈 AI와 학습</span>": "기계학습, 신경망, 딥러닝",
            "<span style='font-size: 0.8em;'>🧩 사회적 영향</span>": "진로, 윤리, 사회 변화",
            "<span style='font-size: 0.8em;'>🌐 AI 프로젝트</span>": "문제 해결 기반 프로젝트 수행"
        }
    },
    {
        "title": "📚 데이터 과학(진로선택)",
        "desc": """
        <span style='color:red;'>기계학습을 활용한 데이터 기반 분석</span> 능력을 키우는 과목입니다.
        """,
        "areas": {
            "<span style='font-size: 0.8em;'>💻 데이터 과학 이해</span>": "데이터 의사결정 구조 이해",
            "<span style='font-size: 0.8em;'>📈 준비와 분석</span>": "수집, 전처리, 정제",
            "<span style='font-size: 0.8em;'>🧩 모델링과 평가</span>": "분석 도구 탐색 및 성능 평가",
            "<span style='font-size: 0.8em;'>🌐 프로젝트 수행</span>": "현실 문제 해결 탐구"
        }
    },
    {
        "title": "📚 소프트웨어와 생활(융합선택)",
        "desc": """
        <span style='color:red;'>문제 해결을 위한 소프트웨어 융합 활용</span>을 다루는 과목입니다.
        """,
        "areas": {
            "<span style='font-size: 0.8em;'>💻 사회 변화 사례</span>": "변화 이끄는 소프트웨어 활용",
            "<span style='font-size: 0.8em;'>📈 작품 창작</span>": "피지컬 컴퓨팅 프로젝트",
            "<span style='font-size: 0.8em;'>🧩 현상 분석</span>": "다양한 데이터 분석",
            "<span style='font-size: 0.8em;'>🤖 모의실험</span>": "시뮬레이션 응용",
            "<span style='font-size: 0.8em;'>🌐 가치 창출</span>": "스타트업 아이디어 구현"
        }
    },
    {
        "title": "📚 정보과학(진로선택)",
        "desc": """
        <span style='color:red;'>고급 컴퓨팅 문제 해결 역량</span>을 심화하는 과목입니다.
        """,
        "areas": {
            "<span style='font-size: 0.8em;'>💻 프로그래밍</span>": "효율적 구현과 모듈화",
            "<span style='font-size: 0.8em;'>📈 데이터 구조</span>": "자료처리 구조화",
            "<span style='font-size: 0.8em;'>🧩 알고리즘</span>": "문제 해결 알고리즘 설계",
            "<span style='font-size: 0.8em;'>🌐 정보과학 프로젝트</span>": "융합적 문제 해결"
        }
    }
]

for subject in subject_contents:
    render_subject_section(subject["title"], subject["desc"], subject["areas"])

# ---------------------- 마무리 ----------------------
st.header("📚 정보교과, 여러분의 미래를 설계합니다!")
st.markdown("""
정보교과는 여러분의 미래 경쟁력을 키워주는 멋진 도구입니다. <br>
논리력, 창의력, 문제 해결력, 협업 역량을 두루 키울 수 있어요. <br>
**당신의 미래를 정보교과와 함께 설계해 보세요!**
""", unsafe_allow_html=True)

# ---------------------- 끝 ----------------------
