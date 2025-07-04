import streamlit as st

# --- 사이드바 추가 ---
st.sidebar.header("📚 이 가이드에 대해")
st.sidebar.write("""
이 가이드는 2022 개정 교육과정 정보과 내용을 바탕으로
고등학교 학생들이 과목 선택 시
"정보교과"에 대한 이해를 돕기 위해 제작되었습니다.
""")
st.sidebar.markdown("---")
st.sidebar.header("🔗 참고 자료")
st.sidebar.markdown("""
- [2022 개정 교육과정/정보과 - 나무위키](https://namu.wiki/w/2022%20개정%20교육과정/정보과)
- [2022 개정 교육과정/정보과 - 네이버 블로그](https://m.blog.naver.com/math_rani/223294591331)
- [울산광역시교육청](https://use.go.kr/component/file/ND_fileDownload.do?q_fileSn=786326&q_fileId=e36a31ba-8557-4ce8-b5ef-52217892487e)
- [부산고교학점제지원센터](https://home.pen.go.kr/hscredit/cm/cntnts/cntntsView.do?cntntsId=3729&mi=17411)
- [서울진로진학정보센터](https://www.jinhak.or.kr/subList/20000000271)
- [대전고교학점제지원센터](https://djehcredit.com/hscredit/bbs/view.php?table=sschool&page=2&field=&str=&sid=157&mno=1)
""")

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

