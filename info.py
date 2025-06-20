
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="정보과 안내", page_icon="💻")

# --- CSS 스타일 ---
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

# --- 사이드바 ---
st.sidebar.header("📚 이 가이드에 대해")
st.sidebar.write("2022 개정 교육과정 정보과 내용을 바탕으로 고등학생들의 과목 선택을 돕기 위한 가이드입니다.")
st.sidebar.markdown("---")
st.sidebar.header("🔗 참고 자료")
st.sidebar.markdown("""
- [정보과 - 나무위키](https://namu.wiki/w/2022%20개정%20교육과정/정보과)
- [네이버 블로그](https://m.blog.naver.com/math_rani/223294591331)
- [울산교육청 워크북](https://use.go.kr/component/file/ND_fileDownload.do?q_fileSn=786326&q_fileId=e36a31ba-8557-4ce8-b5ef-52217892487e)
- [부산고교학점제센터](https://home.pen.go.kr/hscredit/cm/cntnts/cntntsView.do?cntntsId=3729&mi=17411)
- [서울진로진학센터](https://www.jinhak.or.kr/subList/20000000271)
- [대전고교학점제지원센터](https://djehcredit.com/hscredit/bbs/view.php?table=sschool&page=2&field=&str=&sid=157&mno=1)
""")

# --- 함수: 과목 렌더링 ---
def render_subject_section(title, description, info_areas):
    st.subheader(title)
    st.markdown(description, unsafe_allow_html=True)
    cols = st.columns(min(len(info_areas), 3))
    for i, (area, detail) in enumerate(info_areas.items()):
        with cols[i % len(cols)]:
            st.markdown(f"### {area}", unsafe_allow_html=True)
            st.write(detail)

# --- 함수: 퀴즈 ---
def run_quiz():
    st.subheader("💡 정보 상식 퀴즈")
    quiz_questions = [
        {
            "question": "컴퓨터에게 일을 시키기 위해 사용하는 약속된 언어는?",
            "options": ["한국어", "영어", "프로그래밍 언어", "수학 언어"],
            "answer": "프로그래밍 언어",
            "explanation": "프로그래밍 언어는 컴퓨터와의 소통을 위한 약속된 언어입니다."
        },
        {
            "question": "정보과 5대 영역이 아닌 것은?",
            "options": ["컴퓨팅 시스템", "데이터", "알고리즘과 프로그래밍", "인공지능", "디자인"],
            "answer": "디자인",
            "explanation": "디자인은 정보과 교육과정의 핵심 영역은 아닙니다."
        }
    ]
    for i, q in enumerate(quiz_questions):
        st.markdown(f"**문제 {i+1}.** {q['question']}")
        user_answer = st.radio("정답 선택:", q['options'], key=f"quiz_{i}")
        if user_answer:
            if user_answer == q['answer']:
                st.success("정답입니다! 👍")
            else:
                st.error(f"오답입니다. 정답은 '{q['answer']}' 입니다.")
            st.info(f"해설: {q['explanation']}")
        st.markdown("---")

# --- 함수: 적성 테스트 ---
def run_aptitude_test():
    st.subheader("🧠 정보과 적성 간단 테스트")
    questions = [
        "기술이나 기기를 배우는 걸 좋아한다.",
        "문제 원인 분석과 해결을 좋아한다.",
        "복잡한 걸 정리하는 걸 좋아한다.",
        "데이터를 해석하는 게 재밌다.",
        "아이디어를 구현해보고 싶다.",
        "디지털 기기의 작동 원리가 궁금하다.",
        "AI와 미래 기술에 관심 있다.",
        "친구들과 함께 문제 해결을 즐긴다."
    ]
    score = 0
    for i, q in enumerate(questions):
        if st.checkbox(q, key=f"aptitude_{i}"):
            score += 1
    st.markdown(f"총 {score}개 항목에 체크하셨습니다.")
    if score >= 6:
        st.balloons()
        st.success("정보과에 대한 흥미와 적성이 매우 높습니다! 미래 IT 전문가로의 길을 추천합니다.")
    elif score >= 4:
        st.info("정보과에 대한 잠재력과 흥미가 충분합니다! 도전해 보세요.")
    elif score >= 2:
        st.warning("정보과가 낯설지만 관심 있는 부분이 있습니다. 열린 마음으로 수업에 참여해 보세요.")
    else:
        st.error("아직 정보과에 대한 관심이 적을 수 있습니다. 조금 더 알아보세요!")

# --- 과목 안내 ---
subject_data = [
    {
        "title": "📚 정보(일반선택) 과목에서 무엇을 배울까요?",
        "desc": "2022 개정 교육과정의 정보교과는 크게 5가지 영역으로 나뉘며, 컴퓨팅 사고력과 실생활 문제 해결 능력을 기릅니다.",
        "areas": {
            "💻 컴퓨팅 시스템": "컴퓨터 작동 원리, 하드웨어/소프트웨어 이해",
            "📈 데이터": "데이터 수집과 분석으로 의미 있는 정보 도출",
            "🧩 알고리즘과 프로그래밍": "문제 해결 알고리즘 및 파이썬 실습",
            "🤖 인공지능": "AI 개념과 사례 탐구",
            "🌐 디지털 문화": "디지털 윤리와 시민 의식"
        }
    },
    {
        "title": "📚 인공지능 기초(진로선택) 과목에서 무엇을 배울까요?",
        "desc": "AI의 원리부터 윤리, 프로젝트 기반 문제 해결까지 배울 수 있어요!",
        "areas": {
            "💻 인공지능의 이해": "탐색, 지식 표현, 추론",
            "📈 인공지능과 학습": "기계학습, 신경망, 딥러닝",
            "🧩 인공지능의 사회적 영향": "사회 변화와 진로, 윤리",
            "🌐 인공지능 프로젝트": "SDGs 기반 문제 해결"
        }
    }
]

# --- 페이지 구성: 탭 ---
tabs = st.tabs(["정보 소개", "퀴즈", "적성 테스트", "FAQ"])

with tabs[0]:
    st.title("💻 2022 개정 정보과 안내")
    st.image("https://img.freepik.com/premium-photo/young-student-boy-programming-robot-in-ai-classroom_103577-1450.jpg", caption="AI실습 이미지", use_container_width=True)
    for subject in subject_data:
        render_subject_section(subject["title"], subject["desc"], subject["areas"])

with tabs[1]:
    run_quiz()

with tabs[2]:
    run_aptitude_test()

with tabs[3]:
    st.header("📚 자주 묻는 질문 (FAQ)")
    faqs = [
        ("Q1. 코딩을 해본 적이 없는데 괜찮을까요?", "정보과는 기초부터 배우므로 누구나 시작할 수 있어요."),
        ("Q2. 수학을 못하면 힘들까요?", "논리적 사고가 더 중요합니다. 필요한 수학은 수업 중 설명해줘요."),
        ("Q3. 어떤 진로에 도움이 되나요?", "모든 분야에서 정보 활용 능력은 강점이 됩니다."),
        ("Q4. 수업이 지루하지는 않나요?", "실습과 프로젝트가 많아 재미있고 활동적입니다!")
    ]
    for q, a in faqs:
        with st.expander(q):
            st.write(a)

st.markdown("---")
st.header("📚 여러분의 빛나는 미래를 응원해요!")
st.markdown("정보교과는 여러분의 꿈을 현실로 만들어 줄 멋진 시작입니다. 파이팅! 😊")
