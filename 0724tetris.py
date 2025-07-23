import streamlit as st
import time
import random

st.set_page_config(page_title="미니 테트리스 연습!", layout="centered")

# ----------------------------
# ✅ 세션 상태 초기화
# ----------------------------
def init_game_state():
    # 게임 보드 (10x20 빈 공간)
    st.session_state.board = [['.' for _ in range(10)] for _ in range(20)]
    st.session_state.current_piece = None # 현재 움직이는 블록
    st.session_state.piece_pos = (0, 4) # 블록의 시작 위치 (row, col)
    st.session_state.game_over = False
    st.session_state.score = 0

# 블록 생성 (아주 간단하게 I 블록 하나만!)
def create_new_piece():
    # 'I' 블록 (가로 4칸)
    return [(0,0), (0,1), (0,2), (0,3)] # 상대 좌표

# 보드에 블록 그리기/지우기
def draw_piece(board, piece, pos, char='X'):
    for r_offset, c_offset in piece:
        r, c = pos[0] + r_offset, pos[1] + c_offset
        if 0 <= r < len(board) and 0 <= c < len(board[0]):
            board[r][c] = char
    return board

# ----------------------------
# ✅ 게임 로직 (단순화된 이동)
# ----------------------------

# 보드 출력 함수
def render_board(board):
    st.markdown("```\n" + "\n".join([" ".join(row) for row in board]) + "\n```")

# 게임 시작/초기화
if 'board' not in st.session_state or st.session_state.game_over:
    init_game_state()
    st.session_state.current_piece = create_new_piece() # 새 게임 시작 시 첫 블록 생성
    st.session_state.game_over = False
    st.session_state.score = 0

st.title("👾 미니 테트리스 연습!")
st.markdown("블록이 움직이는 느낌만 살짝 맛보는 연습용 미니 게임이야! ✨")
st.write(f"현재 점수: **{st.session_state.score}**")

# 현재 블록 위치에서 보드 상태 업데이트
display_board = [row[:] for row in st.session_state.board] # 원본 보드 복사
if st.session_state.current_piece:
    display_board = draw_piece(display_board, st.session_state.current_piece, st.session_state.piece_pos)
render_board(display_board)


# ----------------------------
# ✅ 사용자 조작 버튼
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("⬅️ 왼쪽으로"):
        if not st.session_state.game_over:
            # 왼쪽으로 이동 가능한지 확인 (벽/다른 블록과 충돌 없는지 확인은 생략)
            st.session_state.piece_pos = (st.session_state.piece_pos[0], st.session_state.piece_pos[1] - 1)
            st.rerun()
with col2:
    if st.button("➡️ 오른쪽으로"):
        if not st.session_state.game_over:
            # 오른쪽으로 이동 가능한지 확인 (생략)
            st.session_state.piece_pos = (st.session_state.piece_pos[0], st.session_state.piece_pos[1] + 1)
            st.rerun()
with col3:
    if st.button("⬇️ 아래로 (한 칸)"):
        if not st.session_state.game_over:
            # 블록이 아래로 떨어질 수 있는지 확인 (충돌은 생략)
            st.session_state.piece_pos = (st.session_state.piece_pos[0] + 1, st.session_state.piece_pos[1])

            # 바닥에 닿았는지 아주 간단한 확인 (모든 블록 위치에 대한 검사는 생략)
            if st.session_state.piece_pos[0] >= 19 : # 보드 맨 아래에 닿았다고 가정
                st.write("블록이 바닥에 닿았어!")
                # 현재 블록을 보드에 고정
                st.session_state.board = draw_piece(st.session_state.board, st.session_state.current_piece, st.session_state.piece_pos)
                st.session_state.current_piece = create_new_piece() # 새 블록 생성
                st.session_state.piece_pos = (0, 4) # 새 블록 시작 위치

                # 라인 클리어 로직 (아주 간단하게!)
                cleared_lines = 0
                new_board = [['.' for _ in range(10)] for _ in range(20)]
                current_row_idx = 19
                for r in range(19, -1, -1):
                    if '.' not in st.session_state.board[r]: # 라인이 꽉 찼으면
                        cleared_lines += 1
                        st.session_state.score += 100 # 점수 추가
                    else:
                        new_board[current_row_idx] = st.session_state.board[r]
                        current_row_idx -= 1
                st.session_state.board = new_board
                if cleared_lines > 0:
                    st.success(f"🎉 {cleared_lines}줄을 지웠어! 축하해! 🎉")


            st.rerun()
with col4:
    if st.button("🔁 새 게임 시작"):
        init_game_state()
        st.session_state.current_piece = create_new_piece()
        st.rerun()

st.markdown("---")
st.info("이건 Streamlit으로 만드는 아주 단순화된 테트리스 개념 버전이야. 실제 게임처럼 만들려면 더 많은 코드가 필요해! 😉")
