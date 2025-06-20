import streamlit as st

def display_aptitude_test():
    st.header("📚 정보교과 적성 간단 테스트")
    questions = [
        "새로운 기술이나 기기에 대해 배우는 것을 좋아한다.",
        "문제가 생겼을 때 원인을 분석하고 해결하는 과정을 즐긴다.",
        "복잡한 것을 단순하게 만들거나 순서대로 정리하는 것을 좋아한다.",
        "데이터나 숫자를 보고 의미를 파악하는 것에 흥미를 느낀다."
    ]

    for i, q in enumerate(questions):
        st.checkbox(q, key=f"aptitude_{i}")

    checked_count = sum(st.session_state.get(f"aptitude_{i}", False) for i in range(len(questions)))
    st.subheader("📚 테스트 결과")
    st.write(f"체크한 항목 수: **{checked_count}개**")

    if checked_count >= 3:
        st.balloons()
        st.markdown("🎉 정보교과에 매우 잘 맞는 성향이에요!")
    elif checked_count == 2:
        st.markdown("😊 정보교과에 대한 잠재력이 충분하네요!")
    else:
        st.markdown("🙂 아직 정보교과가 낯설 수 있지만, 배워보면 재미있을 수도 있어요!")
