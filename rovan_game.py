import streamlit as st
from PIL import Image

st.title("مغامرة الأميرة روفان والأمير عمر 👸🤴")

# دالة لعرض الصور
def show_img(filename):
    try:
        img = Image.open(f"images/{filename}")
        st.image(img, use_column_width=True)
    except:
        st.error(f"الصورة {filename} غير موجودة في مجلد images")

# -- خطوات القصة --
if 'step' not in st.session_state:
    st.session_state.step = 0

name = st.text_input("What Is Your Name ?")
if name.lower() == "rovan":
    show_img("rofy-princess.jpeg")
    
    father = st.text_input("What Is Your Father Name ?")
    if father.lower() == "hassan":
        show_img("hassan-king.jpeg")
        
        mother = st.text_input("What Is Your Mother Name ?")
        if mother.lower() == "aliaa":
            show_img("aliaa-queen.jpeg")
            
            brother = st.text_input("What Is Your Brother Name ?")
            if brother.lower() == "omar":
                show_img("omar-prince.jpeg")
                st.write("الان سنتناول الطعام")
                
                food_ans = st.text_input("ما معني كلمة الطعام بالانجليزيه ؟")
                if food_ans.lower() == "food":
                    show_img("family food 1.jpeg")
                    st.write("الان وقت المغامرة سنذهب جميعا الي الغابة")
                    show_img("junjle1.jpeg")
                    st.write("اثناء الصيد قال الاب ل عمر لا تذهب بعيدا ولكن عمر المشاغب لم يسمع كلام الاب وجري بعيدا بمفرده ليلعب مع القرود")
                    
                    naughty = st.text_input("ما معني كلمة مشاغب باللغه الانجليزيه ؟")
                    if naughty.lower() == "naughty":
                        show_img("omar.jpeg")
                        st.write("لان عمر لم يستمع الي كلام الاب فقامت الغوله بخطفه ولم يجد من ينقذه")
                        show_img("ghoul.jpeg")
                        st.write("الان دور البطله روفان في انقاذ اخيها")
                        show_img("rofy herro.jpeg")
                        st.write("يجب ان تجيب الاميره روفان علي الاسئلة لتتمكن من انقاذ اخيها")
                        
                        head = st.text_input("ما معني كلمة رأس باللغه الانجليزيه ؟")
                        ear = st.text_input("ما معني كلمة أذن باللغه الانجليزيه ؟")
                        
                        if head and ear:
                            st.write("والان قامت الاميره روفان باستدعاء اليونيكورن وحملت سيفها واستعدت لانقاذ الامير عمر")
                            show_img("uni corne1.jpeg")
                            
                            mouth = st.text_input("ما معني كلمة فم باللغه الانجليزيه ؟")
                            nose = st.text_input("ما معني كلمة انف باللغه الانجليزيه ؟")
                            
                            if mouth and nose:
                                st.write("والان قامت الاميره بامتطاء اليونيكورن وذهبت لانقاذ عمر من يد الغوله")
                                show_img("uni corne 2.jpeg")
                                
                                eye = st.text_input("ما معني كلمة عين باللغه الانجليزيه ؟")
                                hair = st.text_input("ما معني كلمة شعر باللغه الانجليزيه ؟")
                                
                                if eye and hair:
                                    st.write("وها قد فعلتها بطلة الابطال الاميره الجميله روفي البطله وانقذت الامير عمر والان هما في طريق العوده الي القصر")
                                    show_img("uni corne 3.jpeg")
                                    st.write("وعادت الاميره روفان الي ابيها وامها واعطاها ابيها كاس كبير لانها انقذت عمر وقد تعلم الامير عمر ان يسمع كلام ابيه وامه دائما")
                                    show_img("reward2.jpeg")
                                    show_img("reward1.jpeg")
 
