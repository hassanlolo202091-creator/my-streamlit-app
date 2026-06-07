import streamlit as st
from PIL import Image

st.set_page_config(page_title="Family Adventure", page_icon="👨‍👩‍👧‍👦")

if 'step' not in st.session_state:
    st.session_state.step = 'upload_photos'
    st.session_state.data = {}

if st.session_state.step == 'upload_photos':
    st.header("Step 1: Meet the Family")
    f_name = st.text_input("Father's name?")
    f_img = st.file_uploader("Father's photo", type=['jpg', 'png'])
    m_name = st.text_input("Mother's name?")
    m_img = st.file_uploader("Mother's photo", type=['jpg', 'png'])
    b_name = st.text_input("Brother's name?")
    b_img = st.file_uploader("Brother's photo", type=['jpg', 'png'])
    u_name = st.text_input("Your name?")
    u_img = st.file_uploader("Your photo", type=['jpg', 'png'])
    
    if st.button("Save & Start!"):
        if f_img and m_img and b_img and u_img:
            st.session_state.data = {"father": f_img, "mother": m_img, "brother": b_img, "user": u_img}
            st.session_state.step = 'part2_story'
            st.rerun()

elif st.session_state.step == 'part2_story':
    st.header("The Adventure Begins!")
    transport = st.radio("How will your father come?", ["Plane", "Car", "Camel"])
    if st.button("See who is coming!"):
        st.write(f"He is coming by {transport}!")
        st.image(st.session_state.data['father'])
        st.session_state.step = 'location_question'

elif st.session_state.step == 'location_question':
    loc = st.radio("Where do you want to go?", ["The Sea", "The Café", "The House"])
    if st.button("Go!"):
        st.session_state.step = 'brother_question'
        st.rerun()

elif st.session_state.step == 'brother_question':
    is_naughty = st.radio("Is your brother naughty?", ["Yes", "No"])
    if st.button("Submit"):
        st.session_state.step = 'fan_question'
        st.rerun()

elif st.session_state.step == 'fan_question':
    want_fan = st.radio("Do you want your father to hang him on the fan?", ["Yes", "No"])
    if st.button("Finish"):
        st.session_state.step = 'final_reveal'
        st.rerun()

elif st.session_state.step == 'final_reveal':
    st.header("The End!")
    st.image([st.session_state.data['father'], st.session_state.data['mother'], 
              st.session_state.data['brother'], st.session_state.data['user']])