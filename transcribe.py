import whisper
import warnings
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
warnings.filterwarnings("ignore", category=UserWarning)



def transcribe_audio(audio_path,user_input):
    # Carregar o modelo Whisper
    model = whisper.load_model("base")
    
    # Transcrever o áudio
    try:
        result = model.transcribe(audio_path)
        transcription = result["text"]
    except Exception as e:
        print(f"Erro ao transcrever o áudio: {e}")
        return None

    try:
        genai.configure(api_key='AIzaSyAjZk_OOAtqvSCC1yp7cyL7X_suj80H0Jk')
        model = genai.GenerativeModel("gemini-1.5-flash") 
        response = model.generate_content(f"Você é um assistente que resume a transcrição de um áudio, fornecendo informações de forma clara e objetiva. Transcrição: {transcription},Pergunta: {user_input}")
        print("Resumo gerado:", response.text)
    except Exception as e:
        print(f"Erro ao usar o modelo generativo: {e}")
    
    return response.text

# print(transcribe_audio("WhatsApp Ptt 2025-01-09 at 22.48.04.ogg","o que ele pretende fazer?"))


