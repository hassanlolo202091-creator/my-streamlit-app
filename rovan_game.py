# بدلاً من الكود القديم، استخدم هذا النمط لكل خطوة:
elif st.session_state.step == 0:
    name = st.text_input("What Is Your Name?")
    if st.button("تأكيد الاسم"): # زر إضافي للتحكم
        if name.lower() == "rovan":
            show_img("rofy-princess.jpeg")
            st.session_state.step = 1
            st.rerun()
        else:
            st.error("الاسم غير صحيح، حاولي مجدداً")

elif st.session_state.step == 1:
    father = st.text_input("What Is Your Father Name?")
    if st.button("تأكيد اسم الأب"): # زر إضافي للتحكم
        if father.lower() == "hassan":
            show_img("hassan-king.jpeg")
            st.session_state.step = 2
            st.rerun()
