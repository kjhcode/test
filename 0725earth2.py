import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim # geopy에서 Nominatim을 불러와 주소->좌표 변환!
import time # 지오코딩 요청 간격을 두기 위해 (과도한 요청 방지)

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="나만의 북마크 지도 (주소로 찾기!)", layout="wide", initial_sidebar_state="expanded")

# --- 세션 상태 초기화 함수 ---
def init_session_state():
    if 'bookmarks' not in st.session_state:
        st.session_state.bookmarks = [
            # 광주광역시교육연구정보원 북마크 추가 (정확한 좌표로 수정!)
            {"name": "광주광역시교육연구정보원", 
             "latitude": 35.177595, # 정확한 위도
             "longitude": 126.846068, # 정확한 경도
             "description": "광주광역시 서구 치평동 1208에 위치! 공공학습관리시스템(LMS) 운영, AI 교육원 설립 추진 등 미래 교육을 선도하는 기관이에요! 🚀"},
            {"name": "남산타워", "latitude": 37.5512, "longitude": 126.9882, "description": "서울의 랜드마크! 경치 최고예요! 🗼"},
            {"name": "경복궁", "latitude": 37.5796, "longitude": 126.9770, "description": "조선 시대 왕궁, 한복 입고 구경하면 더 좋아요. 👑"},
            {"name": "해운대 해수욕장", "latitude": 35.1587, "longitude": 129.1601, "description": "부산의 대표 해변, 여름에 시원한 바닷바람! 🏖️"}
        ]
init_session_state()

st.title("🗺️ 나만의 즐겨찾기 지도 (주소로 콕! 찍기)")
st.markdown("이제 주소만 입력하면 지도가 알아서 찾아줄 거예요! 😊")

# 광주광역시교육연구정보원에 대한 추가 정보 표시
st.info(
    "💡 혹시 광주광역시교육연구정보원에 대해 아세요? "
    "광주 서구 치평동에 위치한 이곳은 공공학습관리시스템(LMS) 운영, 디지털 교수·학습 플랫폼 구축, "
    "AI 교육원 설립 추진 등 미래 교육을 위해 정말 힘쓰는 곳이랍니다!"
    "최근에는 중등 영재캠프도 운영하고 전국 최초로 교육행정데이터를 연동하기도 했어요.,"
)
st.markdown("---")


# --- 1. 북마크 추가하기 섹션 ---
st.header("📍 새로운 북마크 추가 (주소 입력)")

# geopy geolocator 초기화
# Nominatim은 OpenStreetMap 기반의 무료 지오코딩 서비스예요.
# user_agent는 서비스 이용 시 필요한 고유 식별자 같은 거예요.
geolocator = Nominatim(user_agent="my_map_bookmark_app")

# st.form을 사용해서 입력창을 그룹화하고, 제출 시 자동으로 입력 내용을 초기화할 수 있게 해!
with st.form("new_bookmark_form", clear_on_submit=True):
    name = st.text_input("✨ 장소 이름", placeholder="예: 우리 집, 단골 카페")
    address = st.text_input("🏠 주소 입력", placeholder="예: 서울특별시청, 광주광역시교육연구정보원, 부산 해운대구")
    description = st.text_area("📝 간단한 설명 (선택 사항)", placeholder="예: 분위기 좋고 커피가 맛있어요.")
    
    # 폼 제출 버튼
    add_button = st.form_submit_button("⭐ 북마크 추가!")

    if add_button: # 버튼이 눌렸을 때
        if name and address: # 이름과 주소가 모두 입력되었는지 확인!
            with st.spinner(f"'{address}' 주소를 지도에서 찾고 있어요..."): # 주소 찾을 때 로딩 스피너 표시
                try:
                    # Nominatim은 너무 많은 요청을 짧은 시간에 보내면 차단될 수 있으니, 약간의 시간 지연을 줘!
                    time.sleep(1) # 1초 대기
                    location = geolocator.geocode(address)
                    
                    if location:
                        new_bookmark = {
                            "name": name,
                            "latitude": location.latitude,
                            "longitude": location.longitude,
                            "description": description
                        }
                        st.session_state.bookmarks.append(new_bookmark) # 새 북마크를 목록에 추가!
                        st.success(f"'{name}'(이)가 지도에 추가되었어요! 멋져요! 👍")
                    else:
                        st.warning(f"죄송해요, '{address}' 주소를 찾을 수 없었어요. 주소를 더 정확하게 입력해 줄래요? 😥")
                except Exception as e:
                    st.error(f"주소 변환 중 오류가 발생했어요: {e} 다시 시도해 주세요. 😥")
        else:
            st.warning("장소 이름과 주소를 꼭 입력해야 해요. 😅")

st.markdown("---") # 구분선

# --- 2. 내 북마크 목록 (사이드바) ---
# 사이드바에 현재 저장된 북마크 목록을 보여줄 거야.
st.sidebar.header("📝 내 북마크 목록")
if st.session_state.bookmarks: # 북마크가 있을 때만 표시
    for i, bookmark in enumerate(st.session_state.bookmarks):
        # 숫자를 넷째 자리까지 표시하도록 수정
        st.sidebar.write(f"**{i+1}. {bookmark['name']}**")
        st.sidebar.write(f"   위도: {bookmark['latitude']:.6f}, 경도: {bookmark['longitude']:.6f}") # 소수점 자릿수 변경
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
    m = folium.Map(location=[first_bookmark['latitude'], first_bookmark['longitude']], zoom_start=14) # zoom_start를 14로 더 확대!

    # 각 북마크를 지도에 마커로 추가할 거야!
    for bookmark in st.session_state.bookmarks:
        # 마커를 클릭했을 때 나타날 팝업 내용을 HTML로 예쁘게 꾸밀 수 있어.
        popup_html = f"""
        <b>{bookmark['name']}</b><br>
        위도: {bookmark['latitude']:.6f}<br>
        경도: {bookmark['longitude']:.6f}<br>
        {bookmark['description']}
        """
        # 광주광역시교육연구정보원만 파란색 마커, 나머지는 빨간색 마커
        marker_color = "blue" if bookmark["name"] == "광주광역시교육연구정보원" else "red" 
        marker_icon = "book" if bookmark["name"] == "광주광역시교육연구정보원" else "map-marker" # 책 아이콘으로 변경!

        folium.Marker(
            location=[bookmark['latitude'], bookmark['longitude']], # 마커 위치
            popup=folium.Popup(popup_html, max_width=300), # 팝업 내용과 최대 너비
            tooltip=bookmark['name'], # 마우스를 올렸을 때 나타나는 텍스트
            icon=folium.Icon(color=marker_color, icon=marker_icon, prefix="fa") # 아이콘 색상, 모양, 스타일을 지정 (Font Awesome 사용)
        ).add_to(m) # 지도에 마커를 추가!
    
    # st_folium 함수를 사용해서 Folium 지도를 Streamlit 앱에 보여줘!
    # width와 height를 조절해서 지도 크기를 바꿀 수 있어.
    st_folium(m, width=800, height=500)
else:
    st.info("북마크를 추가하면 지도에 표시될 거예요. 빨리 나만의 지도를 만들어 봐! 🤗")

st.markdown("---")
st.caption("✨ Pygame은 복잡한 게임처럼 실시간 반응이 중요한 앱에, Streamlit은 이런 웹 대시보드나 간단한 앱 만들기에 아주 유용하답니다!")
