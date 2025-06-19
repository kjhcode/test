import streamlit as st
from PIL import Image  #Pillow 라이브러리 활용하기: 이미지를 Streamlit에 보여주기 전에 파이썬 코드에서 직접 이미지 크기를 조절하는 방법. Pillow라는 이미지 처리 라이브러리를 사용.

# 페이지 설정 - 이 부분이 가장 먼저 와야 해요!
st.set_page_config(layout="wide", page_title="정보과 안내", page_icon="💻") # 페이지 제목과 아이콘 추가

# --- CSS 스타일 추가 (글꼴 및 기타 디자인) ---
# Google Fonts에서 '고운돋움'체 불러오기
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

html, body, [class*="st-"] {
    font-family: 'Gowun Dodum', sans-serif;
}

/* 제목 스타일 (선택 사항) */
h1 {
    color: #4B088A; /* 보라색 계열 */
    text-align: center;
}

/* 헤더 스타일 (선택 사항) */
h2 { /* st.header()에 해당하는 h2 태그 스타일 */
    color: #800080; /* 자주색 계열 */
    margin-top: 3.5rem;
    font-size: 3.5rem; /* st.subheader() (h3)와 비슷하게 크기 조절 */
}

h3 { /* st.subheader()에 해당하는 h3 태그 스타일 */
    color: #800080; /* 자주색 계열 */
    margin-top: 2.0rem;
}

/* Expander 스타일 (선택 사항) */
.stExpander {
    border: 1px solid #DDA0DD; /* 연보라색 테두리 */
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
}

/* 버튼 스타일 (선택 사항) */
.stButton>button {
    background-color: #EE82EE; /* 연보색 배경 */
    color: white;
    border-radius: 5px;
}

</style>
""", unsafe_allow_html=True)
# ------------------------------------

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
- [2022 개정 교육과정/정보과 - 나무위키] [[8]](https://namu.wiki/w/2022%20개정%20교육과정/정보과)
- [2022 개정 교육과정 정보 살펴보기 - 네이버 블로그](https://m.blog.naver.com/math_rani/223294591331) [[4]](https://m.blog.naver.com/math_rani/223294591331)
- [과목선택 워크북 - 울산광역시교육청](https://use.go.kr/component/file/ND_fileDownload.do?q_fileSn=786326&q_fileId=e36a31ba-8557-4ce8-b5ef-52217892487e)
- [고교학점제 지원센터 - 과목 소개 - 2022개정 교육과정-부산광역시교육청고교학점제지원센터](https://home.pen.go.kr/hscredit/cm/cntnts/cntntsView.do?cntntsId=3729&mi=17411)
- [2015/2022 개정 교육과정 선택과목 안내서 - 서울진로진학정보센터](https://www.jinhak.or.kr/subList/20000000271)
- [2022 개정 교육과정 고등학교 선택과목 안내서 - 대전고교학점제지원센터 (2025년 신입생부터)](https://djehcredit.com/hscredit/bbs/view.php?table=sschool&page=2&field=&str=&sid=157&mno=1)
""")
# ------------------------------------

st.title("💻 미래를 코딩하다! 2022개정 교육과정의 고등학교 정보과 소개") # 제목 아이콘 유지

st.markdown("""
안녕, 친구들! 😊 <br>
2학년 과목 선택 때문에 고민이 많을 텐데요, <br>
여러분들이 수강을 희망한 과목을 살펴보니 <span style="color: red;">**정보**</span>/<span style="color: blue;">**프로그래밍**</span>/<span style="color: green;">**인공지능 기초**</span>/<span style="color: gold;">**빅데이터 분석**</span> 과목이더라구요!  <br> 
이 결과를 확인하고 우리 학생들이 인공지능 시대에 맞는 교과목을 알고 있다는 생각을 했습니다. <br> <br>

정보교과는 <br>
단순히 컴퓨터를 배우는 걸 넘어서, <br>
우리가 살아갈 미래 사회에서 꼭 필요한 <span style="color: red;">  생각하는 힘과 문제 해결 능력을 키워</span>주는 아주 중요한 과목입니다!<br>
왜 정보교과를 선택해야 하는지, <br>
같이 한번 알아볼까요?
""", unsafe_allow_html=True) # HTML 사용을 허용해야 해요!


