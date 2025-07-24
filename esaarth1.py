import streamlit as st
import folium
from streamlit_folium import st_folium

# --- 페이지 기본 설정 ---
# 앱의 제목, 레이아웃, 사이드바 상태 등을 설정해줘!
st.set_page_config(page_title="나만의 북마크 지도", layout="wide", initial_sidebar_state="expanded")

# --- 세션 상태 초기화 함수 ---
# 앱이 새로고침되어도 북마크 목록이 사라지지 않도록 st.session_state에 저장할 거야.
# 'bookmarks'라는 리스트가 없으면 새로 만들고, 예시 북마크 몇 개를 추가해둬!
def init_session_state():
    if 'bookmarks' not in st.session_state:
        st.session_state.bookmarks = [
            # 광주광역시교육연구정보원 북마크 추가
            {"name": "광주광역시교육연구정보원", 
             "latitude": 35.1559, # 대략적인 위도
             "longitude": 126.8526, # 대략적인 경도
             "description": "공공학습관리시스템(LMS) 운영, AI 교육원 설립 추진 등 미래 교육을 선도하는 기관이에요! 🚀"},
            {"name": "남산타워", "latitude": 37.5512, "longitude": 126.9882, "description": "서울의 랜드마크! 경치 최고예요! 🗼"},
            {"name": "경복궁", "latitude": 37.5796, "longitude": 126.9770, "description": "조선 시대 왕궁, 한복 입고 구경하면 더 좋아요. 👑"},
            {"name": "해운대 해수욕장", "latitude": 35.1587, "longitude": 129.1601, "description": "부산의 대표 해변, 여름에 시원한 바닷바람! 🏖️"}
        ]
init_session_state()

st.title("🗺️ 나만의 즐겨찾기 지도")
st.markdown("가고 싶은 곳, 추억의 장소를 나만의 지도에 콕! 저장해보세요. 😊")

# 광주광역시교육연구정보원에 대한 추가 정보 표시
st.info(
    "💡 혹시 광주광역시교육연구정보원에 대해 아세요? "
    "여기는 공공학습관리시스템(LMS) 운영, 디지털 교수·학습 플랫폼 구축, "
    "AI 교육원 설립 추진 등 미래 교육을 위해 정말 힘쓰는 곳이랍니다! [【1】](https://geris.gen.go.kr/), [【9】](https://sites.google.com/gsuite.gen.go.kr/2021gwangjuai/%ED%99%88) "
    "최근에는 중등 영재캠프도 운영하고 전국 최초로 교육행정데이터를 연동하기도 했어요. [【2】](http://www.newsworker.co.kr/news/articleView.html?idxno=387759), [【4】](https://www.yna.co.kr/view/AKR20250527072900054)"
)
st.markdown("---")


# --- 1. 북마크 추가하기 섹션 ---
st.header("📍 새로운 북마크 추가")

# st.form을 사용해서 입력창을 그룹화하고, 제출 시 자동으로 입력 내용을 초기화할 수 있게 해!
with st.form("new_bookmark_form", clear_on_submit=True):
    name = st.text_input("✨ 장소 이름", placeholder="예: 우리 집, 단골 카페")
    # 위도와 경도는 소수점 자릿수를 맞춰서 보기 좋게!
    lat = st.number_input("⬆️ 위도", format="%.4f", value=37.5000, help="지도의 세로선 위치 (한국은 보통 33 ~ 38 사이)")
    lon = st.number_input("➡️ 경도", format="%.4f", value=127.0000, help="지도의 가로선 위치 (한국은 보통 126 ~ 129 사이)")
    description = st.text_area("📝 간단한 설명 (선택 사항)", placeholder="예: 분위기 좋고 커피가 맛있어요.")
    
    # 폼 제출 버튼
    add_button = st.form_submit_button("⭐ 북마크 추가!")

    if add_button: # 버튼이 눌렸을 때
        if name and lat is not None and lon is not None: # 이름, 위도, 경도가 모두 입력되었는지 확인!
            new_bookmark = {"name": name, "latitude": lat, "longitude": lon, "description": description}
            st.session_state.bookmarks.append(new_bookmark) # 새 북마크를 목록에 추가!
            st.success(f"'{name}'(이)가 지도에 추가되었어요! 멋져요! 👍")
        else:
            st.warning("장소 이름, 위도, 경도를 꼭 입력해야 해요. 😅")

