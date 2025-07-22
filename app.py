import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 파일 로드
@st.cache_data
def load_data():
    df = pd.read_csv("202506_202506_연령별인구현황_월간_남녀구분.csv", encoding='cp949')
    return df

df = load_data()

# 서울 전체만 추출
seoul = df.iloc[0]

# 연령 컬럼 필터링
male_cols = [col for col in df.columns if "남_" in col and "세" in col]
female_cols = [col for col in df.columns if "여_" in col and "세" in col]

# 연령 추출
ages = [col.split('_')[-1].replace("세", "") for col in male_cols]
male_pop = seoul[male_cols].apply(lambda x: int(str(x).replace(",", "")))
female_pop = seoul[female_cols].apply(lambda x: int(str(x).replace(",", "")))

# 인구 피라미드 (여성은 음수 처리)
fig_pyramid = go.Figure()
fig_pyramid.add_trace(go.Bar(
    y=ages,
    x=male_pop,
    name="남성",
    orientation='h',
    marker_color='blue'
))
fig_pyramid.add_trace(go.Bar(
    y=ages,
    x=-female_pop,
    name="여성",
    orientation='h',
    marker_color='pink'
))
fig_pyramid.update_layout(
    title="서울특별시 인구 피라미드 (2025.06)",
    barmode='relative',
    xaxis=dict(title='인구수'),
    yaxis=dict(title='연령'),
    height=800
)

# 총인구 그래프
total_pop = male_pop + female_pop
fig_total = go.Figure()
fig_total.add_trace(go.Bar(
    x=ages,
    y=total_pop,
    name="총 인구",
    marker_color='gray'
))
fig_total.update_layout(
    title="서울특별시 연령별 총 인구수 (2025.06)",
    xaxis_title="연령",
    yaxis_title="인구수",
    height=500
)

# Streamlit UI
st.title("서울특별시 연령별 인구 분석 (2025.06)")
st.plotly_chart(fig_pyramid, use_container_width=True)
st.plotly_chart(fig_total, use_container_width=True)
