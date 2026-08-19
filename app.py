ضimport streamlit as st
import random

# حفظ التقدم في الجلسة
if 'level' not in st.session_state:
    st.session_state.level = 1

level = st.session_state.level

# حساب الصعوبة بناءً على رقم الدور
num_suspects = min(3 + (level // 500), 8) # يزداد عدد المشتبه بهم كلما ارتفع المستوى
time_estimate = "3-5 دقائق" if level < 500 else "5-7 دقائق"

st.title(f"🕵️‍♂️ لعبة المحقق - الدور {level}")
st.caption(f"مستوى الصعوبة: {'سهل' if level < 500 else 'متوسط/صعب'} | الوقت المتوقع: {time_estimate}")

# مولد القضية الأوتوماتيكي بناءً على رقم الدور
random.seed(level) # يضمن أن الدور له نفس المعطيات دائماً

suspects = [f"شخصية {i+1}" for i in range(num_suspects)]
culprit = random.choice(suspects)

st.write(f"📌 **تفاصيل القضية:** وقعت جريمة غامضة وهناك {num_suspects} مشتبه بهم.")
st.write("استمع لأقوال المشتبه بهم واكتشف الجاني:")

selected = st.radio("من هو القاتل حسب الأدلة؟", suspects)

if st.button("تأكيد الاتهام 🔍"):
    if selected == culprit:
        st.success("🎉 إجابة صحيحة! تم القبض على الجاني وإحالتة للقاضي.")
        if st.button("Transition to Level Next ➡️"):
            st.session_state.level += 1
            st.rerun()
    else:
        st.error("❌ اتهام خاطئ! القاتل الحقيقي لا يزال طليقاً.")
        # هنا يمكن إضافة زر مشاهدة إعلان للحصول على تلميح
