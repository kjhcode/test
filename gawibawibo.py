import streamlit as st
import random

def play_game(user_choice):
    """가위바위보 게임 로직을 실행하고 결과를 반환하는 함수"""
    choices = ["가위", "바위", "보"]
    computer_choice = random.choice(choices)

    st.write(f"나는 **{user_choice}**를 냈고, 컴퓨터는 **{computer_choice}**를 냈어!")

    if user_choice == computer_choice:
        st.subheader("🎉 비겼다! 다시 한 번 해볼까?")
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        st.balloons() # 이겼을 때 풍선 효과!
        st.subheader("🥳 야호! 네가 이겼어! 역시 대단해!")
    else:
        st.subheader("😢 아쉽다! 컴퓨터가 이겼어... 다음엔 꼭 이길 거야!")

st.title("✌️가위바위보 한판 해요!✌️")
st.markdown("---")

st.write("나랑 가위바위보 한판 할 준비 됐지?")

# 사용자의 선택을 받을 수 있는 라디오 버튼
user_select = st.radio(
    "자, 뭐 낼지 골라봐!",
    ["가위", "바위", "보"],
    index=0 # 기본 선택은 '가위'로!
)

# 게임 시작 버튼
if st.button("게임 시작!"):
    play_game(user_select)

st.markdown("---")
st.caption("새로운 게임을 하고 싶으면, 선택을 바꾸거나 페이지를 새로고침하면 돼!")
