import streamlit as st

st.set_page_config(page_title="لعبة المحقق - القضايا المتعددة", page_icon="🕵️‍♂️", layout="centered")

st.markdown("""
<style>
body { direction: RTL; text-align: right; }
</style>
""", unsafe_allow_html=True)

st.title("🕵️‍♂️ لعبة المحقق: قضية الفندق الغامض")

if "stage" not in st.session_state:
    st.session_state.stage = "intro"
if "clues" not in st.session_state:
    st.session_state.clues = []
if "score" not in st.session_state:
    st.session_state.score = 0

# --- الدور الأول: المقدمة ---
if st.session_state.stage == "intro":
    st.subheader("📌 الدور 1: استلام المهمة")
    st.write("أهلاً بك يا سيادة المحقق! تم استدعاؤك لحل جريمة غامضة في الفندق الكلاسيكي.")
    st.write("أمامك عدة أدوار ومهمات يجب إنجازها خطوة بخطوة للوصول للحقيقة.")
    if st.button("بدء المهمة الأولى 🔍"):
        st.session_state.stage = "task1_search"
        st.rerun()

# --- الدور الثاني: مهمة البحث عن الأدلة ---
elif st.session_state.stage == "task1_search":
    st.subheader("🔍 الدور 2: مهمة البحث والتفتيش")
    st.write("أنت الآن في مسرح الجريمة. اختر الأماكن التي تريد تفقدها لإيجاد أدلة:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("تفتيش دراج المكتب 🗄️"):
            if "رسالة مشفرة" not in st.session_state.clues:
                st.session_state.clues.append("رسالة مشفرة")
                st.session_state.score += 10
                st.success("عثرت على ورقة بها رسالة مشفرة! (+10 نقاط)")
    with col2:
        if st.button("تفتيش السجادة 🧹"):
            if "بصمة غريبة" not in st.session_state.clues:
                st.session_state.clues.append("بصمة غريبة")
                st.session_state.score += 10
                st.success("عثرت على بصمة حذاء غامضة! (+10 نقاط)")

    st.info(f"الأدلة بحوزتك: {', '.join(st.session_state.clues) if st.session_state.clues else 'لا يوجد بعد'}")
    
    if len(st.session_state.clues) >= 2:
        if st.button("الانتقال للدور التالي (فك الشفرة) ➡️"):
            st.session_state.stage = "task2_puzzle"
            st.rerun()

# --- الدور الثالث: مهمة حل اللغز ---
elif st.session_state.stage == "task2_puzzle":
    st.subheader("🧩 الدور 3: مهمة فك الشفرة")
    st.write("للإنتقال للمرحلة القادمة، عليك حل الشفرة المكتوبة في الرسالة:")
    st.write("L-U-G-Z -> ما هي الكلمة الصحيحة باللغة العربية؟")
    
    answer = st.text_input("اكتب إجابتك هنا:")
    if st.button("تأكيد الحل 💡"):
        if answer.strip() in ["لغز", "اللغز"]:
            st.success("إجابة صحيحة! تم فك الخزنة بنجاح. (+20 نقطة)")
            st.session_state.score += 20
            st.session_state.stage = "task3_interrogate"
            st.rerun()
        else:
            st.error("إجابة خاطئة، حاول مرة أخرى!")

# --- الدور الرابع: مهمة الاستجواب ---
elif st.session_state.stage == "task3_interrogate":
    st.subheader("🗣️ الدور 4: مهمة استجواب المشتبه بهم")
    st.write("لديك شخصان مشتبه بهما، استجوبهما بدقة:")
    
    suspect = st.selectbox("اختر من تريد استجوابه:", ["المدير (سامي)", "الموظفة (نور)"])
    
    if suspect == "المدير (سامي)":
        st.write("سامي: 'أنا كنت في مكتبي، لكن البصمة على السجادة قد تكون لأحد العمال.'")
    else:
        st.write("نور: 'أنا رأيت سامي يحمل الرسالة المشفرة قبل الجريمة بـ 10 دقائق!'")

    if st.button("الذهاب للدور النهائي (إصدار الحكم) ⚖️"):
        st.session_state.stage = "final_accuse"
        st.rerun()

# --- الدور الخامس: الاتهام والنهاية ---
elif st.session_state.stage == "final_accuse":
    st.subheader("⚖️ الدور 5: القرار النهائي")
    st.write(f"مجموع نقاطك الكلي: {st.session_state.score}")
    
    final_choice = st.radio("من هو القاتل الحقيقي بناءً على الأدلة والشهادات؟", ["المدير (سامي)", "الموظفة (نور)"])
    
    if st.button("تأكيد الاتهام 🎯"):
        if final_choice == "المدير (سامي)":
            st.balloons()
            st.success("🎉 ممتاز جداً! نجحت في حل الجريمة وألقت الشرطة القبض على المدير!")
        else:
            st.error("❌ للأسف، الاتهام كان خاطئاً والقاتل الحقيقي هرب!")
            
        if st.button("لعب لعبة جديدة 🔄"):
            st.session_state.stage = "intro"
            st.session_state.clues = []
            st.session_state.score = 0
            st.rerun()
