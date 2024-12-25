import speech_recognition as sr
import pyttsx3
import webbrowser

# Reconhecer Fala
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language='pt-BR')
            return text.lower()
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError:
            print("Erro no serviço de reconhecimento.")
    return None

# Converter texto em fala
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Processar comandos
def process_command(command):
    if "youtube" in command:
        speak("Abrindo YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "pesquisar" in command:
        speak("O que você quer pesquisar?")
        search_query = recognize_speech()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Pesquisando por {search_query}.")
    elif "sair" in command:
        speak("Encerrando o assistente. Até logo!")
        return True
    else:
        speak("Desculpe, ainda não sei como ajudar com isso.")
    return False

# Loop Principal
while True:
    command = recognize_speech()
    if command:
        if process_command(command):
            break
