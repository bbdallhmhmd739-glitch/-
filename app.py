import streamlit as st

st.set_page_config(page_title="لعبة المحقق - القضية الكبرى", page_icon="🕵️‍♂️", layout="centered")

st.markdown("""
<style>
body { direction: RTL; text-align: right; }
</style>
""", unsafe_allow_html=True)

st.title("🕵️‍♂️ لعبة المحقق: شبكة الأسرار")

if "stage" not in st.session_state:
    st.session_state.stage = "intro"
if "clues" not in st.session_state:
    st.session_state.clues = []

# البداية
if st.session_state.stage == "intro":
    st.subheader("المرحلة 0: البداية")
    st.write("تم استدعاؤك للتحقيق في مسرح جريمة غامض داخل الفندق الكبير. الضحية رجل أعمال معروف.")
    st.write("هدف الرحلة: تجميع الأدلة، استجواب المشتبه بهم، وكشف الجاني الحقيقي!")
    if st.button("بدء التحقيق 🔍"):
        st.session_state.stage = "search_scene"
        st.rerun()

# المرحلة الأولى: تفتيش مسرح الجريمة
elif st.session_state.stage == "search_scene":
    st.subheader("المرحلة 1: تفتيش الغرفة")
    st.write("أنت الآن داخل غرفة الضحية. أين تريد أن تبحث عن الأدلة أولاً؟")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("تفتيش المكتب 📑"):
            if "رسالة تهديد" not in st.session_state.clues:
                st.session_state.clues.append("رسالة تهديد")
                st.success("عثرت على: رسالة تهديد غامضة في الدرج!")
    with col2:
        if st.button("تفتيش الخزنة 🗝️"):
            if "مفتاح خاص" not in st.session_state.clues:
                st.session_state.clues.append("مفتاح خاص")
                st.success("عثرت على: مفتاح صغير مصمم بشكل غريب!")

    st.write("---")
    st.write(f"الأدلة المجمعة حتى الآن: {', '.join(st.session_state.clues) if st.session_state.clues else 'لا يوجد أدلة بعد'}")
    
    if len(st.session_state.clues) >= 1:
        if st.button("الانتقال لاستجواب المشتبه بهم ➡️"):
            st.session_state.stage = "interrogate"
            st.rerun()

# المرحلة الثانية: الاستجواب
elif st.session_state.stage == "interrogate":
    st.subheader("المرحلة 2: غرف الاستجواب")
    st.write("لديك مشتبه بهما رئيسيان. من تريد أن تستجوب؟")
    
    suspect = st.radio("اختر المشتبه به:", ["مساعد الضحية (سارة)", "حارس الفندق (أحمد)"])
    
    if suspect == "مساعد الضحية (سارة)":
        st.write("سارة: 'أنا كنت في المكتبة وقت الحادثة، ولم ألمس أي شيء!'")
        if "رسالة تهديد" in st.session_state.clues:
            st.info("💡 يمكنك مواجهتها برسالة التهديد!")
    else:
        st.write("أحمد: 'أنا رأيت شخصاً يرتدي معطفاً أسود يركض في الممر.'")
        if "مفتاح خاص" in st.session_state.clues:
            st.info("💡 هذا المفتاح يطابق خزانة الحراس!")

    if st.button("توجيه الاتهام النهائي ⚖️"):
        st.session_state.stage = "accuse"
        st.rerun()

# المرحلة الثالثة: الاتهام والنتيجة
elif st.session_state.stage == "accuse":
    st.subheader("المرحلة الأخيرة: كشف الحقيقة")
    final_choice = st.selectbox("من هو القاتل بناءً على الأدلة؟", ["مساعد الضحية (سارة)", "حارس الفندق (أحمد)"])
    
    if st.button("تأكيد القرار 🎯"):
        if final_choice == "مساعد الضحية (سارة)" and "رسالة تهديد" in st.session_state.clues:
            st.balloons()
            st.success("🎉 أحسنت يا محقق! سارة هي الجانية بالفعل، ورسالة التهديد كانت الخيط الكاشف!")
        else:
            st.error("❌ للأسف، التقدير لم يكن صحيحاً أو الأدلة غير كافية. اعد المحاولة!")
            
        if st.button("إعادة اللعبة 🔄"):
            st.session_state.stage = "intro"
            st.session_state.clues = []
            st.rerun()
