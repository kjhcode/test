import streamlit as st

def display_quiz():
    st.header("📚 정보교과 상식 퀴즈!")
    quiz_questions = [
        {
            "question": "컴퓨터에게 일을 시키기 위해 사용하는 약속된 언어를 무엇이라고 할까요?",
            "options": ["한국어", "영어", "프로그래밍 언어", "수학 언어"],
            "answer": "프로그래밍 언어",
            "explanation": "컴퓨터는 사람이 쓰는 언어를 바로 이해하지 못해요. 프로그래밍 언어를 사용해서 명령을 내려야 해요."
        }
    ]

    for i, q in enumerate(quiz_questions):
        st.markdown(f"**문제 {i+1}.** {q['question']}")
        user_answer = st.radio(f"문제 {i+1} 정답 선택:", q['options'], key=f"quiz_{i}")
        if user_answer:
            if user_answer == q['answer']:
                st.success("🎉 정답입니다! 잘 알고 있네요! 👍")
            else:
                st.error(f"😅 아쉽지만 정답이 아니에요. 정답은 '{q['answer']}' 입니다.")
            st.info(f"**해설:** {q['explanation']}")
        st.markdown("---")
