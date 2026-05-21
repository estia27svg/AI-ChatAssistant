import streamlit as st

st.set_page_config(page_title="AI Assistant", page_icon="🤖")

st.title("🤖 AI Chat Assistant")
st.write("Mirësevini në chatbot-in tim!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pyetja = st.chat_input("Shkruaj një pyetje...")

if pyetja:
    st.session_state.messages.append(
        {"role": "user", "content": pyetja}
    )

    with st.chat_message("user"):
        st.markdown(pyetja)

    # Pergjigje fake AI
    if "pershendetje" in pyetja.lower():
        pergjigja = "Pershendetje! 😊 Si mund t'ju ndihmoj?"
    elif "si je" in pyetja.lower():
        pergjigja = "Jam mire! Faleminderit qe pyete 🤖"
    elif "python" in pyetja.lower():
        pergjigja = "Python eshte nje gjuhe programuese shume e perdorur ne AI."
    else:
        pergjigja = f"Ju shkruat: {pyetja}"

    st.session_state.messages.append(
        {"role": "assistant", "content": pergjigja}
    )

    with st.chat_message("assistant"):
        st.markdown(pergjigja)import streamlit as st

st.set_page_config(page_title="AI Assistant", page_icon="🤖")

st.title("🤖 AI Chat Assistant")
st.write("Mirësevini në chatbot-in tim!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pyetja = st.chat_input("Shkruaj një pyetje...")

if pyetja:
    st.session_state.messages.append(
        {"role": "user", "content": pyetja}
    )

    with st.chat_message("user"):
        st.markdown(pyetja)

    # Pergjigje fake AI
    if "pershendetje" in pyetja.lower():
        pergjigja = "Pershendetje! 😊 Si mund t'ju ndihmoj?"
    elif "si je" in pyetja.lower():
        pergjigja = "Jam mire! Faleminderit qe pyete 🤖"
    elif "python" in pyetja.lower():
        pergjigja = "Python eshte nje gjuhe programuese shume e perdorur ne AI."
    else:
        pergjigja = f"Ju shkruat: {pyetja}"

    st.session_state.messages.append(
        {"role": "assistant", "content": pergjigja}
    )

    with st.chat_message("assistant"):
        st.markdown(pergjigja)