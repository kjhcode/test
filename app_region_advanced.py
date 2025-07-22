import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# CSV 업로드
st.title("지역별 연령 인구 시각화 (2025년 6월 기준)")
uploaded_file = st.file_uploader("📂 CSV 파일을 업로드하세요", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding="cp949")

    # 연령 컬럼 정리
    male_cols = [col for col in df.columns if "남_" in col and "세" in col]
    female_cols = [col for col in df.columns if "여_" in col and "세" in col]
    ages = [col.split('_')[-1].replace("세", "") for col in male_cols]

    # 지역 선택 (복수 선택 가능)
    selected_regions = st.multiselect("지역 선택", df["행정구역"].tolist(), default=[df["행정구역"].tolist()[0]])

    # 연령 필터
    min_age, max_age = st.slider("연령 범위 선택", 0, len(ages)-1, (0, len(ages)-1))
    filtered_ages = ages[min_age:max_age+1]
    filtered_male_cols = male_cols[min_age:max_age+1]
    filtered_female_cols = female_cols[min_age:max_age+1]

    # 비율 보기
    use_ratio = st.checkbox("비율(%)로 보기", value=False)

    for region in selected_regions:
        region_data = df[df["행정구역"] == region].iloc[0]

        male_pop = region_data[filtered_male_cols].apply(lambda x: int(str(x).replace(",", "")))
        female_pop = region_data[filtered_female_cols].apply(lambda x: int(str(x).replace(",", "")))
        total_pop = male_pop + female_pop
        female_pop_negative = -female_pop

        if use_ratio:
            region_total = total_pop.sum()
            male_pop = male_pop / region_total * 100
            female_pop = female_pop / region_total * 100
            total_pop = total_pop / region_total * 100
            female_pop_negative = -female_pop
            yaxis_title = "비율 (%)"
        else:
            yaxis_title = "인구수"

        # 인구 피라미드
        fig_pyramid = go.Figure()
        fig_pyramid.add_trace(go.Bar(
            y=filtered_ages,
            x=male_pop,
            name="남성",
            orientation='h',
            marker_color='blue'
        ))
        fig_pyramid.add_trace(go.Bar(
            y=filtered_ages,
            x=female_pop_negative,
            name="여성",
            orientation='h',
            marker_color='pink'
        ))
        fig_pyramid.update_layout(
            title=f"{region} 인구 피라미드 (2025년 6월)",
            barmode="relative",
            xaxis_title=yaxis_title,
            yaxis_title="연령",
            height=800,
            template="plotly_white"
        )

        # 총 인구 막대그래프
        fig_total = go.Figure()
        fig_total.add_trace(go.Bar(
            x=filtered_ages,
            y=total_pop,
            name="총 인구",
            marker_color="gray"
        ))
        fig_total.update_layout(
            title=f"{region} 연령별 총 인구수 (2025년 6월)",
            xaxis_title="연령",
            yaxis_title=yaxis_title,
            height=500,
            template="plotly_white"
        )

        # 출력
        st.subheader(f"📊 {region} 시각화")
        st.plotly_chart(fig_pyramid, use_container_width=True)
        st.plotly_chart(fig_total, use_container_width=True)
else:
    st.info("먼저 CSV 파일을 업로드하세요.")