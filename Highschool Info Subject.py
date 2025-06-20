import streamlit as st

# 퀴즈 함수 유지

def display_quiz(questions):
    st.subheader("💻 정보교과 상식 퀴즈!")
    for i, q in enumerate(questions):
        with st.container():
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

# 탭 구조 생성
st.set_page_config(layout="wide")

menu = ["1. 정보과 소개", "2. 교육과정 변화", "3. 학교 수업 및 FAQ", "4. 진로/적성/의견", "5. 응원"]
tabs = st.tabs(menu)

# 첫 번째 탭 - 정보과 소개
with tabs[0]:
    st.markdown("""
        <h1 style='text-align: center; color: #4B088A;'>💻 미래를 코딩하다! 2022 개정 교육과정 고등학교 정보과 소개</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size: 1.1rem;'>
    정보교과는 <br> 단순히 컴퓨터를 배우는 걸 넘어서, <br> 우리가 살아갈 미래 사회에서 꼭 필요한 <span style="color: red;"> 
    생각하는 힘과 문제 해결 능력을 키워</span>주는 아주 중요한 과목입니다!<br> 왜 정보교과를 선택해야 하는지,<br> 같이 한번 알아볼까요?
    """, unsafe_allow_html=True)
   
   
    st.markdown("""
    <h3 style='color: #800080;'>📚 정보과목을 선택하면 좋은 점!</h3>
    <ul style='font-size: 1.05rem;'>
        <li><b>미래 사회 핵심 역량 강화:</b> AI, 데이터 분석 등 미래 유망 분야의 기초를 다질 수 있어요.</li>
        <li><b>문제 해결 능력 향상:</b> 복잡한 문제를 논리적으로 분석하고 해결하는 능력을 키워요.</li>
        <li><b>창의적인 아이디어 구현:</b> 코딩을 통해 나만의 아이디어를 실제로 만들 수 있어요.</li>
        <li><b>융합 사고력 배양:</b> 과학, 예술, 인문 등 다양한 분야와의 융합이 가능해요.</li>
        <li><b>진로 선택의 폭 확대:</b> 다양한 분야로 진출할 수 있는 발판이 돼요.</li>
    </ul>
    """, unsafe_allow_html=True)

