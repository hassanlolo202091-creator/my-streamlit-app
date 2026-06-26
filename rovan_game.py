import streamlit as st
from PIL import Image

st.title("مغامرة الأميرة روفان والأمير عمر 👸🤴")

# تهيئة الحالة للتنقل بين المراحل
if 'step' not in st.session_state:
    st.session_state.step = 0

def show_img(filename):
    try:
        # تأكد من أن الصور موجودة في مجلد images بجانب ملف الكود
        img = Image.open(f"images/{filename}")
        st.image(img, use_column_width=True)
    except:
        st.warning(f"الصورة {filename} غير موجودة في مجلد images")

# -- مراحل القصة --

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
    st.write("اثناء الصيد قال الاب لعمر: لا تذهب بعيدا.. ولكن عمر المشاغب لم يسمع الكلام وجرى بعيدا!")
    naughty = st.text_input("ما معني كلمة مشاغب باللغه الانجليزيه ؟")
    if naughty.lower() == "naughty":
        show_img("omar.jpeg")
        st.write("للأسف، قامت الغولة بخطفه!")
        if st.button("إنقاذ عمر"):
            st.session_state.step = 6
            st.rerun()

elif st.session_state.step == 6:
    show_img("rofy herro.jpeg")
    st.write("دور البطلة روفان الآن! يجب الإجابة على الأسئلة لإنقاذ أخيك.")
    head = st.text_input("ما معني كلمة رأس باللغه الانجليزيه ؟")
    ear = st.text_input("ما معني كلمة أذن باللغه الانجليزيه ؟")
    if head.lower() == "head" and ear.lower() == "ear":
        st.success("أحسنتِ!")
        if st.button("استدعاء اليونيكورن"):
            st.session_state.step = 7
            st.rerun()
 elif st.session_state.step == 7:
    show_img("uni corne1.jpeg")
    st.write("الآن قامت الأميرة روفان باستدعاء اليونيكورن وحملت سيفها!")
    mouth = st.text_input("ما معنى كلمة فم باللغة الإنجليزية؟")
    nose = st.text_input("ما معنى كلمة أنف باللغة الإنجليزية؟")
    
    if mouth.lower() == "mouth" and nose.lower() == "nose":
        st.success("أحسنتِ يا بطلة!")
        if st.button("الذهاب لإنقاذ عمر"):
            st.session_state.step = 8
            st.rerun()

elif st.session_state.step == 8:
    show_img("uni corne 2.jpeg")
    st.write("امتطت الأميرة اليونيكورن وذهبت لإنقاذ عمر من يد الغولة.")
    eye = st.text_input("ما معنى كلمة عين باللغة الإنجليزية؟")
    hair = st.text_input("ما معنى كلمة شعر باللغة الإنجليزية؟")
    
    if eye.lower() == "eye" and hair.lower() == "hair":
        st.success("لقد أنقذتِ الموقف!")
        if st.button("العودة للقصر"):
            st.session_state.step = 9
            st.rerun()

elif st.session_state.step == 9:
    show_img("uni corne 3.jpeg")
    st.write("وها قد عادت بطلة الأبطال روفان ومعها الأمير عمر!")
    st.write("أعطاها الأب كأساً كبيراً لمكافأتها، وتعلم عمر أن يسمع كلام والديه.")
    show_img("reward2.jpeg")
    show_img("reward1.jpeg")
    
    if st.button("إعادة اللعب من جديد؟"):
        st.session_state.step = 0
        st.rerun()

# يمكنك إكمال باقي المراحل بنفس هذا النمط (7, 8, ...)
