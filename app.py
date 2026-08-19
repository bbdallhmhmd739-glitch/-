import streamlit as st
import random

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="لعبة المحقق: القضايا اللانهائية",
    page_icon="🕵️‍♂️",
    layout="centered"
)

# التهيئة الأوليّة لمستوى اللعبة
if 'level' not in st.session_state:
    st.session_state.level = 1

level = st.session_state.level

# حساب الصعوبة بناءً على المستوى
if level <= 500:
    difficulty = "سهل"
    num_suspects = 3
    time_estimate = "3 - 5 دقائق"
elif level <= 3000:
    difficulty = "متوسط"
    num_suspects = 5
    time_estimate = "5 - 7 دقائق"
else:
    difficulty = "صعب جداً"
    num_suspects = 7
    time_estimate = "7+ دقائق"

# عنوان التطبيق والمعلومات
st.title("🕵️‍♂️ لعبة المحقق: قضية الفندق الغامض")
st.subheader(f"📌 الدور {level}: قضية الغرفة المغلقة")

col1, col2, col3 = st.columns(3)
col1.metric("المستوى", level)
col2.metric("الصعوبة", difficulty)
col3.metric("الوقت المتوقع", time_estimate)

st.divider()

# مولد القضايا الأوتوماتيكي (معادلة ثابتة برقم المستوى)
random.seed(level)

characters = ["السيد أحمد (المدير)", "الآنسة سارة (الموظفة)", "السيد خالد (النزيل)", 
              "المهندس كريم", "الطاهي محمود", "الدكتور سامي", "السيدة فاطمة"]
items = ["ساعة يد مكسورة", "مفتاح ذهبي", "بصمة غريبة على الباب", "رسالة تهديد مشفرة", "خصلة شعر"]
locations = ["الغرفة 101", "المطعم الرئيسي", "حديقة الفندق", "المكتبة", "الممر الخلفي"]

suspects_list = random.sample(characters, num_suspects)
culprit = random.choice(suspects_list)
clue = random.choice(items)
crime_scene = random.choice(locations)

st.write(f"🔍 **تفاصيل البلاغ:** وقعت حادثة غامضة في **{crime_scene}**.")
st.write(f"🧩 **الدليل الرئيسي:** تم العثور على **{clue}** قرب موقع الجريمة.")

st.markdown("### 👥 قائمة المشتبه بهم والأقوال:")

# توليد أقوال المشتبه بهم
for suspect in suspects_list:
    if suspect == culprit:
        st.write(f"- **{suspect}**: \"كنت متواجداً في المكان ولكن لم ألمس شيئاً!\" *(شهادة مرتبكة)*")
    else:
        st.write(f"- **{suspect}**: \"لدي حجة غياب قوية، كنت في مكان آخر تماماً.\"" )

st.divider()

# منطقة الاتهام والتفاعل
selected_suspect = st.radio("من هو المتهم الحقيقي بناءً على الأدلة والتحقيق؟", suspects_list)

if st.button("تأكيد الاتهام وإصدار الحكم 🔍"):
    if selected_suspect == culprit:
        st.balloons()
        st.success(f"🎉 أحسنت يا سيادة المحقق! نجحت في كشف القاتل ({culprit}) وتفكيك اللغز.")
        
        if st.button("الانتقال إلى الدور التالي ➡️"):
            st.session_state.level += 1
            st.rerun()
    else:
        st.error(f"❌ اتهام خاطئ! الشخص المتهَم ليس هو الفاعل، حاول التركيز أكثر في الشهادات.")
        st.info("💡 تلميح: راقب الأقوال المرتبكة جيداً.")
