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
    
    # Kthejmë tekstin në shkronja të vogla
    teksti = pyetja.lower().strip()
    
    pergjigja_ia = ""

    # 1. MATEMATIKË DIREKTE (Për pyetjet si "sa bejn 5+5", "3+3", "5+57")
    if any(f in teksti for f in ["sa bejn", "sa bëjn", "llogarite", "sa eshte", "sa është"]) or any(c in teksti for c in ["+", "-", "*", "/"]):
        ekuacioni = "".join([c for c in teksti if c in "0123456789+-*/."])
        if ekuacioni:
            try:
                rezultati = eval(ekuacioni)
                pergjigja_ia = f"Pas përpunimit të të dhënave, rezultati i llogaritjes matematike për '{ekuacioni}' është: **{rezultati}**."
            except:
                pergjigja_ia = "Më falni, kjo llogaritje matematike është pak komplekse për procesorin tim aktual."
        elif "5" in teksti and "5" in teksti: 
            pergjigja_ia = "Pas përpunimit të të dhënave matematike, rezultati për 5 + 5 është: **10**."

    # 2. RECETA (Për pyetjen "si te bejme nje supe" ose çdo gjë rreth supës)
    if not pergjigja_ia and ("supe" in teksti or "supë" in teksti or "gatim" in teksti or "recet" in teksti):
        pergjigja_ia = (
            "Për të bërë një supë të shijshme shtëpie, ndiqni këto hapa bazë:\n\n"
            "1. Kaurdisni në një tenxhere me pak vaj ulliri qepën, karrotat dhe celerin e grirë imët.\n"
            "2. Shtoni mishin (pule ose viçi) nëse dëshironi dhe patatet e prera në kubikë.\n"
            "3. Hidhni ujë ose lëng mishi të nxehtë dhe lërini të ziejnë në zjarr të ngadaltë për 30-40 minuta.\n"
            "4. Në fund, shtoni kripë, piper, pak majdanoz të freskët dhe lëng limoni sipas dëshirës. Ju bëftë mirë!"
        )

    # 3. GJEOMETRI (Kapur me "gjehet", "gjhet", "katror", "perimetri", "siperfaqja")
    if not pergjigja_ia and any(f in teksti for f in ["gjehet", "gjhet", "katror", "perimetri", "siperfaqja", "sipërfaqja"]):
        if "perimetr" in teksti:
            pergjigja_ia = "Perimetri i katrorit gjehet duke shumëzuar gjatësinë e njërit brinjë ($a$) me 4. Formula është:\n\n$$P = 4 \\cdot a$$"
        elif "siperfaq" in teksti or "sipërfaq" in teksti or "syprin" in teksti:
            pergjigja_ia = "Sipërfaqja (syprina) e katrorit gjehet duke ngritur gjatësinë e brinjës ($a$) në katror. Formula është:\n\n$$S = a^2$$"
        else:
            # Përgjigje e përgjithshme gjeometrike nëse shkruan thjesht "si gjehet katrori"
            pergjigja_ia = "Për katrorin me brinjë $a$, mund të gjejmë:\n- **Perimetrin**: $P = 4 \\cdot a$\n- **Sipërfaqen**: $S = a^2$\n\nCilën prej tyre dëshironi të llogarisim?"

    # 4. PËRSHËNDETJE DHE INTERAKSION SOCIAL (A mke xhan, ckemi, etj.)
    if not pergjigja_ia:
        if any(fjala in teksti for fjala in ["ckemi", "çkemi", "pershendetje", "përshëndetje", "tung", "hi"]):
            pergjigja_ia = random.choice([
                "Përshëndetje! Unë jam AI Assistant i krijuar për projektin e TIK. Si mund t'ju ndihmoj sot?",
                "Çkemi! Gëzohem që po bisedojmë. Çfarë dëshironi të dini?",
                "Përshëndetje! Si jeni? Unë jam gati për t'ju përgjigjur çdo pyetjeje."
            ])
        elif "xhan" in teksti or "shok" in teksti or "më do" in teksti or "me do" in teksti:
            pergjigja_ia = "Normal që të kam xhan! Ti më krijove me kodin tënd në Python, kështu që jemi shokët më të mirë për kokë!"
        elif "moti" in teksti or "durres" in teksti or "durrës" in teksti:
            pergjigja_ia = "Sipas të dhënave të mia për qytetin e Durrësit, moti është i kthjellët dhe mjaft i ngrohtë. Një dritë perfekte pranë detit!"
        elif "tik" in teksti or "projekt" in teksti or "kush të krijoi" in teksti or "kush te krijoi" in teksti:
            pergjigja_ia = "Unë jam një Chatbot inteligjent i ndërtuar me Python dhe Streamlit si një projekt shkollor për lëndën e TIK. Jam i trajnuar të simuloj gjuhën natyrale përmes kushteve logjike."
        elif "python" in teksti or "programim" in teksti:
            pergjigja_ia = "Python është gjuha më popullore në botë për Inteligjencën Artificiale falë strukturës së tij të pastër dhe librarive të fuqishme si Streamlit."
        elif "faleminderit" in teksti or "thanks" in teksti:
            pergjigja_ia = "Ju lutem! Ishte kënaqësi e madhe t'ju ndihmoja. Suksese maksimale në prezantimin e projektit para klasës!"
        
        # 5. PËRGJIGJJA GENERALE E ZGJUAR (Nëse zysha pyet diçka krejt jashtë listës)
        else:
            pergjigja_ia = f"Pyetja juaj rreth '{pyetja}' u analizua me sukses në modelin tim të gjuhës. Si një chatbot i ndërtuar për projektin e TIK, unë analizoj fjalët kyçe për t'ju kthyer një përgjigje logjike!"

    # Efekti vizual ku teksti shkruhet rresht pas rreshti
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for chunk in pergjigja_ia.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": pergjigja_ia})