st.header("📚 정보과목, 왜 중요할까?") # 헤더 아이콘 유지
st.markdown("""
<span style="font-size: 0.9em;">
우리가 사는 세상은 빠르게 변하고 있습니다. <br>
인공지능, 빅데이터, 자율주행... <br>
이 모든 것들이 '정보' 기술과 관련이 깊지요! <br>
정보교과를 배우면 이런 변화를 이해하고, 미래 사회의 주인공으로 성장하는 데 필요한 핵심 역량을 기를 수 있습니다.  <br> [[8]](https://namu.wiki/w/2022%20개정%20교육과정/정보과) <br> <br>
</span>
""", unsafe_allow_html=True) # HTML 사용을 허용해야 해요!


st.header("📚 정보과목을 선택하면 좋은 점!") # 헤더 아이콘 유지

# --- 장점 부분을 컬럼으로 나눠서 배치 ---
col1, col2 = st.columns(2) # 2개의 컬럼 생성

with col1:
    st.write("""
    -   **미래 사회 핵심 역량 강화:** AI, 데이터 분석 등 미래 유망 분야의 기초를 다질 수 있음. [[8]](https://namu.wiki/w/2022%20개정%20교육과정/정보과)
    -   **문제 해결 능력 향상:** 복잡한 문제를 논리적으로 분석하고 해결하는 힘을 기를 수 있음.
    -   **창의적인 아이디어 구현:** 코딩을 통해 나만의 아이디어를 실제로 만들어 볼 수 있음.
    -   **다양한 분야와의 연결:** 과학, 수학은 물론 인문, 예술 분야와도 융합하여 생각하는 능력을 키울 수 있음. [[4]](https://m.blog.naver.com/math_rani/223294591331)
    -   **진로 선택의 폭 확대:** IT, 데이터 과학자, AI 전문가 등 다양한 분야로 진출할 수 있는 발판을 마련할 수 있음. 
    """)
# --------------------------------------


