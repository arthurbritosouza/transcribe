import io
import whisper
import warnings
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import whisper
import io
import numpy as np
from pydub import AudioSegment
import tempfile

load_dotenv()
warnings.filterwarnings("ignore", category=UserWarning)

def transcribe_audio(uploaded_file,user_input):
    # Carregar o modelo Whisper
    model = whisper.load_model("base")
    
        # Transcrever o áudio
    if uploaded_file is not None:
        # Salva o arquivo de áudio na memória
        audio_bytes = uploaded_file.read()

        # Usa io.BytesIO para tratar o arquivo na memória como um arquivo
        audio_file = io.BytesIO(audio_bytes)
        
    try:
        # Usar pydub para ler o arquivo de áudio e convertê-lo para WAV
        audio = AudioSegment.from_file(audio_file)
        
        # Salvar o arquivo temporariamente em formato WAV
        with tempfile.NamedTemporaryFile(delete=True) as tmp_wav_file:
            audio.export(tmp_wav_file.name, format="wav")
            
            # Carregar o arquivo WAV temporário com Whisper
            result = model.transcribe(tmp_wav_file.name)
            transcription = result["text"]
            st.write("Transcrição:", transcription)
    except Exception as e:
        st.error(f"Erro ao transcrever o áudio: {e}")


    try:
        genai.configure(api_key='AIzaSyAjZk_OOAtqvSCC1yp7cyL7X_suj80H0Jk')
        model = genai.GenerativeModel("gemini-1.5-flash") 
        response = model.generate_content(f"Você é um assistente que resume a transcrição de um áudio, fornecendo informações de forma clara e objetiva. Transcrição: {transcription},Pergunta: {user_input}")
        print("Resumo gerado:", response.text)
    except Exception as e:
        print(f"Erro ao usar o modelo generativo: {e}")
    
    return response.text

# print(transcribe_audio("WhatsApp Ptt 2025-01-09 at 22.48.04.ogg","o que ele pretende fazer?"))


