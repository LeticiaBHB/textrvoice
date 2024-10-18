
Speech Conversion Application
This Python script provides a simple way to convert text into speech using two different libraries:

gTTS (Google Text-to-Speech) for online text-to-speech conversion.
pyttsx3 for offline text-to-speech with support for multiple voices and more customization.
Prerequisites
Before running the script, you need to install the following dependencies:

gTTS:

bash
Copiar código
pip install gtts
pyttsx3:

bash
Copiar código
pip install pyttsx3
Features
gTTS: Converts text to speech using Google's Text-to-Speech API and saves the output as an MP3 file.
pyttsx3: Provides offline text-to-speech functionality, supporting multiple voices, customizable speech rate, and volume.
Usage
Run the Script:

bash
Copiar código
python <script_name>.py
Choose the Library: You will be prompted to choose which text-to-speech library to use:

Type 1 for gTTS (Google Text-to-Speech).
Type 2 for pyttsx3 (offline engine).
gTTS:

You will be prompted to choose a language: Portuguese, English, or Spanish.
Enter the text you want to convert.
The audio will be saved as audio_gtts.mp3 in the selected language.
pyttsx3:

Lists available voices for you to choose from.
Prompts for the speech rate and volume settings.
Reads the entered text aloud in real-time using the selected voice.
How It Works
gTTS Section
python
Copiar código
def escolher_gtts():
    # Choose the language for gTTS
    idiomas = {"1": "pt-br", "2": "en", "3": "es"}
    # Convert text to speech and save it as MP3
    tts = gTTS(text=texto, lang=idioma_selecionado)
    tts.save("audio_gtts.mp3")
pyttsx3 Section
python
Copiar código
def escolher_pyttsx3():
    engine = pyttsx3.init()
    # Configure the voice, speech rate, and volume
    engine.setProperty('voice', voices[opcao_voz].id)
    engine.setProperty('rate', velocidade)
    engine.setProperty('volume', volume)
    # Generate speech
    engine.say(texto)
    engine.runAndWait()
Conclusion
This script offers flexibility in how you convert text to speech, allowing you to use either a cloud-based service or an offline library, depending on your needs. Feel free to modify the code for further customization!
