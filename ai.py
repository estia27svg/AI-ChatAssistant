import streamlit as st

st.set_page_config(page_title="AI Assistant", page_icon="🤖")

st.title("🤖 AI Chat Assistant")
st.write("Mirësevini në chatbot-in tim!")

# Ruaj mesazhet
if "messages" not in st.session_state:
    st.session_state.messages = []

# Shfaq mesazhet e vjetra
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input nga përdoruesi
pyetja = st.chat_input("Shkruaj një pyetje...")

if pyetja:

    # Shfaq pyetjen e user
    st.session_state.messages.append(
        {"role": "user", "content": pyetja}
    )

    with st.chat_message("user"):
        st.markdown(pyetja)

    # Pergjigjet e chatbot
    if "pershendetje" in pyetja.lower():
        pergjigja = "Pershendetje! 😊 Si mund t'ju ndihmoj?"

    elif "si je" in pyetja.lower():
        pergjigja = "Jam mire! Faleminderit qe pyete 🤖"

    elif "python" in pyetja.lower():
        pergjigja = "Python eshte nje nga gjuhet programuese me te perdorura ne Inteligjencen Artificiale."

    elif "ai" in pyetja.lower():
        pergjigja = "Inteligjenca Artificiale eshte teknologji qe lejon kompjuteret te mendojne dhe te mesojne."

    else:
        pergjigja = f"Ju shkruat: {pyetja}"

    # Ruaj përgjigjen
    st.session_state.messages.append(
        {"role": "assistant", "content": pergjigja}
    )

    # Shfaq përgjigjen
    with st.chat_message("assistant"):
        st.markdown(pergjigja)