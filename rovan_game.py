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
    name = st.text_input("What Is Your Name?")
    if name.lower() == "rovan":
        show_img("rofy-princess.jpeg")
        if st.button("التالي"):
            st.session_state.step = 1
            st.rerun()

elif st.session_state.step == 1:
    father = st.text_input("What Is Your Father Name?")
    if father.lower() == "hassan":
        show_img("hassan-king.jpeg")
        if st.button("التالي"):
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    mother = st.text_input("What Is Your Mother Name?")
    if mother.lower() == "aliaa":
        show_img("aliaa-queen.jpeg")
        if st.button("التالي"):
            st.session_state.step = 3
            st.rerun()

elif st.session_state.step == 3:
    brother = st.text_input("What Is Your Brother Name?")
    if brother.lower() == "omar":
        show_img("omar-prince.jpeg")
        if st.button("نبدأ الطعام"):
            st.session_state.step = 4
            st.rerun()

elif st.session_state.step == 4:
    st.write("الان سنتناول الطعام")
    food_ans = st.text_input("ما معني كلمة الطعام بالانجليزيه ؟")
    if food_ans.lower() == "food":
        show_img("family food 1.jpeg")
        if st.button("إلى الغابة"):
            st.session_state.step = 5
            st.rerun()

elif st.session_state.step == 5:
    st.write("الان وقت المغامرة سنذهب جميعا الي الغابة")
    show_img("junjle1.jpeg")
    st.write("عمر المشاغب جرى بعيدا!")
    naughty = st.text_input("ما معني كلمة مشاغب باللغه الانجليزيه ؟")
    if naughty.lower() == "naughty":
        show_img("omar.jpeg")
        st.write("قامت الغولة بخطفه!")
        if st.button("إنقاذ عمر"):
            st.session_state.step = 6
            st.rerun()

elif st.session_state.step == 6:
    st.write("دور روفان الآن!")
    head = st.text_input("ما معني كلمة رأس باللغه الانجليزيه ؟")
    ear = st.text_input("ما معني كلمة أذن باللغه الانجليزيه ؟")
    if head.lower() == "head" and ear.lower() == "ear":
        if st.button("استدعاء اليونيكورن"):
            st.session_state.step = 7
            st.rerun()

elif st.session_state.step == 7:
    show_img("uni corne1.jpeg")
    mouth = st.text_input("ما معني كلمة فم باللغه الانجليزيه ؟")
    nose = st.text_input("ما معني كلمة انف باللغه الانجليزيه ؟")
    if mouth.lower() == "mouth" and nose.lower() == "nose":
        if st.button("الذهاب لإنقاذ عمر"):
            st.session_state.step = 8
            st.rerun()

elif st.session_state.step == 8:
    show_img("uni corne 2.jpeg")
    eye = st.text_input("ما معني كلمة عين باللغه الانجليزيه ؟")
    hair = st.text_input("ما معني كلمة شعر باللغه الانجليزيه ؟")
    if eye.lower() == "eye" and hair.lower() == "hair":
        if st.button("العودة للقصر"):
            st.session_state.step = 9
            st.rerun()

elif st.session_state.step == 9:
    show_img("uni corne 3.jpeg")
    st.write("تم الإنقاذ! روفان بطلة الأبطال.")
    show_img("reward2.jpeg")
    st.write("تم الإنقاذ! روفان بطلة الأبطال.")
    show_img("reward1.jpeg")
    if st.button("إعادة اللعب"):
        st.session_state.step = 0
        st.rerun()
