
import streamlit as st

# 페이지 설정
st.set_page_config(layout="wide")

st.title("✨ 2022 개정 교육과정, 2학년 과목 선택 가이드 ✨")

st.write("""
안녕, 고등학교 1학년 친구들! 😊
이제 곧 2학년이 되면서 너희가 직접 배울 과목을 선택해야 할 시간이야.
고교학점제 아래에서는 너희의 흥미와 적성, 그리고 미래 진로에 맞춰 과목을 고르는 게 정말 중요해졌어.
어떤 과목을 선택해야 할지 막막하다면, 이 가이드가 조금이나마 도움이 되었으면 좋겠어!
""")

st.header("📚 고교학점제란 무엇일까?")
st.write("""
고교학점제는 대학처럼 학생들이 원하는 과목을 직접 선택해서 듣고,
필요한 학점을 채우면 졸업할 수 있는 제도야. [[2]](https://use.go.kr/component/file/ND_fileDownload.do?q_fileSn=786326&q_fileId=e36a31ba-8557-4ce8-b5ef-52217892487e)
이 제도를 통해 너희는 더 깊이 배우고 싶은 분야를 탐구하고,
미래 진로를 미리 경험해 볼 수 있어!
""")

st.header("🤔 과목 선택, 왜 중요할까?")
st.write("""
너희가 선택한 과목들은 단순히 배우는 내용을 넘어,
너희의 관심사, 강점, 그리고 앞으로 어떤 분야로 나아가고 싶은지를 보여주는 지표가 돼.
대학 입시에서도 너희의 과목 선택 이력이 중요하게 평가될 수 있으니 신중하게 선택하는 게 좋겠지?
""")

st.header("🗺️ 계열별 추천 과목 살펴보기")
st.write("""
크게 몇 가지 계열로 나눠서 관련 있는 과목들을 소개해 줄게.
물론 이건 추천일 뿐이고, 너희의 꿈에 따라 얼마든지 다르게 선택할 수 있어!
""")