st.header("📚 2022 고등학교 정보 과목은 이렇게 바뀝니다.") # 헤더 아이콘 유지
uploaded_file = st.file_uploader("이미지 파일을 선택해주세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # ✨ 여기! 업로드된 파일을 열어서 'image' 변수에 할당하는 과정이 꼭 필요해! ✨
        image = Image.open(uploaded_file)

        # 이제 'image' 변수에 이미지 객체가 들어있으니까 st.image()에 넘겨줄 수 있어!
        st.image(image, use_container_width=True) # 너비를 200픽셀로 설정

    except Exception as e:
        st.error(f"이미지를 처리하는 중 오류가 발생했어요: {e}")

else:
    st.info("이미지 파일을 업로드해주세요.")


st.markdown("""
<span style="font-size: 1.5em;">
-   정보 <br>
-   인공지능 기초 <br>
-   데이터 과학 <br>
-   소프트웨어와 생활 <br>     
</span>의 과목을 선택할 수 있도록 되어져있습니다..  <br>  <br> 

""", unsafe_allow_html=True) # HTML 사용을 허용해야 해요!


st.header("📚 정보(일반선택)과목에서 무엇을 배울까요? (2022 개정 교육과정 기준)") # 헤더 아이콘 유지
st.markdown("""
2022 개정 교육과정의 정보교과는 크게 5가지 영역으로 나뉘어 있습니다.. [[8]](https://namu.wiki/w/2022%20개정%20교육과정/정보과) <br>
이 영역들을 통해 <span style="color: red;">  컴퓨팅 사고력을 기르고 실생활 문제를 해결하는 방법 </span>을 배우게 될 것입니다!<br>
""", unsafe_allow_html=True) # HTML 사용을 허용해야 해요!
# 정보교과 5가지 영역 - 아이콘 변경
info_areas = {
    " <span style='font-size: 0.7em;'>💻 컴퓨팅 시스템</span>": "컴퓨터가 어떻게 작동하는지, 하드웨어와 소프트웨어의 기본 원리를 이해함.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>📈 데이터</span>": "다양한 데이터를 수집하고 분석해서 의미 있는 정보를 찾아내는 방법을 배움.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🧩 알고리즘과 프로그래밍 </span>": "문제를 해결하기 위한 절차(알고리즘)를 설계하고, 컴퓨터 언어(파이썬 등)로 프로그램을 만드는 연습을 함.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🤖 인공지능 </span>": "스스로 학습하고 판단하는 인공지능의 기본 개념과 활용 사례를 탐구함.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🌐 디지털 문화 </span>": "디지털 세상에서의 올바른 윤리 의식과 시민 역량을 기름." # 아이콘 크기 조절
}

# --- 컬럼을 활용하여 내용 배치 ---
cols = st.columns(len(info_areas)) # 영역 개수만큼 컬럼 생성
area_list = list(info_areas.items()) # 딕셔너리를 리스트로 변환하여 순서대로 접근

for i, col in enumerate(cols):
    area, description = area_list[i]
    with col: # 각 컬럼 안에 내용 넣기
        # subheader 대신 markdown ### 사용 및 unsafe_allow_html=True 추가
        st.markdown(f"### {area}", unsafe_allow_html=True)
        st.write(description)
#----------------------------------------------------------------------------------------------------------------------------------------
st.header("📚 인공지능 기초(진로선택) 과목에서 무엇을 배울까요? (2022 개정 교육과정 기준)") # 헤더 아이콘 유지
st.markdown("""
2022 개정 교육과정의 인공지능 기초 교과는 많은 내용 요소들이 중학교 정보와 고등학교 정보로 이동하였습니다. <br>
인식과 관련된 부분이 삭제되었고, ‘인공지능 프로젝트’ 단원이 신설되었습니다.<br>
이 영역들을 통해 <span style="color: red;"> 인공지능과 지속 가능 발전목표를 가지고 인공지능 문제 해결 절차 </span>를 배우게 될 것입니다!<br>
""", unsafe_allow_html=True) # HTML 사용을 허용해야 해요!
# 인공지능기초교과 4가지 영역 - 아이콘 변경
info_areas = {
    " <span style='font-size: 0.7em;'>💻 인공지능의 이해</span>": "인공지능의 원리, 인공지능과 탐색, 지식의 표현과 추론.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>📈 인공지능과 학습</span>": "기계학습과 데이터, 기계학습 알고리즘, 인공신경망과 딥러닝.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🧩 인공지능의 사회적 영향 </span>": "인공지능의 발전과 사회 변화, 인공지능과 진로, 인공지능과 윤리.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🌐 인공지능 프로젝트  </span>": "인공지능과 지속가능발전목표, 인공지능 문제 해결 절차.", # 아이콘 크기 조절
    
}

# --- 컬럼을 활용하여 내용 배치 ---
cols = st.columns(len(info_areas)) # 영역 개수만큼 컬럼 생성
area_list = list(info_areas.items()) # 딕셔너리를 리스트로 변환하여 순서대로 접근

for i, col in enumerate(cols):
    area, description = area_list[i]
    with col: # 각 컬럼 안에 내용 넣기
        # subheader 대신 markdown ### 사용 및 unsafe_allow_html=True 추가
        st.markdown(f"### {area}", unsafe_allow_html=True)
        st.write(description)

#----------------------------------------------------------------------------------------------------------------------------------------
st.header("📚 데이터 과학(진로선택)과목에서 무엇을 배울까요? (2022 개정 교육과정 기준)") # 헤더 아이콘 유지
st.markdown("""
2022 개정 교육과정의 데이터과학 교과는 기초적인 기계학습의 방법을 활용해 데이터를 분석하고 해석하는 데 초점을 맞추고 있습니다. <br>
이 영역들을 통해 <span style="color: red;"> 통계와 기계학습을 활용해 다양한 프로젝트를 해결하는 방법 </span>을 배우게 될 것입니다! <br>
""", unsafe_allow_html=True) # HTML 사용을 허용해야 해요!
# 데이터 과학 교과 4가지 영역 - 아이콘 변경
info_areas = {
    " <span style='font-size: 0.7em;'>💻 데이터 과학의 이해</span>": "데이터 기반 의사 결정의 중요성 인식.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>📈 데이터 준비과 분석</span>": "데이터 분석을 위한 데이터 수집, 전처리 과정. 데이터 분석에 효과적인 형태로 변환", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🧩 데이터 모델링과 평가 </span>": "데이터 모델의 개념. 분석을 위한 도구 탐색. 분석 결과 평가.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🌐 데이터 과학 프로젝트  </span>": "데이터 기반 문제 해결을 위한 데이터 과학의 기본 개념과 원리를 바탕으로 탐구 과정 수행.", # 아이콘 크기 조절
    
}

# --- 컬럼을 활용하여 내용 배치 ---
cols = st.columns(len(info_areas)) # 영역 개수만큼 컬럼 생성
area_list = list(info_areas.items()) # 딕셔너리를 리스트로 변환하여 순서대로 접근

for i, col in enumerate(cols):
    area, description = area_list[i]
    with col: # 각 컬럼 안에 내용 넣기
        # subheader 대신 markdown ### 사용 및 unsafe_allow_html=True 추가
        st.markdown(f"### {area}", unsafe_allow_html=True)
        st.write(description)

#----------------------------------------------------------------------------------------------------------------------------------------
st.header("📚 소프트웨어와 생활(융합선택)과목에서 무엇을 배울까요? (2022 개정 교육과정 기준)") # 헤더 아이콘 유지
st.markdown("""
2022개정 교육과정에서는 융합 선택 과목이 생겼으며 정보 교과에서는 소프트웨어와 생활 과목이 융합 선택에 해당합니다. <br>
이 영역들을 통해 <span style="color: red;"> 다양한 학문 분야와 융합으로 소프트웨어를 활용해 문제를 해결하는 프로젝트로 가치 창출을 경험 </span>을 배우게 될 것입니다!<br>
""", unsafe_allow_html=True) # HTML 사용을 허용해야 해요!
# 소프트웨어와 생활 교과 5가지 영역 - 아이콘 변경
info_areas = {
    " <span style='font-size: 0.7em;'>💻 세상을 변화 시키는 소프트웨어</span>": "소프트웨어를 통해 세상을 변화시키 사례 탐색.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>📈 작품을 창작하는 소프트웨어</span>": "피지컬 컴퓨팅 시스템의 구성 및 작동 원리 분석.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🧩 현상을 분석하는 소프트웨어</span>": "다양한 분야의 데이터 탐색.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🤖 모의 실험하는 소프트웨어</span>": "시뮬레이션 프로그램 활용.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🌐 가치를 창출하는 소프트웨어</span>": "스타트업 프로젝트에 적합한 소프트웨어 구현." # 아이콘 크기 조절
}

# --- 컬럼을 활용하여 내용 배치 ---
cols = st.columns(len(info_areas)) # 영역 개수만큼 컬럼 생성
area_list = list(info_areas.items()) # 딕셔너리를 리스트로 변환하여 순서대로 접근

for i, col in enumerate(cols):
    area, description = area_list[i]
    with col: # 각 컬럼 안에 내용 넣기
        # subheader 대신 markdown ### 사용 및 unsafe_allow_html=True 추가
        st.markdown(f"### {area}", unsafe_allow_html=True)
        st.write(description)


#----------------------------------------------------------------------------------------------------------------------------------------
st.header("📚 정보과학(진로선택)과목에서 무엇을 배울까요? (2022 개정 교육과정 기준)") # 헤더 아이콘 유지
st.markdown("""
이전 교육과정에서는 과학계열 전문교과1에 포함되어 있던 정보과학이 2022개정 교육과정에서는 정보 교과의 진로 선택 과목으로 포함되었습니다. <br>
2022개정 교육과정에서 정보과학의 내용 체계는 자료처리가 데이터 구조로 컴퓨팅 시스템 대신 정보과학 프로젝트가 포함되었습니다.<br>
이 영역들을 통해 <span style="color: red;"> 실생활에서 발생하는 문제와 다양한 학문 분야의 문제를 융합적으로 해결하기 위한 정보과학과 방법론을 습득하여 해결할 수 있는 능력 </span>을 배우게 될 것입니다!<br>
""", unsafe_allow_html=True) # HTML 사용을 허용해야 해요!
# 정보과학 교과 4가지 영역 - 아이콘 변경
info_areas = {
    " <span style='font-size: 0.7em;'>💻 프로그래밍</span>": "효율적인 프로그래밍 구현.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>📈 자료처리->데이터구조</span>": "데이터들의 관계를 파악하고 특성에 맞도록 구조화.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🧩 알고리즘 </span>": "문제를 효율적으로 해결하기 위한 적합한 알고리즘 설계.", # 아이콘 크기 조절
    " <span style='font-size: 0.7em;'>🌐 컴퓨팅 시스템->정보과학 프로젝트</span>": "다양한 학문 분야의 문제를 컴퓨팅 관점에서 해결.", # 아이콘 크기 조절
   
}

# --- 컬럼을 활용하여 내용 배치 ---
cols = st.columns(len(info_areas)) # 영역 개수만큼 컬럼 생성
area_list = list(info_areas.items()) # 딕셔너리를 리스트로 변환하여 순서대로 접근

for i, col in enumerate(cols):
    area, description = area_list[i]
    with col: # 각 컬럼 안에 내용 넣기
        # subheader 대신 markdown ### 사용 및 unsafe_allow_html=True 추가
        st.markdown(f"### {area}", unsafe_allow_html=True)
        st.write(description)


st.header("📚 우리 학교 정보교과 소개") # 헤더 아이콘 유지
st.markdown("""

우리 학교 정보교과 수업은  <br> 
이론과 실습의 균형을 맞춰 진행됩니다.  <br> 
최신 AI실에서 다양한 프로그래밍 언어를 배우고,  <br> 
직접 프로그램을 만들어보는 활동을 많이 합니다.

특히,해커톤과 로봇대회 및 데이터 분석 프로젝트 발표회 같은 교외/내 활동과 연계해서 배우는 내용을 더 깊이 탐구할 기회가 많아요.  <br> 
정보 선생님께서도 학생들의 눈높이에 맞춰 쉽고 재미있게 가르쳐주셔서 수업 시간이 지루할 틈이 없답니다!
""", unsafe_allow_html=True) # HTML 사용을 허용해야 해요!



st.header("📚 정보교과 선배들의 이야기") # 헤더 아이콘 유지
st.write("""
*   **김OO 선배 (2학년):** "처음엔 코딩이 어렵게 느껴졌는데, 선생님이랑 친구들이랑 같이 하다 보니 금방 익숙해졌어요. 정보교과 덕분에 논리적으로 생각하는 힘이 길러진 것 같아요!"
*   **이OO 선배 (2학년):** "저는 문과 성향인데도 정보교과 수업이 정말 재미있어요! 데이터를 분석해서 사회 현상을 이해하는 게 신기했고, 인공지능 기술이 우리 삶에 얼마나 큰 영향을 주는지 알게 됐어요."
*   **박OO 선배 (3학년):** "정보교과에서 배운 프로그래밍 덕분에 교내 IT 동아리 활동도 더 활발하게 할 수 있었고, 대학교 전공 선택에도 큰 도움이 됐어요. 미래에 어떤 직업을 갖든 정보 역량은 필수인 것 같아요!"
""")

st.header("📚 정보교과, 궁금한 점이 있나요? (FAQ)") # 헤더 아이콘 유지
st.write("정보교과 선택을 고민하는 친구들이 자주 묻는 질문들을 모아봤어요!")

# FAQ는 이미 expander를 사용하고 있어서 그대로 유지!
with st.expander("Q1. 코딩을 한 번도 안 해봤는데 괜찮을까요?"):
    st.markdown("""
    A. 네, 전혀 문제없어요! <br> 정보교과는 코딩 경험이 없는 친구들도 기초부터 차근차근 배울 수 있도록 구성되어 있어요. <br>처음에는 조금 낯설 수 있지만, 꾸준히 따라오면 누구나 재미있게 배울 수 있답니다!
    """, unsafe_allow_html=True)

with st.expander("Q2. 수학을 잘 못하는데 정보교과를 따라갈 수 있을까요?"):
    st.markdown("""
    A. 정보교과에서 일부 수학적인 개념(예: 알고리즘의 효율성)이 나오기도 하지만, <br>고도의 수학 실력이 필수적인 것은 아니에요. <br>논리적으로 생각하고 문제를 해결하려는 의지가 더 중요하답니다! <br>필요한 수학 개념은 수업 시간에 충분히 설명해 줄 거예요.
    """, unsafe_allow_html=True)

with st.expander("Q3. 정보교과를 배우면 어떤 진로에 도움이 되나요?"):
    st.markdown("""
    A. 정보교과는 IT 분야(소프트웨어 개발자, 데이터 과학자, 인공지능 전문가 등)는 물론이고, <br>데이터를 다루거나 디지털 기술을 활용하는 거의 모든 분야의 진로에 도움이 돼요. <br>경영, 의료, 교육, 예술 등 어떤 분야를 선택하든 정보 활용 능력은 큰 강점이 될 거예요! <br> (아래 '관련 진로/학과 심화' 섹션을 참고해 주세요!)
    """, unsafe_allow_html=True)

with st.expander("Q4. 정보교과 수업은 딱딱하고 재미없을 것 같아요."):
    st.markdown("""
    A. 전혀 그렇지 않아요! <br> 정보교과는 이론만 배우는 게 아니라, <br> 직접 코딩하고 결과물을 만들어보면서 성취감을 느낄 수 있는 활동적인 과목이에요. <br>친구들과 함께 프로젝트를 하거나 아이디어를 공유하면서 재미있게 배울 수 있답니다!
    """, unsafe_allow_html=True)

st.header("📚 정보교과와 연결된 미래 (진로/학과)") # 헤더 아이콘 유지
st.write("""
정보교과에서 배우는 내용들은 미래 사회의 다양한 분야와 깊이 연결되어 있어요.
정보교과를 통해 탐색해 볼 수 있는 몇 가지 진로 및 학과를 좀 더 자세히 알아볼까요?
""")

# 진로/학과 데이터 - 아이콘 변경
st.header("📚 정보교과와 연결된 미래 (진로/학과)") # 헤더 아이콘 유지
st.write("""
정보교과에서 배우는 내용들은 미래 사회의 다양한 분야와 깊이 연결되어 있어요.
정보교과를 통해 탐색해 볼 수 있는 몇 가지 진로 및 학과를 좀 더 자세히 알아볼까요?
""")

# 진로/학과 데이터 - 아이콘 변경
# ✨ 딕셔너리 정의 안에서는 딱 '키: 값' 형태로만! ✨
career_data = {
    "<span style='font-size: 1.2em;'>💻 컴퓨터/소프트웨어 분야": { # 이 문자열 자체가 키가 되는 거야!
        "설명": "컴퓨터 시스템을 이해하고 소프트웨어를 개발하는 분야예요. 우리가 사용하는 앱, 웹사이트, 게임 등이 모두 이 분야의 결과물이죠.",
        "관련 직업 (예시)": ["소프트웨어 개발자", "웹 개발자", "앱 개발자", "게임 프로그래머", "정보 보안 전문가"],
        "관련 학과 (예시)": ["컴퓨터공학과", "소프트웨어학과", "정보통신공학과", "사이버보안학과"]
    },
    "<span style='font-size: 0.7em;'>🧠 데이터/AI 분야": {
        "설명": "방대한 데이터를 수집, 분석하고 인공지능 기술을 개발하거나 활용하는 분야예요. 미래 사회에서 가장 중요해질 분야 중 하나죠.",
        "관련 직업 (예시)": ["데이터 과학자", "데이터 분석가", "인공지능 개발자", "머신러닝 엔지니어", "빅데이터 전문가"],
        "관련 학과 (예시)": ["데이터사이언스학과", "인공지능학과", "통계학과 (데이터 분석 트랙)", "산업공학과"]
    },
    "<span style='font-size: 0.7em;'>🔗 융합 기술 분야": {
        "설명": "정보 기술을 다른 분야와 결합하여 새로운 가치를 창출하는 분야예요. 정보교과의 융합적 사고력이 빛을 발하는 곳이죠!",
        "관련 직업 (예시)": ["로봇 공학자", "스마트팜 전문가", "디지털 헬스케어 개발자", "핀테크 전문가", "에듀테크 개발자"],
        "관련 학과 (예시)": ["로봇공학과", "바이오정보학과", "스마트시스템공학과", "미디어학과 (디지털 콘텐츠)", "각 분야 + IT 융합 학과"]
    }
}

# ✨ 딕셔너리를 다 만든 다음에, 이 내용을 화면에 보여줄 때 st.markdown()을 사용하는 거야! ✨
# 예를 들어, 각 분야의 제목(키)을 화면에 보여주고 싶다면 이렇게 반복문을 쓸 수 있어.
for career_area, details in career_data.items():
    st.markdown(career_area, unsafe_allow_html=True) # 키(HTML 포함 문자열)를 마크다운으로 보여주기
    st.write(details["설명"]) # 설명 보여주기
    st.write("관련 직업 (예시):", ", ".join(details["관련 직업 (예시)"])) # 직업 목록 보여주기
    st.write("관련 학과 (예시):", ", ".join(details["관련 학과 (예시)"])) # 학과 목록 보여주기
    st.write("---") # 구분선 넣기











'''career_data = {
    my_text = "<span style='font-size: 0.7em;'>💻 컴퓨터/소프트웨어 분야"
    st.markdown(my_text, unsafe_allow_html=True)
    "<span style='font-size: 0.7em;'>💻 컴퓨터/소프트웨어 분야": { # 아이콘 변경
        "설명": "컴퓨터 시스템을 이해하고 소프트웨어를 개발하는 분야예요. 우리가 사용하는 앱, 웹사이트, 게임 등이 모두 이 분야의 결과물이죠.",
        "관련 직업 (예시)": ["소프트웨어 개발자", "웹 개발자", "앱 개발자", "게임 프로그래머", "정보 보안 전문가"],
        "관련 학과 (예시)": ["컴퓨터공학과", "소프트웨어학과", "정보통신공학과", "사이버보안학과"]
    },
    "<span style='font-size: 0.7em;'>🧠 데이터/AI 분야": { # 아이콘 유지
        "설명": "방대한 데이터를 수집, 분석하고 인공지능 기술을 개발하거나 활용하는 분야예요. 미래 사회에서 가장 중요해질 분야 중 하나죠.",
        "관련 직업 (예시)": ["데이터 과학자", "데이터 분석가", "인공지능 개발자", "머신러닝 엔지니어", "빅데이터 전문가"],
        "관련 학과 (예시)": ["데이터사이언스학과", "인공지능학과", "통계학과 (데이터 분석 트랙)", "산업공학과"]
    },
    "<span style='font-size: 0.7em;'>🔗 융합 기술 분야": { # 아이콘 유지
        "설명": "정보 기술을 다른 분야와 결합하여 새로운 가치를 창출하는 분야예요. 정보교과의 융합적 사고력이 빛을 발하는 곳이죠!",
        "관련 직업 (예시)": ["로봇 공학자", "스마트팜 전문가", "디지털 헬스케어 개발자", "핀테크 전문가", "에듀테크 개발자"],
        "관련 학과 (예시)": ["로봇공학과", "바이오정보학과", "스마트시스템공학과", "미디어학과 (디지털 콘텐츠)", "각 분야 + IT 융합 학과"]
    }
}

# --- 진로/학과 부분을 컬럼으로 나눠서 배치 ---
career_cols = st.columns(len(career_data)) # 진로 분야 개수만큼 컬럼 생성
career_list = list(career_data.items()) # 딕셔너리를 리스트로 변환

for i, col in enumerate(career_cols):
    field, info = career_list[i]
    with col: # 각 컬럼 안에 내용 넣기
        st.subheader(f"{field}")
        st.write(info["설명"])
        st.write(f"**주요 직업:** {', '.join(info['관련 직업 (예시)'])}")
        st.write(f"**관련 학과:** {', '.join(info['관련 학과 (예시)'])}")
# -------------------------------------------'''

# --- 인터랙티브 요소 섹션 추가 ---
st.header("📚 정보교과와 친해지기! (간단 퀴즈 & 적성 테스트)")

st.subheader("💻 정보교과 상식 퀴즈!") # 헤더 아이콘 유지
st.write("정보교과에 대해 얼마나 알고 있는지 간단한 퀴즈로 확인해 볼까요?")

# 퀴즈 문제와 정답, 해설
quiz_questions = [
    {
        "question": "컴퓨터에게 일을 시키기 위해 사용하는 약속된 언어를 무엇이라고 할까요?",
        "options": ["한국어", "영어", "프로그래밍 언어", "수학 언어"],
        "answer": "프로그래밍 언어",
        "explanation": "컴퓨터는 사람이 쓰는 언어를 바로 이해하지 못해요. 그래서 컴퓨터가 이해할 수 있는 약속된 언어인 프로그래밍 언어를 사용해서 명령을 내린답니다!"
    },
    {
        "question": "2022 개정 교육과정 정보교과의 5가지 영역이 아닌 것은 무엇일까요?",
        "options": ["컴퓨팅 시스템", "데이터", "알고리즘과 프로그래밍", "인공지능", "디자인"],
        "answer": "디자인",
        "explanation": "2022 개정 교육과정 정보교과의 5가지 영역은 컴퓨팅 시스템, 데이터, 알고리즘과 프로그래밍, 인공지능, 디지털 문화랍니다. 디자인은 직접적인 영역은 아니에요!"
    }
    # 퀴즈 문제를 더 추가할 수 있어요!
]

# 퀴즈 풀이
for i, q in enumerate(quiz_questions):
    st.markdown(f"**문제 {i+1}.** {q['question']}")
    user_answer = st.radio(f"문제 {i+1} 정답 선택:", q['options'], key=f"quiz_{i}")

    # 정답 확인 버튼 (선택 사항)
    # if st.button(f"문제 {i+1} 정답 확인", key=f"check_{i}"):
    if user_answer: # 사용자가 답을 선택하면 바로 피드백
        if user_answer == q['answer']:
            st.success("🎉 정답입니다! 잘 알고 있네요! 👍")
        else:
            st.error(f"😅 아쉽지만 정답이 아니에요. 정답은 '{q['answer']}' 입니다.")
        st.info(f"**해설:** {q['explanation']}")
    st.markdown("---")

st.subheader("📚 정보교과 적성 간단 테스트") # 헤더 아이콘 유지
st.write("아래 질문들을 읽고 나에게 해당하는 항목에 체크해 보세요! 정보교과가 너에게 잘 맞을지 살짝 엿볼 수 있을 거예요!")

# 적성 테스트 질문
aptitude_questions = [
    "새로운 기술이나 기기에 대해 배우는 것을 좋아한다.",
    "문제가 생겼을 때 원인을 분석하고 해결하는 과정을 즐긴다.",
    "복잡한 것을 단순하게 만들거나 순서대로 정리하는 것을 좋아한다.",
    "데이터나 숫자를 보고 의미를 파악하는 것에 흥미를 느낀다.",
    "나만의 아이디어를 실제로 만들어보고 싶다는 생각을 해본 적이 있다.",
    "컴퓨터나 스마트폰을 사용하는 것 외에 내부 작동 방식이 궁금하다.",
    "미래 사회의 변화나 인공지능 기술 발전에 관심이 많다.",
    "친구들과 함께 머리를 맞대고 문제를 해결하는 것을 좋아한다."
]

# --- Session state initialization for aptitude test ---
# Initialize session state for each checkbox BEFORE creating them
for i in range(len(aptitude_questions)):
    if f"aptitude_{i}" not in st.session_state:
        st.session_state[f"aptitude_{i}"] = False
# ----------------------------------------------------

# 체크박스로 질문 표시 및 응답 받기
st.markdown("---")
st.markdown("**나에게 해당하는 항목에 체크해주세요!**")
st.markdown("---")

checked_count = 0
for i, question in enumerate(aptitude_questions):
    col_apt, col_q = st.columns([0.1, 0.9])
    with col_apt:
        # Create the checkbox, linking it to the session state key
        # The positional argument "" is sufficient for an empty label
        st.checkbox("", key=f"aptitude_{i}")

    with col_q:
        st.write(question) # Display the question text

    # Read the state directly from session_state to count checked items
    if st.session_state[f"aptitude_{i}"] :
        checked_count += 1

st.markdown("---")

# 결과 보여주기
st.subheader("📚 테스트 결과") # 헤더 아이콘 유지
st.write(f"체크한 항목 수: **{checked_count}개**")

if checked_count >= 6:
    st.balloons() # 풍선 효과!
    st.markdown("""
        "🎉 와우! 정보교과에 대한 흥미와 적성이 아주 높은 편이네요! <br>정보교과를 선택하면 정말 재미있게 배우고 큰 성장을 할 수 있을 거예요!<br> 미래 IT 전문가의 꿈을 키워보는 건 어떨까요?")
        """, unsafe_allow_html=True)
elif checked_count >= 4:
    st.markdown("""
    😊 정보교과에 대한 잠재력과 흥미가 충분하네요! <br>조금만 더 관심을 가지고 노력하면 정보교과에서 좋은 결과를 얻을 수 있을 거예요. <br>한번 도전해 보는 것을 추천해요!")
    """, unsafe_allow_html=True)
elif checked_count >= 2:
    st.markdown("""
        🙂 아직 정보교과가 낯설 수 있지만, 몇 가지 항목에 해당하는 것을 보니 관심 가질 만한 부분이 있네요! <br>정보교과 수업을 통해 새로운 재미를 발견할 수도 있어요. <br>너무 어렵게 생각하지 말고 열린 마음으로 다가가 보세요!")
        """, unsafe_allow_html=True)
else:
    st.markdown("""
    😅 아직 정보교과에 대해 잘 모르거나 크게 흥미를 느끼지 못할 수도 있어요. <br>하지만 정보교과는 미래 사회에 꼭 필요한 과목이니, 이 가이드를 통해 조금 더 알아보는 건 어떨까요? <br>생각보다 재미있을 수도 있답니다!")
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("📚 홍보물에 대한 의견 남기기") # 헤더 아이콘 유지
st.write("이 홍보물에 대해 궁금한 점이나 의견이 있다면 자유롭게 남겨주세요! (남겨주신 의견은 저장되지 않습니다.)")

# --- 댓글 입력창 (저장 기능 없음) ---
user_comment = st.text_area("여기에 의견을 입력하세요:", height=100)
if st.button("의견 제출"):
    if user_comment:
        st.success("의견이 제출되었습니다! 소중한 의견 감사합니다! 😊")
        # 참고: 여기에 입력된 의견은 새로고침하면 사라져요.
        # 의견을 저장하고 다른 사람들에게 보여주려면 데이터베이스 연동이 필요해요!
        # 예: Google Sheets, Firebase, 또는 간단한 파일 저장 등
    else:
        st.warning("의견을 입력해주세요!")
# ------------------------------------
st.markdown("---")


st.header("📚 여러분의 빛나는 미래를 응원해! ❤️") # 헤더 아이콘 유지
st.markdown("""
정보교과는  <br> 
여러분의 잠재력을 깨우고 미래를 설계하는 데 훌륭한 도구가 될 것입니다. <br>
망설이지 말고 정보교과의 문을 두드려보세요! <br>
여러분의 멋진 도전을 응원하겠습니다! 파이팅! 😊
""", unsafe_allow_html=True)

st.markdown("---")
# 참고 자료는 이제 사이드바에 있으니 본문에서는 간단히 언급만 해도 돼.
# st.write("이 가이드에 사용된 참고 자료는 왼쪽 사이드바에서 확인하실 수 있습니다.")
