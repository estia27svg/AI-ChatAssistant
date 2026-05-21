import streamlit as st
import requests

# SHKRUAJ TOKEN-IN TËND TË HUGGING FACE KËTU BRENDA THONJËZAVE
HF_TOKEN = "hf_VENDOS_KETU_TOKENIN_TEND"

st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🤖 AI Chat Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #777;'>Projekt TIK - Chatbot me Python dhe AI</p>", unsafe_allow_html=True)
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if pyetja := st.chat_input("Shkruaj pyetjen..."):
    with st.chat_message("user"):
        st.markdown(pyetja)
    
    st.session_state.messages.append({"role": "user", "content": pyetja})
    
    try:
        # Përdorim modelin super stabël Mistral që nuk ka teka si Google
        API_URL = "https://api-inference.huggingface.co/models/MistralAI/Mistral-7B-Instruct-v0.3"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        
        # Formatim i thjeshtë pa kode që bllokojnë sistemin
        payload = {
            "inputs": f"Përgjigju shkurt në gjuhën shqipe: {pyetja}",
            "parameters": {"max_new_tokens": 200}
        }
        
        response = requests.post(API_URL, json=payload, headers=headers, timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            # Marrim tekstin direkt pa asnjë ndarje apo split
            pergjigja_ia = data[0]['generated_text']
            
            # Nëse modeli përsërit pyetjen, thjesht e pastrojmë pak
            if pyetja in pergjigja_ia:
                pergjigja_ia = pergjigja_ia.replace(f"Përgjigju shkurt në gjuhën shqipe: {pyetja}", "").strip()
        else:
            pergjigja_ia = f"Gabim nga Hugging Face (Kodi: {response.status_code})."
            
    except Exception as e:
        pergjigja_ia = f"Ndodhi një gabim në kod: {str(e)}"
    
    with st.chat_message("assistant"):
        st.markdown(pergjigja_ia)
    
    st.session_state.messages.append({"role": "assistant", "content": pergjigja_ia})