# 적성 테스트 함수 추가
def display_aptitude_test():
    st.subheader("💻 정보교과 적성 간단 테스트")
    st.write("아래 질문들을 읽고 나에게 해당하는 항목에 체크해 보세요! 정보교과가 너에게 잘 맞을지 살짝 엿볼 수 있을 거예요!")

    questions = [
        "새로운 기술이나 기기에 대해 배우는 것을 좋아한다.",
        "문제가 생겼을 때 원인을 분석하고 해결하는 과정을 즐긴다.",
        "복잡한 것을 단순하게 만들거나 순서대로 정리하는 것을 좋아한다.",
        "데이터나 숫자를 보고 의미를 파악하는 것에 흥미를 느낀다.",
        "나만의 아이디어를 실제로 만들어보고 싶다는 생각을 해본 적이 있다.",
        "컴퓨터나 스마트폰을 사용하는 것 외에 내부 작동 방식이 궁금하다.",
        "미래 사회의 변화나 인공지능 기술 발전에 관심이 많다.",
        "친구들과 함께 머리를 맞대고 문제를 해결하는 것을 좋아한다."
    ]

    st.markdown("---")
    st.markdown("**나에게 해당하는 항목에 체크해주세요!**")
    st.markdown("---")

    count = 0
    for i, q in enumerate(questions):
        if st.checkbox(q, key=f"apt_{i}"):
            count += 1

    st.markdown("---")
    st.subheader("📊 테스트 결과")
    st.write(f"체크한 항목 수: **{count}개**")

    if count >= 6:
        st.balloons()
        st.success("🎉 와우! 정보교과에 대한 흥미와 적성이 아주 높은 편이네요! 정보교과를 선택하면 정말 재미있게 배우고 큰 성장을 할 수 있을 거예요! 미래 IT 전문가의 꿈을 키워보는 건 어떨까요!")
    elif count >= 4:
        st.info("😊 정보교과에 대한 잠재력과 흥미가 충분하네요! 조금만 더 관심을 가지고 노력하면 정보교과에서 좋은 결과를 얻을 수 있을 거예요. 한번 도전해 보는 것을 추천해요!")
    elif count >= 2:
        st.warning("🙂 아직 정보교과가 낯설 수 있지만, 몇 가지 항목에 해당하는 것을 보니 관심 가질 만한 부분이 있네요! 정보교과 수업을 통해 새로운 재미를 발견할 수도 있어요. 너무 어렵게 생각하지 말고 열린 마음으로 다가가 보세요.")
    elif count >= 1:
        st.error("😅 아직 정보교과에 대해 잘 모르거나 크게 흥미를 느끼지 못할 수도 있어요. 하지만 정보교과는 미래 사회에 꼭 필요한 과목이니, 이 가이드를 통해 조금 더 알아보는 건 어떨까요? 생각보다 재미있을 수도 있답니다!")
    else:
        st.error("😅")

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
    <h3 style='color: #800080;'>📚 정보교과는 </h3>
    <p style='font-size: 1.1rem;'>
    단순히 컴퓨터를 배우는 걸 넘어서, <br> 우리가 살아갈 미래 사회에서 꼭 필요한 <span style="color: red;"> 
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
    st.subheader("🖥️ 정보(일반선택) :  컴퓨팅 사고력과 문제 해결 능력을 키우는 기본 과목!")
    st.success('컴퓨팅 시스템 : 컴퓨터가 어떻게 작동하는지, 하드웨어와 소프트웨어의 기본 원리를 이해함.')
    st.success('데이터 : 컴퓨터가 어떻게 작동하는지, 하드웨어와 소프트웨어의 기본 원리를 학습함.')
    st.success('알고리즘과 프로그래밍 : 문제를 해결하기 위한 절차(알고리즘)를 설계하고, 컴퓨터 언어(파이썬 등)로 프로그램을 구현함.')
    st.success('인공지능 : 스스로 학습하고 판단하는 인공지능의 기본 개념과 활용 사례를 탐구함.')
    st.success('디지털 문화 : 디지털 세상에서의 올바른 윤리 의식과 시민 역량을 기름.')
 
    st.subheader("🖥️ 인공지능 기초(진로선택) : 인공지능의 개념과 원리를 배우며 인공지능과 지속가능발전을 목표로 삼아 인공지능 문제 해결 절차를 학습하는 과목!")
    st.success('인공지능의 이해 :인공지능의 원리, 인공지능과 탐색, 지식의 표현과 추론. ')
    st.success('인공지능과 학습 : 기계학습과 데이터, 기계학습 알고리즘, 인공신경망과 딥러닝. ')
    st.success('인공지능의 사회적 영향 : 인공지능의 발전과 사회 변화, 인공지능과 진로, 인공지능과 윤리. ')
    st.success('인공지능 프로젝트 : 인공지능과 지속가능발전목표, 인공지능 문제 해결 절차.')

    st.subheader("🖥️ 데이터 과학(진로선택) : 데이터 기반 문제 해결을 위해 데이터를 분석하고 해석해서 실생활 문제를 해결하는 방법을 배우는 과목!")
    st.success('데이터 과학의 이해 : 데이터 기반 의사 결정의 중요성 인식. ')
    st.success('데이터 준비와 분석 : 데이터 분석을 위한 데이터 수집, 전처리 과정. 데이터 분석에 효과적인 형태로 변환.')
    st.success('데이터 모델링과 평가 : 데이터 모델의 개념. 분석을 위한 도구 탐색. 분석 결과 평가. ')
    st.success('데이터 과학 프로젝트 : 데이터 기반 문제 해결을 위한 데이터 과학의 기본 개념과 원리를 바탕으로 탐구 과정 수행.')

    st.subheader("🖥️ 소프트웨어와 생활(융합선택) : 소프트웨어로 문제를 해결하는 다양한 실생활 융합 사례를 탐구해요! ")
    st.success('세상을 변화시키는 소프트웨어 : 소프트웨어를 통해 세상을 변화시킨 사례 탐색.')
    st.success('작품을 창작하는 소프트웨어 : 피지컬 컴퓨팅 시스템의 구성 및 작동 원리 분석.')
    st.success('현상을 분석하는 소프트웨어 : 다양한 분야의 데이터 탐색.')
    st.success('모의 실험하는 소프트웨어 : 시뮬레이션 프로그램 활용.')
    st.success('가치를 창출하는 소프트웨어 : 스타트업 프로젝트에 적합한 소프트웨어 구현.')
    
    st.subheader("🖥️ 정보과학(진로선택) : 자료구조, 알고리즘, 프로그래밍, 정보과학 프로젝트 중심 학습으로 구성되어져 있고 특목고 학생들이 선택하는 과목! ")
    st.success('프로그래밍 : 효율적인 프로그래밍 구현.')
    st.success('데이터 구조 : 데이터들의 관계를 파악하고 특성에 맞도록 구조화.')
    st.success('알고리즘 : 문제를 효율적으로 해결하기 위한 적합한 알고리즘 설계.')
    st.success('정보과학 프로젝트 : 다양한 학문 분야의 문제를 컴퓨팅 관점에서 해결')

