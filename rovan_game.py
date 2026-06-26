import streamlit as st

# تعريف مراحل القصة في الـ session_state
if 'stage' not in st.session_state:
    st.session_state.stage = "start"

st.title("مغامرة روفان وعمر")

if st.session_state.stage == "start":
    name = st.text_input("What is your name?")
    if name.lower() == "rovan":
        if st.button("ابدئي المغامرة"):
            st.session_state.stage = "father_name"
            st.rerun()

elif st.session_state.stage == "father_name":
    father = st.text_input("What is your father name?")
    if father.lower() == "hassan":
        if st.button("التالي"):
            st.session_state.stage = "mother_name"
            st.rerun()
# وهكذا تكمل باقي المراحل...
