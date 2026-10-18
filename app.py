import streamlit as st

from agent import run_agent


st.set_page_config(
    page_title="Saad AI",
    page_icon="🤖"
)


st.title("🤖 Saad Personal AI")

st.write(
    "AI Agent يعمل محلياً باستخدام Ollama"
)


user_input = st.text_area(
    "اكتب مهمتك:"
)


if st.button("تشغيل Agent"):

    if user_input:

        with st.spinner("AI يعمل..."):

            result = run_agent(
                user_input
            )

        st.subheader("النتيجة")

        st.write(result)