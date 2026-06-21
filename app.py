import random
import streamlit as st
# FIX: Imported the newly refactored logic_utils module to separate UI from game logic.
import logic_utils

# --- Page Setup ---
st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Logic has been moved to logic_utils.py.")

# --- Sidebar ---
st.sidebar.header("Settings")
difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Normal", "Hard"], index=1)

attempt_limit_map = {"Easy": 6, "Normal": 8, "Hard": 5}
attempt_limit = attempt_limit_map[difficulty]

# FIX: Delegated range generation to logic_utils.
low, high = logic_utils.get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# --- Initialize State ---
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
if "attempts" not in st.session_state:
    # FIX: Changed starting point to 0 using AI assistant to track attempts correctly.
    st.session_state.attempts = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "status" not in st.session_state:
    st.session_state.status = "playing"
if "history" not in st.session_state:
    st.session_state.history = []

# --- UI Components ---
st.subheader("Make a guess")
attempts_box = st.empty()

raw_guess = st.text_input("Enter your guess:", key=f"guess_input_{difficulty}")

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

# --- Logic Handlers ---
if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    # FIX: Added history reset and status updates for a functioning new game button using agent mode.
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    attempts_box.info(f"Attempts left: {max(0, attempt_limit - st.session_state.attempts)}")
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1
    # FIX: Handled user input parsing using the refactored logic_utils method.
    ok, guess_int, err = logic_utils.parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)
        
        # FIX: Removed erratic string-casting glitch (attempts % 2) and delegated to logic_utils using AI.
        outcome, message = logic_utils.check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = logic_utils.update_score(
            st.session_state.score, outcome, st.session_state.attempts
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(f"You won! The secret was {st.session_state.secret}. Final score: {st.session_state.score}")
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.error(f"Out of attempts! The secret was {st.session_state.secret}. Score: {st.session_state.score}")

attempts_box.info(f"Guess a number between {low} and {high}. Attempts left: {attempt_limit - st.session_state.attempts}")

with st.expander("Developer Debug Info", expanded=True):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("History:", st.session_state.history)

st.divider()