# 계열별 정보 (예시)
# 실제 홍보물에는 더 자세하고 다양한 계열과 과목을 넣어야 해!
subject_data = {
    "인문사회 계열": {
        "설명": "사람과 사회, 문화에 대해 깊이 탐구하고 싶은 친구들에게 추천해!",
        "관련 과목 (예시)": ["문학", "사회문화", "윤리와 사상", "세계사", "경제"],
        "관련 진로/학과 (예시)": ["국어국문학과", "사회학과", "심리학과", "경영학과", "법학과"]
    },
    "자연과학 계열": {
        "설명": "자연 현상을 탐구하고 과학적 원리를 이해하는 데 흥미가 있다면?",
        "관련 과목 (예시)": ["물리학", "화학", "생명과학", "지구과학"], [[4]](https://home.pen.go.kr/hscredit/cm/cntnts/cntntsView.do?cntntsId=3729&mi=17411)
        "관련 진로/학과 (예시)": ["물리학과", "화학과", "생명과학과", "수학과"]
    },
    "공학 계열": {
        "설명": "새로운 기술을 개발하고 문제를 해결하는 것에 관심이 많다면 도전!",
        "관련 과목 (예시)": ["미적분", "기하", "물리학", "화학", "정보", "인공지능 기초", "데이터 과학"], [[4]](https://home.pen.go.kr/hscredit/cm/cntnts/cntntsView.do?cntntsId=3729&mi=17411)
        "관련 진로/학과 (예시)": ["컴퓨터공학과", "전자공학과", "기계공학과", "건축학과"]
    },
    "의약학 계열": {
        "설명": "사람이나 동물의 건강, 질병 치료에 기여하고 싶다면?",
        "관련 과목 (예시)": ["생명과학", "화학", "미적분", "확률과 통계"], [[1]](https://www.hscredit.kr/hsc/subject.do)
        "관련 진로/학과 (예시)": ["의예과", "치의예과", "한의예과", "수의예과", "약학과", "간호학과"] [[1]](https://www.hscredit.kr/hsc/subject.do)
    },
     "예술·체육 계열": {
        "설명": "음악, 미술, 체육 등 예체능 분야에 재능과 열정이 있다면!",
        "관련 과목 (예시)": ["음악", "미술", "체육", "음악 연주와 창작", "미술 창작", "스포츠 과학"], [[4]](https://home.pen.go.kr/hscredit/cm/cntnts/cntntsView.do?cntntsId=3729&mi=17411)
        "관련 진로/학과 (예시)": ["음악대학", "미술대학", "체육대학", "디자인학과"]
    }
}

for 계열, 정보 in subject_data.items():
    st.subheader(f"🌟 {계열}")
    st.write(정보["설명"])
    st.write(f"**추천 과목:** {', '.join(정보['관련 과목 (예시)'])}")
    st.write(f"**관련 진로/학과:** {', '.join(정보['관련 진로/학과 (예시)'])}")
    st.markdown("---") # 구분선

st.header("💡 과목 선택 TIP!")
st.write("""
1.  **나 자신을 탐색해 봐:** 내가 뭘 좋아하고 잘하는지, 어떤 분야에 관심 있는지 충분히 고민해 봐.
2.  **진로 정보를 찾아봐:** 희망하는 대학 학과나 직업에서 어떤 과목을 중요하게 생각하는지 알아보자. [[5]](https://www.jinhak.or.kr/subList/20000000271)
3.  **선생님, 선배님과 상담해 봐:** 혼자 고민하기 어렵다면 주변에 도움을 요청하는 것도 좋은 방법이야.
4.  **과목 내용을 미리 살펴보자:** 과목 이름만 보고 판단하기 어렵다면, 교육과정 정보나 교과서 목차 등을 미리 살펴보는 것도 좋아. [[10]](https://djehcredit.com/hscredit/bbs/view.php?table=sschool&page=2&field=&str=&sid=157&mno=1)
""")

st.header("🎉 너의 빛나는 미래를 응원해!")
st.write("""
과목 선택은 너의 성장을 위한 중요한 과정이야.
너무 어렵게 생각하지 말고, 너의 꿈을 향해 한 걸음 나아가는 즐거운 과정이라고 생각하면 좋겠어!
언제나 너의 도전을 응원할게! 파이팅! ❤️
""")

st.markdown("---")
st.write("이 가이드는 2022 개정 교육과정을 바탕으로 작성되었으며, 참고 자료는 다음과 같습니다.")
st.markdown("""
- [학생 진로·진학과 연계한 과목 선택 가이드 북 - 고교학점제](https://www.hscredit.kr/hsc/subject.do) [[1]](https://www.hscredit.kr/hsc/subject.do)
- [과목선택 워크북 - 울산광역시교육청](https://use.go.kr/component/file/ND_fileDownload.do?q_fileSn=786326&q_fileId=e36a31ba-8557-4ce8-b5ef-52217892487e) [[2]](https://use.go.kr/component/file/ND_fileDownload.do?q_fileSn=786326&q_fileId=e36a1ba-8557-4ce8-b5ef-52217892487e)
- [고교학점제 지원센터 - 과목 소개 - 2022개정 교육과정](https://home.pen.go.kr/hscredit/cm/cntnts/cntntsView.do?cntntsId=3729&mi=17411) [[4]](https://home.pen.go.kr/hscredit/cm/cntnts/cntntsView.do?cntntsId=3729&mi=17411)
- [2015/2022 개정 교육과정 선택과목 안내서 - 서울진로진학정보센터](https://www.jinhak.or.kr/subList/20000000271) [[5]](https://www.jinhak.or.kr/subList/20000000271)
- [2022 개정 교육과정 고등학교 선택과목 안내서(2025년 신입생부터)](https://djehcredit.com/hscredit/bbs/view.php?table=sschool&page=2&field=&str=&sid=157&mno=1) [[10]](https://djehcredit.com/hscredit/bbs/view.php?table=sschool&page=2&field=&str=&sid=157&mno=1)
""")
