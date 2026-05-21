import streamlit as st
from google import genai

# 1. Vendosni çelësin tuaj API brenda thonjëzave më poshtë
API_KEY = "AIzaSyCT9MSCKgzdaMQKl1hJqsoBQPonUXQcZT4"

# Lidhja me modelin e Inteligjencës Artificiale
try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"Gabim në konfigurim: {e}")

# Konfigurimi i faqes ueb (Pamja e aplikacionit)
st.set_page_config(page_title="AI Chat Assistant", page_icon="🤖", layout="centered")
st.title("🤖 AI Chat Assistant")
st.write("Projekt TIK - Mirësevini në chatbot-in tim personal!")

# Krijimi i historikut të bisedës në kujtesë
if "messages" not in st.session_state:
    st.session_state.messages = []

# Shfaqja e mesazheve të mëparshme në ekran
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Fusha ku shkruhet pyetja (Chat Input)
if pyetja := st.chat_input("Shkruaj diçka këtu..."):
    # Shfaq mesazhin e përdoruesit
    with st.chat_message("user"):
        st.markdown(pyetja)
    st.session_state.messages.append({"role": "user", "content": pyetja})

    # Dërgimi i pyetjes te Gemini dhe marrja e përgjigjes
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=pyetja
        )
        pergjigjja_ia = response.text
    except Exception as e:
        if "503" in str(e) or "UNAVAILABLE" in str(e):
            pergjigjja_ia = "Serveri është i mbingarkuar, ju lutem provoni përsëri pas pak sekondash."
        else:
            pergjigjja_ia = "Ndodhi një gabim gjatë lidhjes. Kontrolloni internetin."

    # Shfaq përgjigjen e AI në ekran
    with st.chat_message("assistant"):
        st.markdown(pergjigjja_ia)
    st.session_state.messages.append({"role": "assistant", "content": pergjigjja_ia})
