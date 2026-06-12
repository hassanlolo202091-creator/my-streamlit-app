import streamlit as st
from PIL import Image

st.set_page_config(page_title="Family Adventure", page_icon="👨‍👩‍👧‍👦")

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 'upload_photos'
    st.session_state.data = {}

# Page 1: Upload Photos
if st.session_state.step == 'upload_photos':
    st.header("Step 1: Meet the Family")
    f_img = st.file_uploader("Father's photo", type=['jpg', 'png', 'jpeg'])
    m_img = st.file_uploader("Mother's photo", type=['jpg', 'png', 'jpeg'])
    b_img = st.file_uploader("Brother's photo", type=['jpg', 'png', 'jpeg'])
    u_img = st.file_uploader("Your photo", type=['jpg', 'png', 'jpeg'])
    
    if st.button("Save & Start!"):
        if f_img and m_img and b_img and u_img:
            st.session_state.data = {"father": f_img, "mother": m_img, "brother": b_img, "user": u_img}
            st.session_state.step = 'part2_story'
            st.rerun()

# Page 2: Story
elif st.session_state.step == 'part2_story':
    st.header("The Adventure Begins!")
    transport = st.radio("How will your father come?", ["Plane", "Car", "Camel"], key="transport_choice")
    
    if st.button("See who is coming!"):
        if st.session_state.transport_choice == "Plane":
            try:
                father_img = Image.open(st.session_state.data['father']).convert("RGBA").resize((300, 300))
                plane_bg = Image.open("plane.jpeg").convert("RGBA")
                plane_bg.paste(father_img, (100, 100), father_img)
                st.image(plane_bg, caption="Father on the plane!")
            except:
                st.image(st.session_state.data['father'], caption="Father!")
        else:
            st.write(f"He is coming by {st.session_state.transport_choice}!")
            st.image(st.session_state.data['father'], caption="Father!")
        
        st.session_state.step = 'location_question'
        st.rerun()

# Page 3: Location
elif st.session_state.step == 'location_question':
    st.header("Where are we going?")
    loc = st.radio("Where do you want to go?", ["The Sea", "The Café", "The House"])
    if st.button("Go!"):
        st.session_state.step = 'brother_question'
        st.rerun()

# Page 4: Brother
elif st.session_state.step == 'brother_question':
    st.header("Brother's Status")
    is_naughty = st.radio("Is your brother naughty?", ["Yes", "No"])
    if st.button("Submit"):
        st.session_state.step = 'fan_question'
        st.rerun()

# Page 5: Fan
elif st.session_state.step == 'fan_question':
    st.header("The Final Plan")
    want_fan = st.radio("Do you want your father to hang him on the fan?", ["Yes", "No"])
    if st.button("Finish"):
        st.session_state.step = 'final_reveal'
        st.rerun()

# Page 6: Reveal
elif st.session_state.step == 'final_reveal':
    st.header("The End!")
    st.image([st.session_state.data['father'], st.session_state.data['mother'], 
              st.session_state.data['brother'], st.session_state.data['user']])
