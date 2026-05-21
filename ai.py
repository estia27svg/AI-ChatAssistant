import streamlit as st
import random
import time

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
    
    # Logjika e inteligjencës së simuluar në shqip
    teksti = pyetja.lower().strip()
    
    if "ckemi" in teksti or "çkemi" in teksti or "pershendetje" in teksti or "përshëndetje" in teksti:
        pergjigja_ia = random.choice([
            "Përshëndetje! Unë jam AI Assistant i krijuar për projektin e TIK. Si mund t'ju ndihmoj sot?",
            "Çkemi! Gëzohem që po bisedojmë. Çfarë dëshironi të dini?",
            "Përshëndetje! Si jeni? Unë jam gati për t'ju përgjigjur çdo pyetjeje."
        ])
    elif "moti" in teksti or "durres" in teksti or "durrës" in teksti:
        pergjigja_ia = "Sipas të dhënave të mia për qytetin e Durrësit, moti është kryesisht i kthjellët me erëra të lehta nga veriperëndimi. Një ditë perfekte pranverore!"
    elif "tik" in teksti or "projekt" in teksti or "kush të krijoi" in teksti:
        pergjigja_ia = "Unë jam një Chatbot inteligjent i ndërtuar me Python dhe Streamlit si një projekt shkollor për lëndën e TIK. Jam i integruar për të procesuar gjuhën natyrale."
    elif "python" in teksti or "programim" in teksti:
        pergjigja_ia = "Python është një nga gjuhët më të fuqishme dhe më të përdorura në botë për Inteligjencën Artificiale, falë sintaksës së tij të thjeshtë dhe librarive të shumta."
    elif "faleminderit" in teksti:
        pergjigja_ia = "Ju lutem! Ishte kënaqësi t'ju ndihmoja. Suksese në projektin tuaj!"
    else:
        # Përgjigje gjenerale e zgjuar nëse shkruhet diçka tjetër
        pergjigja_ia = f"Pyetja juaj rreth '{pyetja}' u procesua me sukses në modelin tim të gjuhës. Si projekt TIK, unë analizoj çdo fjalë kyçe për t'ju kthyer një përgjigje sa më të saktë!"

    # Simulojmë sikur AI po mendon dhe po shkruan në kohë reale
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for chunk in pergjigja_ia.split():
            full_response += chunk + " "
            time.sleep(0.08)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": pergjigja_ia})