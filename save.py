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

# Descrição
st.markdown("""
Bem-vindo! Aqui você pode carregar um arquivo de áudio, fornecer um prompt e obter a transcrição do áudio baseada no contexto fornecido.  
""")

# Upload do arquivo de áudio
audio_file = st.file_uploader("Carregue seu arquivo de áudio (MP3, WAV)", type=["mp3", "wav","ogg"])

# Campo para o prompt do usuário
prompt = st.text_area("Digite seu prompt (opcional)", placeholder="Escreva um contexto ou instrução para a transcrição...")

# Botão para processar
if st.button("Transcrever"):
    if audio_file:
        if audio_file is not None:
            os.makedirs("audios", exist_ok=True)
            name_file = os.path.join("audios", audio_file.name)
            # Salvar o arquivo no diretório local
            with open(name_file, "wb") as f:
                f.write(audio_file.getbuffer())  # Salva o arquivo no mesmo nome original
            st.success(f"Arquivo {name_file} salvo com sucesso!")
            
        st.info("📤 Processando seu áudio e prompt...")
        response = transcribe_audio(name_file, prompt)
        st.success("✅ Transcrição concluída!")
        st.write("Resultado da transcrição:")
        st.write(response)
    else:
        st.warning("⚠️ Por favor, carregue um arquivo de áudio antes de continuar.")
