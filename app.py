import streamlit as st

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = "start"
if 'data' not in st.session_state:
    st.session_state.data = {"father": None, "mother": None, "brother": None, "user": None}

st.title("Family Game")

# Debugging info - can be removed later
st.write(f"Current Step: {st.session_state.step}")

if st.session_state.step == "start":
    st.write("Welcome to the game!")
    if st.button("Start"):
        st.session_state.step = "fan_question"
        st.rerun()

elif st.session_state.step == "fan_question":
    want_fan = st.radio("Do you want your father to hang on the fan?", ["Yes", "No"])
    if st.button("Next"):
        # Placeholder for data saving
        st.session_state.data["father"]