import streamlit as st
import random

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="لعبة المحقق: القضايا اللانهائية",
    page_icon="🕵️‍♂️",
    layout="centered"
)

# جلب المستوى الحالي من رابط الصفحة أو البدء من الدور 1
query_params = st.query_params
if "level" in query_params:
    try:
        current_level = int(query_params["level"])
    except ValueError:
        current_level = 1
else:
    current_level = 1

st.session_state.level = current_level
level = st.session_state.level

# حساب الصعوبة وعدد المشتبه بهم بناءً على رقم الدور
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

# واجهة اللعبة
st.title("🕵️‍♂️ لعبة المحقق: قضية الفندق الغامض")
st.subheader(f"📌 الدور {level}: قضية الغرفة المغلقة")

col1, col2, col3 = st.columns(3)
col1.metric("المستوى", level)
col2.metric("الصعوبة", difficulty)
col3.metric("الوقت المتوقع", time_estimate)

st.divider()

# توليد تفاصيل القضية بناءً على رقم الدور الحالي
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

for suspect in suspects_list:
    if suspect == culprit:
        st.write(f"- **{suspect}**: \"كنت متواجداً في المكان ولكن لم ألمس شيئاً!\" *(شهادة مرتبكة)*")
    else:
        st.write(f"- **{suspect}**: \"لدي حجة غياب قوية، كنت في مكان آخر تماماً.\"")

st.divider()

# الاتهام والتأكد من الإجابة
selected_suspect = st.radio("من هو المتهم الحقيقي بناءً على الأدلة والتحقيق؟", suspects_list)

if st.button("تأكيد الاتهام وإصدار الحكم 🔍"):
    if selected_suspect == culprit:
        st.balloons()
        st.success(f"🎉 أحسنت يا سيادة المحقق! نجحت في كشف القاتل ({culprit}) وتفكيك اللغز.")
        
        # التحديث للدور التالي في الرابط ثم إعادة التحميل
        st.query_params["level"] = str(level + 1)
        st.button("الانتقال إلى الدور التالي ➡️")
    else:
        st.error("❌ اتهام خاطئ! الشخص المتهَم ليس هو الفاعل، حاول التركيز أكثر في الشهادات.")
        st.info("💡 تلميح: راقب الأقوال المرتبكة جيداً.")
