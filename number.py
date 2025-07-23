import streamlit as st
import random

# 게임 초기화 함수 (새로운 게임 시작)
def init_game():
    st.session_state.secret_number = random.randint(1, 100) # 1부터 100 사이의 비밀 숫자
    st.session_state.guesses = 0 # 추측 횟수 초기화
    st.session_state.game_message = "숫자를 맞춰봐!" # 초기 메시지

# 앱의 메인 제목
st.title("🔢 숫자 맞추기 게임: 컴퓨터의 비밀을 파헤쳐라!")
st.markdown("---")

st.write("안녕! 나는 1부터 100 사이의 숫자 하나를 비밀로 가지고 있어.")
st.write("네가 그 숫자를 몇 번 만에 맞추는지 궁금한데? 😄")

# 세션 상태에 비밀 숫자가 없으면 게임 초기화
if 'secret_number' not in st.session_state:
    init_game()

# 게임 메시지 표시
st.write(st.session_state.game_message)

# 사용자 입력 받기
user_guess = st.number_input("네 생각은 어떤 숫자인데? (1-100 사이)", min_value=1, max_value=100, value=50, step=1)

# 추측 버튼
if st.button("추측하기!"):
    st.session_state.guesses += 1 # 추측 횟수 증가
    current_guess = int(user_guess)

    if current_guess < st.session_state.secret_number:
        st.session_state.game_message = "힝... 내가 생각한 숫자보다 **더 높아요!** ⬆️"
    elif current_guess > st.session_state.secret_number:
        st.session_state.game_message = "히히... 내가 생각한 숫자보다 **더 낮아요!** ⬇️"
    else:
        st.balloons() # 정답이면 풍선 축제!
        st.session_state.game_message = (
            f"🎉🎉 와아! 정답이야! 내 비밀 숫자는 바로 **{st.session_state.secret_number}**였어!\n"
            f"대단하다! **{st.session_state.guesses}**번 만에 맞췄네!"
        )
    st.rerun() # 메시지를 바로 업데이트하기 위해 페이지 새로고침

st.write(f"지금까지 **{st.session_state.guesses}**번 추측했어.")

# 게임 다시 시작 버튼
if st.button("새 게임 시작하기"):
    init_game()
    st.rerun() # 게임 초기화 후 페이지 새로고침

st.markdown("---")
st.caption("컴퓨터의 비밀을 파헤쳐 봐! 