# 세 번째 탭 - 우리학교 소개 + FAQ
with tabs[2]:
    st.header("🏫 우리 학교 정보 수업은?")
    st.markdown("""
    <p style='font-size:1.05rem;'>
    최신 AI실에서 실습 중심으로 수업을 진행해요.<br>
    직접 코드를 작성해보고, 해커톤이나 로봇대회에 참여하기 위해 다양한 미션 수행 프로젝트를 경험해요.<br>
    정보 선생님께서도 학생들의 눈높이에 맞춰 쉽고 재미있게 가르쳐주셔서 수업 시간이 지루할 틈이 없답니다!
    </p>
    """, unsafe_allow_html=True)

    st.header("👩‍🎓 정보 / 인공지능 기초/ 파이썬 프로그래밍 수업을 수강한 선배들의 이야기")
    st.info("- 2학년 정OO 선배 : \"처음엔 코딩이 어렵게 느껴졌는데, 선생님이랑 친구들이랑 같이 하다 보니 금방 익숙해졌어요. 정보교과 덕분에 논리적으로 생각하는 힘이 길러진 것 같아요!\" ")
    st.info("- 2학년 이OO 선배 : \"저는 문과 성향인데도 정보교과 수업이 정말 재미있어요! 데이터를 분석해서 사회 현상을 이해하는 게 신기했고, 인공지능 기술이 우리 삶에 얼마나 큰 영향을 주는지 알게 됐어요.\" ")
    st.info("- 3학년 김OO 선배 : \"정보교과에서 배운 프로그래밍 덕분에 교내 IT 동아리 활동도 더 활발하게 할 수 있었고, 대학교 전공 선택에도 큰 도움이 됐어요. 미래에 어떤 직업을 갖든 정보 역량은 필수인 것 같아요\" ")

    st.header("❓ 정보교과에 대한 궁금증 (FAQ)")
    with st.expander("Q1. 코딩을 한 번도 안 해봤는데 괜찮을까요?"):
        st.success("네, 전혀 문제없어요! 정보교과는 코딩 경험이 없는 친구들도 기초부터 차근차근 배울 수 있도록 구성되어 있어요. 처음에는 조금 낯설 수 있지만, 꾸준히 따라오면 누구나 재미있게 배울 수 있답니다!")
    with st.expander("Q2. 수학을 잘 못하는데 정보교과를 따라갈 수 있을까요?"):
        st.success("정보교과에서 일부 수학적인 개념(예: 알고리즘의 효율성)이 나오기도 하지만, 고도의 수학 실력이 필수적인 것은 아니에요. 논리적으로 생각하고 문제를 해결하려는 의지가 더 중요하답니다! 필요한 수학 개념은 수업 시간에 충분히 설명해 줄 거예요.")
    with st.expander("Q3. 정보교과를 배우면 어떤 진로에 도움이 되나요?"):
        st.success("정보교과는 IT 분야(소프트웨어 개발자, 데이터 과학자, 인공지능 전문가 등)는 물론이고, 데이터를 다루거나 디지털 기술을 활용하는 거의 모든 분야의 진로에 도움이 돼요. 경영, 의료, 교육, 예술 등 어떤 분야를 선택하든 정보 활용 능력은 큰 강점이 될 거예요!")
    with st.expander("Q4. 정보교과 수업은 딱딱하고 재미없을 것 같아요."):
        st.success("전혀 그렇지 않아요! 정보교과는 이론만 배우는 게 아니라, 직접 코딩하고 결과물을 만들어보면서 성취감을 느낄 수 있는 활동적인 과목이에요. 친구들과 함께 프로젝트를 하거나 아이디어를 공유하면서 재미있게 배울 수 있답니다!")

# 네 번째 탭 - 진로 + 퀴즈 + 적성 + 의견
with tabs[3]:
    st.header("🖥️ 정보과와 연결된 진로/학과")
    st.markdown("""
    💡 <b>컴퓨터/소프트웨어 분야</b>: 개발자, 보안 전문가, 게임 프로그래머 등<br>
          <b> 관련학과 : 컴퓨터공학과, 소프트웨어학과, 정보통신공학과, 사이버보안학과 등<br><br>
    💡 <b>데이터/AI 분야</b>: 데이터 과학자, 데이터 분석가, 인공지능 개발자. 머신러닝 엔지니어, 빅데이터 전문가, AI 연구자 등<br>
          <b> 관련학과 : 데이터사이언스학과, 인공지능학과, 통계학과 (데이터 분석 트랙), 산업공학과 등<br><br>
    💡 <b>융합기술 분야</b>: 로봇공학, 스마트팜, 디지털 헬스케어, 에듀테크 개발자 등 <br>
          <b> 관련학과 : 로봇공학과, 바이오정보학과, 스마트시스템공학과, 미디어학과 (디지털 콘텐츠), 각 분야 + IT 융합 학과 등<br><br>
    """, unsafe_allow_html=True)

    quiz_questions = [
        {
            "question": "컴퓨터에게 일을 시키기 위해 사용하는 약속된 언어는?",
            "options": ["한국어", "영어", "프로그래밍 언어", "수학 언어"],
            "answer": "프로그래밍 언어",
            "explanation": "컴퓨터는 사람이 쓰는 언어를 이해하지 못하므로, 약속된 프로그래밍 언어를 사용해요."
        },
        {
            "question": "2022 개정 교육과정 정보교과의 5가지 영역이 아닌 것은 무엇일까요?",
            "options": ["컴퓨팅 시스템", "데이터", "알고리즘과 프로그래밍", "인공지능", "디자인"],
            "answer": "디자인",
            "explanation": "2022 개정 교육과정 정보교과의 5가지 영역은 컴퓨팅 시스템, 데이터, 알고리즘과 프로그래밍, 인공지능, 디지털 문화랍니다. 디자인은 직접적인 영역은 아니에요!"
        }
    ]
    display_quiz(quiz_questions)

    display_aptitude_test()

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
        망설이지 말고 정보교과의 문을 두드려보세요!<br>
        여러분의 멋진 도전을 항상 응원하겠습니다! 파이팅! 💪<br>
        </p>
    """, unsafe_allow_html=True)
