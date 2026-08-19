import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
import docx

st.set_page_config(page_title="المساعد الذكي الشامل", page_icon="🤖", layout="wide")

st.markdown("""
<style>
body, div, p, input, textarea, button { direction: RTL; text-align: right; }
.stChatMessage { direction: RTL; text-align: right; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 تطبيق المساعد الذكي الشامل")

with st.sidebar:
    st.header("⚙️ الإعدادات والحساب")
    user_plan = st.selectbox("باقة الاشتراك الحالية:", ["النسخة المجانية (Free)", "النسخة الاحترافية (Pro) 💎"])
    api_key = st.text_input("أدخل مفتاح Gemini API الخاص بك:", type="password")
    
    st.subheader("📎 رفع ملف للتحليل")
    uploaded_file = st.file_uploader("اختر ملفاً (PDF, Word):", type=["pdf", "docx"])

file_context = ""
if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()
    if file_type == "pdf":
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            file_context += page.extract_text() or ""
        st.success("✅ تم قراءة ملف PDF بنجاح!")
    elif file_type == "docx":
        doc = docx.Document(uploaded_file)
        file_context = "\n".join([para.text for para in doc.paragraphs])
        st.success("✅ تم قراءة ملف Word بنجاح!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اكتب سؤالك هنا..."):
    if not api_key:
        st.error("❌ يرجى إدخال مفتاح Gemini API أولاً.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        full_prompt = f"المستند:\n{file_context[:4000]}\n\nالسؤال: {prompt}" if file_context else prompt

        with st.chat_message("assistant"):
            with st.spinner("جاري التفكير..."):
                try:
                    response = model.generate_content(full_prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"خطأ: {e}")
