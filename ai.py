import streamlit as st
import requests

st.set_page_config(page_title="AI Assistant", page_icon="🤖")

st.title("🤖 AI Chat Assistant")
st.write("Projekt TIK - Chatbot me Python dhe AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pyetja = st.chat_input("Shkruaj pyetjen...")

if pyetja:

    st.session_state.messages.append(
        {"role": "user", "content": pyetja}
    )

    with st.chat_message("user"):
        st.markdown(pyetja)

    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/google/flan-t5-large",
            headers={
                "Authorization": "Bearer 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"
            },
            json={
                "inputs": pyetja
            },
            timeout=30
        )

        data = response.json()

        if isinstance(data, list):
            pergjigja = data[0]["generated_text"]
        else:
            pergjigja = "AI nuk ktheu pergjigje."

    except:
        pergjigja = "Ndodhi nje problem me AI."

    st.session_state.messages.append(
        {"role": "assistant", "content": pergjigja}
    )

    with st.chat_message("assistant"):
        st.markdown(pergjigja)