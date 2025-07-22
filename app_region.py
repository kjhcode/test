import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("202506_202506_연령별인구현황_월간_남녀구분.csv", encoding="cp949")
    return df

df = load_data()

# 지역 선택
region_names = df["행정구역"].tolist()
selected_region = st.selectbox("지역 선택", region_names)

# 선택된 지역의 행 데이터
region_data = df[df["행정구역"] == selected_region].iloc[0]

# 연령 컬럼 필터링
male_cols = [col for col in df.columns if "남_" in col and "세" in col]
female_cols = [col for col in df.columns if "여_" in col and "세" in col]
ages = [col.split('_')[-1].replace("세", "") for col in male_cols]

# 인구 데이터 정제
male_pop = region_data[male_cols].apply(lambda x: int(str(x).replace(",", "")))
female_pop = region_data[female_cols].apply(lambda x: int(str(x).replace(",", "")))
total_pop = male_pop + female_pop
female_pop_negative = -female_pop

# 인구 피라미드
fig_pyramid = go.Figure()
fig_pyramid.add_trace(go.Bar(y=ages, x=male_pop, name="남성", orientation='h', marker_color='blue'))
fig_pyramid.add_trace(go.Bar(y=ages, x=female_pop_negative, name="여성", orientation='h', marker_color='pink'))
fig_pyramid.update_layout(
    title=f"{selected_region} 인구 피라미드 (2025년 6월)",
    barmode="relative",
    xaxis_title="인구수",
    yaxis_title="연령",
    height=800,
    template="plotly_white"
)

# 총 인구 막대 그래프
fig_total = go.Figure()
fig_total.add_trace(go.Bar(x=ages, y=total_pop, name="총 인구", marker_color="gray"))
fig_total.update_layout(
    title=f"{selected_region} 연령별 총 인구수 (2025년 6월)",
    xaxis_title="연령",
    yaxis_title="인구수",
    height=500,
    template="plotly_white"
)

# Streamlit UI
st.title("지역별 연령 인구 시각화 (2025년 6월 기준)")
st.subheader("1. 인구 피라미드 (Population Pyramid)")
st.plotly_chart(fig_pyramid, use_container_width=True)
st.subheader("2. 연령별 총 인구 막대 그래프")
st.plotly_chart(fig_total, use_container_width=True)