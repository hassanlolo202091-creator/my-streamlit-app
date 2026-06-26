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

# --- مراحل القصة ---

if st.session_state.step == 0:
    name = st.text_input("What Is Your Name?")
    if st.button("تأكيد الاسم"):
        if name.lower() == "rovan":
            st.session_state.step = 1
            st.rerun()
        else:
            st.error("الاسم غير صحيح، حاولي مجدداً")

elif st.session_state.step == 1:
    show_img("rofy-princess.jpeg")
    father = st.text_input("What Is Your Father Name?")
    if st.button("تأكيد اسم الأب"):
        if father.lower() == "hassan":
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("اسم الأب غير صحيح")

elif st.session_state.step == 2:
    show_img("hassan-king.jpeg")
    mother = st.text_input("What Is Your Mother Name?")
    if st.button("تأكيد اسم الأم"):
        if mother.lower() == "aliaa":
            st.session_state.step = 3
            st.rerun()
        else:
            st.error("اسم الأم غير صحيح")

elif st.session_state.step == 3:
    show_img("aliaa-queen.jpeg")
    brother = st.text_input("What Is Your Brother Name?")
    if st.button("تأكيد اسم الأخ"):
        if brother.lower() == "omar":
            st.session_state.step = 4
            st.rerun()
        else:
            st.error("اسم الأخ غير صحيح")

elif st.session_state.step == 4:
    show_img("omar-prince.jpeg")
    st.write("الان سنتناول الطعام")
    food_ans = st.text_input("ما معني كلمة الطعام بالانجليزيه ؟")
    if st.button("تأكيد الإجابة"):
        if food_ans.lower() == "food":
            st.session_state.step = 5
            st.rerun()

elif st.session_state.step == 5:
    show_img("family food 1.jpeg")
    st.write("الان وقت المغامرة سنذهب جميعا الي الغابة")
    show_img("junjle1.jpeg")
    naughty = st.text_input("ما معني كلمة مشاغب باللغه الانجليزيه ؟")
    if st.button("تأكيد"):
        if naughty.lower() == "naughty":
            st.session_state.step = 6
            st.rerun()

elif st.session_state.step == 6:
    show_img("omar.jpeg")
    st.write("قامت الغولة بخطف عمر! دور البطلة روفان!")
    head = st.text_input("ما معني كلمة رأس باللغه الانجليزيه ؟")
    ear = st.text_input("ما معني كلمة أذن باللغه الانجليزيه ؟")
    if st.button("إنقاذ عمر"):
        if head.lower() == "head" and ear.lower() == "ear":
            st.session_state.step = 7
            st.rerun()

elif st.session_state.step == 7:
    show_img("uni corne1.jpeg")
    st.write("استدعاء اليونيكورن!")
    mouth = st.text_input("ما معني كلمة فم باللغه الانجليزيه ؟")
    nose = st.text_input("ما معني كلمة انف باللغه الانجليزيه ؟")
    if st.button("المرحلة التالية"):
        if mouth.lower() == "mouth" and nose.lower() == "nose":
            st.session_state.step = 8
            st.rerun()

elif st.session_state.step == 8:
    show_img("uni corne 2.jpeg")
    eye = st.text_input("ما معني كلمة عين باللغه الانجليزيه ؟")
    hair = st.text_input("ما معني كلمة شعر باللغه الانجليزيه ؟")
    if st.button("إنهاء المهمة"):
        if eye.lower() == "eye" and hair.lower() == "hair":
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
