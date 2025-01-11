import os
import streamlit as st
from transcribe import transcribe_audio

# Configurações da página
st.set_page_config(
    page_title="Transcrição de Áudio com Prompt",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Cabeçalho
st.title("🎙️ Transcrição de Áudio com Prompt")

# Inicializando o estado da sessão
if 'response' not in st.session_state:
    st.session_state['response'] = None

# Descrição
st.markdown("""
Bem-vindo! Aqui você pode carregar um arquivo de áudio, fornecer um prompt e obter a transcrição do áudio baseada no contexto fornecido.  
""")

# Upload do arquivo de áudio
audio_file = st.file_uploader("Carregue seu arquivo de áudio (MP3, WAV, OGG)", type=["mp3", "wav", "ogg"])

# Campo para o prompt do usuário
prompt = st.text_area("Digite seu prompt (opcional)", placeholder="Escreva um contexto ou instrução para a transcrição...")

# Botão para processar
if st.button("Transcrever"):
    if audio_file:
        with st.spinner("📤 Processando seu áudio e prompt..."):
            # Processar o arquivo de áudio e gerar a resposta
            response = transcribe_audio(audio_file, prompt)

            if response is not None:
                st.session_state['response'] = response
                st.success("✅ Transcrição concluída com sucesso!")
            else:
                st.error("⚠️ Ocorreu um erro durante a transcrição. Tente novamente.")

# Exibir o resumo gerado, se disponível
if st.session_state['response']:
    st.text_area("Resumo Gerado:", st.session_state['response'], height=200)
