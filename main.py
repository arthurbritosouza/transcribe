import os
import streamlit as st
from transcribe import transcribe_audio
st.set_page_config(
    page_title="Transcrição de Áudio com Prompt",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("🎙️ Transcrição de Áudio com Prompt")

st.markdown("""
Bem-vindo! Aqui você pode carregar um arquivo de áudio, fornecer um prompt e obter a transcrição do áudio baseada no contexto fornecido.  
""")

if "Processando" not in st.session_state:
    st.session_state["Processando"] = False

audio_file = st.file_uploader("Carregue seu arquivo de áudio (MP3, WAV)", type=["mp3", "wav","ogg"])

prompt = st.text_area("Digite seu prompt (opcional)", placeholder="Escreva um contexto ou instrução para a transcrição...")

if st.button("Transcrever"):
    if audio_file:
        if audio_file is not None:
            os.makedirs("audios", exist_ok=True)
            name_file = os.path.join("audios", audio_file.name)
            with open(name_file, "wb") as f:
                f.write(audio_file.getbuffer())
            
        response = transcribe_audio(name_file, prompt)
        if response is None:
            st.session_state["Processando"] = True
            st.info("📤 Processando seu áudio e prompt...")
        else:
            st.session_state["Processando"] = False
        st.write("Resultado da transcrição:")
        st.text_area(
            "Transcrição",
            value=response,
            label_visibility="collapsed",
        )
    else:
        st.warning("⚠️ Por favor, carregue um arquivo de áudio antes de continuar.")
