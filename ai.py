import streamlit as st
import requests

# API Key yt i saktë
API_KEY = "AIzaSyCT9MSCKgzdaMQKl1hJqsoBQPonUXQcZT4"

st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🤖 AI Chat Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #777;'>Projekt TIK - Mirësevini në chatbot-in tim personal!</p>", unsafe_allow_html=True)
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if pyetja := st.chat_input("Shkruaj diçka këtu..."):
    with st.chat_message("user"):
        st.markdown(pyetja)
    
    st.session_state.messages.append({"role": "user", "content": pyetja})
    
    try:
        # URL zyrtare e saktë pa v1beta që funksionon me requests
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": pyetja}
                    ]
                }
            ]
        }
        
        # Rrisim timeout në 30 sekonda që mos të bllokohet kurrë nga rrjeti
        response = requests.post(url, json=payload, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            pergjigja_ia = data['candidates'][0]['content']['parts'][0]['text']
        else:
            # Nëse Google ka ndonjë problem të përkohshëm, të na tregojë saktë kodin
            pergjigja_ia = f"Serveri i Google u përgjigj me kodin {response.status_code}. Ju lutem riprovoni pas pak."
            
    except Exception as e:
        pergjigja_ia = "Ndodhi një vonesë e vogël në rrjet. Ju lutem shkruani përsëri."
    
    with st.chat_message("assistant"):
        st.markdown(pergjigja_ia)
    
    st.session_state.messages.append({"role": "assistant", "content": pergjigja_ia})