st.markdown("---") # 구분선

# --- 2. 내 북마크 목록 (사이드바) ---
# 사이드바에 현재 저장된 북마크 목록을 보여줄 거야.
st.sidebar.header("📝 내 북마크 목록")
if st.session_state.bookmarks: # 북마크가 있을 때만 표시
    for i, bookmark in enumerate(st.session_state.bookmarks):
        st.sidebar.write(f"**{i+1}. {bookmark['name']}**")
        st.sidebar.write(f"   위도: {bookmark['latitude']:.4f}, 경도: {bookmark['longitude']:.4f}")
        if bookmark['description']: # 설명이 있으면 보여줘
            st.sidebar.caption(f"   설명: {bookmark['description']}")
        st.sidebar.markdown("---") # 각 북마크 사이에 구분선

    # 모든 북마크를 한 번에 지우는 버튼
    if st.sidebar.button("🧹 모든 북마크 지우기"):
        st.session_state.bookmarks = []
        st.experimental_rerun() # 앱을 새로고침해서 변경사항을 바로 반영!
else:
    st.sidebar.info("아직 북마크가 없어요. 위에 있는 '새로운 북마크 추가'에서 장소를 추가해보세요! 🚀")

# --- 3. 내 북마크 지도 표시 섹션 ---
st.header("🌍 내 즐겨찾기 지도")

if st.session_state.bookmarks: # 북마크가 있을 때만 지도 생성
    # 지도의 초기 중심점 설정: 첫 번째 북마크의 위치를 중심으로 잡아줘!
    first_bookmark = st.session_state.bookmarks[0]
    # 이제는 광주광역시교육연구정보원을 시작점으로 설정하여 앱을 열면 바로 해당 위치를 볼 수 있도록 해보자!
    m = folium.Map(location=[first_bookmark['latitude'], first_bookmark['longitude']], zoom_start=12) # 좀 더 확대!

    # 각 북마크를 지도에 마커로 추가할 거야!
    for bookmark in st.session_state.bookmarks:
        # 마커를 클릭했을 때 나타날 팝업 내용을 HTML로 예쁘게 꾸밀 수 있어.
        popup_html = f"""
        <b>{bookmark['name']}</b><br>
        위도: {bookmark['latitude']:.4f}<br>
        경도: {bookmark['longitude']:.4f}<br>
        {bookmark['description']}
        """
        marker_color = "blue" if bookmark["name"] == "광주광역시교육연구정보원" else "red" # 교육연구정보원만 파란색 마커!
        
        folium.Marker(
            location=[bookmark['latitude'], bookmark['longitude']], # 마커 위치
            popup=folium.Popup(popup_html, max_width=300), # 팝업 내용과 최대 너비
            tooltip=bookmark['name'], # 마우스를 올렸을 때 나타나는 텍스트
            icon=folium.Icon(color=marker_color, icon="info-sign", prefix="glyphicon") # 아이콘 색상, 모양, 스타일을 지정 (Font Awesome 사용)
        ).add_to(m) # 지도에 마커를 추가!
    
    # st_folium 함수를 사용해서 Folium 지도를 Streamlit 앱에 보여줘!
    # width와 height를 조절해서 지도 크기를 바꿀 수 있어.
    st_folium(m, width=800, height=500)
else:
    st.info("북마크를 추가하면 지도에 표시될 거예요. 빨리 나만의 지도를 만들어 봐! 🤗")

st.markdown("---")
st.caption("✨ Pygame은 복잡한 게임처럼 실시간 반응이 중요한 앱에, Streamlit은 이런 웹 대시보드나 간단한 앱 만들기에 아주 유용하답니다!")
