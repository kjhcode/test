import streamlit as st
from PIL import Image

# 페이지 설정
st.set_page_config(layout="wide", page_title="정보과 안내", page_icon="💻")

# --- CSS 스타일 추가 ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');
html, body, [class*="st-"] { font-family: 'Gowun Dodum', sans-serif; }
h1 { color: #4B088A; text-align: center; }
h2, h3, h4 { color: #800080; margin-top: 2rem; }
.stExpander { border: 1px solid #DDA0DD; border-radius: 5px; padding: 10px; }
.stButton>button { background-color: #EE82EE; color: white; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# --- 사이드바 ---
st.sidebar.header("📚 이 가이드에 대해")
st.sidebar.write("""
이 가이드는 2022 개정 교원과정 정보과 내용을 바탕으로 
고등학교 학생들이 과목 선택 시 
\"정보교과\"에 대한 이해를 돕기 위해 제작되었습니다.
""")

st.sidebar.markdown("---")
st.sidebar.header("🔗 참고 자료")
st.sidebar.markdown("""
- [2022 개정 교원과정/정보과 - 나무위키](https://namu.wiki/w/2022%20개정%20교원과정/정보과)
- [2022 개정 교원과정 정보 살해보기 - 네이버 블로그](https://m.blog.naver.com/math_rani/223294591331)
- [과목선택 워크부 - 울산광역시교육청](https://use.go.kr/component/file/ND_fileDownload.do?q_fileSn=786326&q_fileId=e36a31ba-8557-4ce8-b5ef-52217892487e)
- [고교학점제 지원센터 - 과목 소개 - 부산광역시교육청](https://home.pen.go.kr/hscredit/cm/cntnts/cntntsView.do?cntntsId=3729&mi=17411)
""")

# --- 함수 정의 ---
def display_curriculum(title, description, info_dict):
    st.subheader(title)
    st.markdown(description, unsafe_allow_html=True)
    cols = st.columns(len(info_dict))
    for i, col in enumerate(cols):
        area, content = list(info_dict.items())[i]
        with col:
            st.markdown(f"### {area}", unsafe_allow_html=True)
            st.write(content)

def display_quiz(questions):
    st.subheader("💻 정보교과 상식 퀴즈!")
    for i, q in enumerate(questions):
        with st.container():  # 문제마다 독립된 컨테이너 생성
            st.markdown(f"**문제 {i+1}.** {q['question']}")
            user_answer = st.radio(
                f"문제 {i+1} 정답 선택:", 
                q['options'], 
                key=f"quiz_{i}", 
                index=None
            )

            if user_answer is not None:
                if user_answer == q['answer']:
                    st.success("🎉 정답입니다! 잘 알고 있네요!")
                else:
                    st.error(f"😅 정답은 '{q['answer']}'입니다.")
                st.info(f"**해설:** {q['explanation']}")

            st.markdown("---")

def display_aptitude_test(questions):
    st.subheader("📚 정보교과 적성 간단 테스트")
    st.markdown("**아래 항목 중 해당되는 것을 체크해보세요!**")
    checked_count = 0
    for i, question in enumerate(questions):
        if f"apt_{i}" not in st.session_state:
            st.session_state[f"apt_{i}"] = False
        if st.checkbox(question, key=f"apt_{i}"):
            checked_count += 1
    st.markdown(f"체크한 항목 수: **{checked_count}개**")
    if checked_count >= 6:
        st.balloons()
        st.success("정보교과에 대한 흥미와 적성이 아주 높아요!")
    elif checked_count >= 4:
        st.info("잠재력과 흥미가 충분해요! 도전해봐요!")
    elif checked_count >= 2:
        st.warning("조금 더 관심을 가져보면 좋아요!")
    else:
        st.error("아직은 정보교과가 낯설 수 있어요. 조금 더 알아가보아요!")

# --- 본문 ---
st.title("💻 미래를 코딩하다! 2022개정 교원과정의 고등학교 정보과 소개")

st.markdown("""
안녕, 친구들! 😊<br>
2학년 과목 선택 고민 많지요?<br>
과목선택에 걸리는 \"정보\" \"프로그래밍\" \"인공지능 기초\" \"빅데이터 분석\" 이름, 흥시가 나오지요!<br><br>
정보교과는 평소 사이에서 보는 IT의 공동점이자, 방법입니다!<br>어느 과목을 선택할지, 함께 생각해보어요!
""", unsafe_allow_html=True)

# --- 커리큘럼 출력 ---
display_curriculum(
    "📚 정보(일반선택)과목에서 무엇을 배울까요?",
    "2022 개정 교원과정의 정보교과는 클기 5가지 영역으로 나누어지고, 컴퓨팅 생각 기본의 문제 해결 방식을 비슷한 통신에서 통합하는 과정입니다.<br>",
    {
        "💻 컴퓨팅 시스템": "컴퓨터의 하드웨어/소프트웨어 이해.",
        "📈 데이터": "데이터 수집과 분석, 정보 도출.",
        "🧩 알고리즘과 프로그래밍": "문제 해결 알고리즘과 프로그래밍 실습.",
        "🤖 인공지능": "AI 기본 개념과 활용.",
        "🌐 디지털 문화": "디지털 사회의 윤리 및 시민성."
    }
)

display_curriculum(
    "📚 인공지능 기초(진로선택) 과목에서 무엇을 배울까요?",
    "인공지능의 원리, 학습 방식, 사회적 영향, 그리고 프로젝트 기반 탐구 활동을 통해 AI 문제 해결 능력을 배웁니다.<br>",
    {
        "💻 인공지능의 이해": "AI의 원리와 탐색 기법.",
        "📈 인공지능과 학습": "기계학습, 딥러닝 기초.",
        "🧩 인공지능의 사회적 영향": "윤리, 진로, 사회 변화.",
        "🌐 인공지능 프로젝트": "SDGs 연계 AI 문제 해결 프로젝트."
    }
)

display_curriculum(
    "📚 데이터 과학(진로선택)과목에서 무엇을 배울까요?",
    "기계학습을 활용한 데이터 분석 및 해석 능력을 배양하는 과목입니다.<br>",
    {
        "💻 데이터 과학의 이해": "데이터 기반 의사 결정 이해.",
        "📈 데이터 준비와 분석": "데이터 수집, 전처리, 시각화.",
        "🧩 데이터 모델링과 평가": "모델 설계와 평가 방법.",
        "🌐 데이터 과학 프로젝트": "프로젝트 기반 문제 해결 실습."
    }
)

display_curriculum(
    "📚 소프트웨어와 생활(융합선택)과목에서 무엇을 배울까요?",
    "소프트웨어를 활용하여 실생활 문제를 해결하고 가치를 창출하는 융합적 사고를 기르는 과목입니다.<br>",
    {
        "💻 세상을 변화시키는 소프트웨어": "사회 변화를 이끄는 SW 사례 탐구.",
        "📈 작품을 창작하는 소프트웨어": "피지컬 컴퓨팅 기반 작품 제작.",
        "🧩 현상을 분석하는 소프트웨어": "데이터 기반 현상 분석.",
        "🤖 모의 실험하는 소프트웨어": "시뮬레이션 활용.",
        "🌐 가치를 창출하는 소프트웨어": "아이디어 기반 SW 프로젝트."
    }
)

display_curriculum(
    "📚 정보과학(진로선택)과목에서 무엇을 배울까요?",
    "전문적인 알고리즘, 자료구조, 프로그래밍 능력을 기르고, 다양한 문제를 컴퓨팅 관점에서 해결합니다.<br>",
    {
        "💻 프로그래밍": "효율적인 프로그래밍 구현 능력.",
        "📈 자료처리 → 데이터 구조": "데이터 구조화 및 처리.",
        "🧩 알고리즘": "문제 해결 중심 알고리즘 설계.",
        "🌐 컴퓨팅 시스템 → 정보과학 프로젝트": "학제 간 프로젝트 수행."
    }
)

# --- 퀴즈 및 적성 테스트 실행 예시 ---
quiz_questions = [
    {
        "question": "컴퓨터에게 일을 시키기 위해 사용하는 약속된 언어는?",
        "options": ["한국어", "영어", "프로그래밍 언어", "수학 언어"],
        "answer": "프로그래밍 언어",
        "explanation": "컴퓨터는 사람이 쓰는 언어를 이해하지 못하므로, 약속된 프로그래밍 언어를 사용해요."
    }
]

display_quiz(quiz_questions)

display_aptitude_test([
    "새로운 기술에 관심이 많다.",
    "문제를 해결하는 걸 좋아한다.",
    "데이터를 분석하는 게 흥미롭다.",
    "컴퓨터나 기계의 원리가 궁금하다.",
    "프로그래밍을 배워보고 싶다."
])

