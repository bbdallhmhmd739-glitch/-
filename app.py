import streamlit as st

st.set_page_config(page_title="لعبة المحقق", page_icon="🕵️", layout="centered")

st.markdown("""
<style>
body { direction: RTL; text-align: right; }
</style>
""", unsafe_allow_html=True)

st.title("🕵️ لعبة المحقق: جريمة في القطار")

if "stage" not in st.session_state:
    st.session_state.stage = "intro"

if st.session_state.stage == "intro":
    st.write("أهلاً بك يا محقق! لقد تم العثور على جثة في القطار السريع.")
    st.write("أنت المحقق الوحيد القادر على حل هذا اللغز قبل وصول القطار للمحطة الأخيرة.")
    if st.button("ابدأ التحقيق"):
        st.session_state.stage = "scene_1"
        st.rerun()

elif st.session_state.stage == "scene_1":
    st.write("أنت الآن في عربة الركاب. هناك ثلاثة مشتبه بهم.")
    st.write("1. الرجل العجوز الذي يدعي أنه كان نائماً.")
    st.write("2. السيدة الأنيقة التي كانت تتشاجر مع الضحية.")
    st.write("3. الشاب المرتبك الذي يحمل حقيبة مشبوهة.")
    
    choice = st.radio("من ستستجوب أولاً؟", ["الرجل العجوز", "السيدة الأنيقة", "الشاب المرتبك"])
    
    if st.button("استجواب"):
        st.session_state.stage = "interrogation_result"
        st.session_state.choice = choice
        st.rerun()

elif st.session_state.stage == "interrogation_result":
    st.write(f"لقد اخترت استجواب: {st.session_state.choice}")
    if st.session_state.choice == "السيدة الأنيقة":
        st.write("لقد اعترفت بوجود خلاف مالي كبير بينها وبين الضحية!")
        st.write("وجدت دليلاً مهماً معها.")
        st.success("أحسنت! لقد أمسكت بالخيط الأول.")
    else:
        st.write("يبدو أن هذا الشخص بريء، لم تجد دليلاً يدينه.")
        st.warning("جرب شخصاً آخر.")
    
    if st.button("العودة للمشتبه بهم"):
        st.session_state.stage = "scene_1"
        st.rerun()