# 두 번째 탭 - 교육과정 변화
with tabs[1]:
    st.markdown("<h2 style='color:#800080;'>📚 2022 고등학교 정보 과목은 이렇게 바뀝니다.</h2>", unsafe_allow_html=True)
    st.info("2022 개정 교육과정에서는 다양한 정보 관련 과목이 개설되어 있어요!")

    st.markdown("""
    <div style='line-height: 1.8;'>
    ✅ <b>일반선택</b>: 정보<br>
    ✅ <b>진로선택</b>: 인공지능 기초, 데이터 과학, 정보과학<br>
    ✅ <b>융합선택</b>: 소프트웨어와 생활
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("🖥️ 정보과(일반선택)")
    st.success("컴퓨팅 시스템, 데이터, 알고리즘과 프로그래밍, 인공지능, 디지털 문화 등 5가지 영역을 배워요.")

    st.subheader("🖥️ 인공지능 기초(진로선택)")
    st.success("AI의 원리, 학습 알고리즘, 사회적 영향, 프로젝트 기반 학습 등을 배워요.")

    st.subheader("🖥️ 데이터 과학(진로선택)")
    st.success("데이터 수집, 전처리, 모델링, 프로젝트를 통해 데이터 분석 역량을 키워요.")

    st.subheader("🖥️ 소프트웨어와 생활(융합선택)")
    st.success("소프트웨어로 문제를 해결하는 다양한 실생활 융합 사례를 탐구해요.")

    st.subheader("🖥️ 정보과학(진로선택)")
    st.success("자료구조, 알고리즘, 프로그래밍, 정보과학 프로젝트 중심 학습으로 구성돼 있어요.")

# 세 번째 탭 - 우리학교 소개 + FAQ
with tabs[2]:
    st.header("🏫 우리 학교 정보교과 수업은?")
    st.markdown("""
    <p style='font-size:1.05rem;'>
    최신 컴퓨터 실습실에서 실습 중심으로 수업을 진행해요.<br>
    직접 코드를 작성해보고, 해커톤이나 프로젝트 발표회도 경험해요.<br>
    정보 선생님이 친절하고 수업이 재미있어서 만족도가 높아요!
    </p>
    """, unsafe_allow_html=True)

    st.header("👩‍🎓 정보교과 선배들의 이야기")
    st.info("\"처음엔 어렵지만 재밌게 배울 수 있어요!\" - 2학년 김OO 선배")
    st.info("\"문과도 할 수 있어요! 사회 현상을 데이터로 분석했어요.\" - 2학년 이OO 선배")
    st.info("\"정보를 통해 진로 탐색에 도움을 받았어요.\" - 3학년 박OO 선배")

    st.header("❓ 정보교과에 대한 궁금증 (FAQ)")
    with st.expander("Q1. 코딩을 안 해봤는데 괜찮을까요?"):
        st.success("물론이죠! 처음 배우는 친구들을 위해 기초부터 차근차근 배워요.")
    with st.expander("Q2. 수학을 잘 못하는데요?"):
        st.success("수학보단 논리적 사고가 중요해요. 수업 중 필요한 부분은 충분히 설명해줘요.")
    with st.expander("Q3. 진로에 도움이 되나요?"):
        st.success("IT뿐 아니라 다양한 분야에서 정보 활용 역량은 강점이 될 수 있어요.")
    with st.expander("Q4. 수업이 지루하지 않나요?"):
        st.success("실습과 프로젝트 위주 수업이라 재미있어요!")

# 네 번째 탭 - 진로 + 퀴즈 + 적성 + 의견
with tabs[3]:
    st.header("🖥️ 정보교과와 연결된 진로/학과")
    st.markdown("""
    💡 <b>컴퓨터/소프트웨어</b>: 개발자, 보안 전문가 등<br>
    💡 <b>데이터/AI</b>: 데이터 과학자, AI 연구자 등<br>
    💡 <b>융합기술</b>: 로봇공학, 스마트팜, 디지털 헬스케어 등
    """, unsafe_allow_html=True)

    quiz_questions = [
        {
            "question": "컴퓨터에게 일을 시키기 위해 사용하는 약속된 언어는?",
            "options": ["한국어", "영어", "프로그래밍 언어", "수학 언어"],
            "answer": "프로그래밍 언어",
            "explanation": "컴퓨터는 사람이 쓰는 언어를 이해하지 못하므로, 약속된 프로그래밍 언어를 사용해요."
        },
        {
            "question": "정보교과의 5가지 영역이 아닌 것은?",
            "options": ["컴퓨팅 시스템", "데이터", "알고리즘과 프로그래밍", "인공지능", "디자인"],
            "answer": "디자인",
            "explanation": "정보교과의 주요 영역은 컴퓨팅 시스템, 데이터, 알고리즘과 프로그래밍, 인공지능, 디지털 문화예요."
        }
    ]
    display_quiz(quiz_questions)

    st.subheader("💬 홍보물에 대한 의견 남기기")
    user_comment = st.text_area("💡 여기에 자유롭게 의견을 입력해 주세요:", height=100)
    if st.button("✉️ 의견 제출"):
        if user_comment:
            st.success("의견이 제출되었습니다! 감사합니다!")
        else:
            st.warning("의견을 입력해주세요!")

# 다섯 번째 탭 - 응원 메시지
with tabs[4]:
    st.markdown("""
        <h2 style='color: #4B088A;'>📣 여러분의 빛나는 미래를 응원해요! ❤️</h2>
        <p style='font-size:1.1rem;'>
        정보교과는 여러분의 잠재력을 깨우고 미래를 설계하는 데 훌륭한 도구입니다.<br>
        망설이지 말고 도전해보세요!<br>
        여러분의 멋진 도전을 항상 응원합니다! 💪<br>
        </p>
    """, unsafe_allow_html=True)
