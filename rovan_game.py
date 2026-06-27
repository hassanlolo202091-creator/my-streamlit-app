import streamlit as st
from PIL import Image

st.title("مغامرة الأميرة روفان والأمير عمر 👸🤴")

# تهيئة الحالة
if 'step' not in st.session_state:
    st.session_state.step = 0

def show_img(filename):
    try:
        img = Image.open(f"images/{filename}")
        st.image(img, use_column_width=True)
    except:
        st.warning(f"الصورة {filename} غير موجودة")

# --- هيكل القصة ---

if st.session_state.step == 0:
    with st.form("step0"):
        name = st.text_input("What Is Your Name?")
        submitted = st.form_submit_button("التالي")
        if submitted and name.lower() == "rovan":
            st.session_state.step = 1
            st.rerun()

elif st.session_state.step == 1:
    show_img("rofy-princess.jpeg")
    with st.form("step1"):
        father = st.text_input("What Is Your Father Name?")
        submitted = st.form_submit_button("التالي")
        if submitted and father.lower() == "hassan":
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    show_img("hassan-king.jpeg")
    with st.form("step2"):
        mother = st.text_input("What Is Your Mother Name?")
        submitted = st.form_submit_button("التالي")
        if submitted and mother.lower() == "aliaa":
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    show_img("aliaa-queen.jpeg")
    with st.form("step3"):
        brother = st.text_input("What Is Your Brother Name?")
        submitted = st.form_submit_button("نبدأ الطعام")
        if submitted and brother.lower() == "omar":
            st.session_state.step = 4
            st.rerun()

elif st.session_state.step == 4:
    show_img("omar-prince.jpeg")
    st.write("الان سنتناول الطعام")
    with st.form("step4"):
        food_ans = st.text_input("ما معني كلمة الطعام بالانجليزيه ؟")
        submitted = st.form_submit_button("إلى الغابة")
        if submitted and food_ans.lower() == "food":
            st.session_state.step = 5
            st.rerun()

elif st.session_state.step == 5:
    show_img("family food 1.jpeg")
    st.write("الان وقت المغامرة سنذهب جميعا الي الغابة")
    show_img("junjle1.jpeg")
    st.write("عمر المشاغب جرى بعيدا!")
    with st.form("step5"):
        naughty = st.text_input("ما معني كلمة مشاغب باللغه الانجليزيه ؟")
        submitted = st.form_submit_button("إنقاذ عمر")
        if submitted and naughty.lower() == "naughty":
            st.session_state.step = 6
            st.rerun()

elif st.session_state.step == 6:
    show_img("omar.jpeg")
    st.write("قامت الغولة بخطفه! دور روفان الآن!")
    with st.form("step6"):
        head = st.text_input("ما معني كلمة رأس باللغه الانجليزيه ؟")
        ear = st.text_input("ما معني كلمة أذن باللغه الانجليزيه ؟")
        submitted = st.form_submit_button("استدعاء اليونيكورن")
        if submitted and head.lower() == "head" and ear.lower() == "ear":
            st.session_state.step = 7
            st.rerun()

elif st.session_state.step == 7:
    show_img("uni corne1.jpeg")
    with st.form("step7"):
        mouth = st.text_input("ما معني كلمة فم باللغه الانجليزيه ؟")
        nose = st.text_input("ما معني كلمة انف باللغه الانجليزيه ؟")
        submitted = st.form_submit_button("الذهاب لإنقاذ عمر")
        if submitted and mouth.lower() == "mouth" and nose.lower() == "nose":
            st.session_state.step = 8
            st.rerun()

elif st.session_state.step == 8:
    show_img("uni corne 2.jpeg")
    with st.form("step8"):
        eye = st.text_input("ما معني كلمة عين باللغه الانجليزيه ؟")
        hair = st.text_input("ما معني كلمة شعر باللغه الانجليزيه ؟")
        submitted = st.form_submit_button("العودة للقصر")
        if submitted and eye.lower() == "eye" and hair.lower() == "hair":
            st.session_state.step = 9
            st.rerun()

elif st.session_state.step == 9:
    show_img("uni corne 3.jpeg")
    st.write("تم الإنقاذ! روفان بطلة الأبطال.")
    show_img("reward2.jpeg")
    show_img("reward1.jpeg")
    if st.button("إعادة اللعب"):
        st.session_state.step = 0
        st.rerun()
