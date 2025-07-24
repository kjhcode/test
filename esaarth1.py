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

st.title("🗺️ 나만의 즐겨찾기 지도")
st.markdown("가고 싶은 곳, 추억의 장소를 나만의 지도에 콕! 저장해보세요. 😊")

# 광주광역시교육연구정보원에 대한 추가 정보 표시
st.info(
    "💡 혹시 광주광역시교육연구정보원에 대해 아세요? "
    "광주 서구 치평동에 위치한 이곳은 공공학습관리시스템(LMS) 
