from gtts import gTTS
import pyttsx3


def escolher_gtts():
    # Escolha de idioma para gTTS
    print("Escolha um idioma para gTTS:")
    print("1. Português (Brasil)")
    print("2. Inglês")
    print("3. Espanhol")

    opcao_idioma = input("Digite o número da sua escolha: ")

    idiomas = {
        "1": "pt-br",
        "2": "en",
        "3": "es"
    }

    idioma_selecionado = idiomas.get(opcao_idioma, "pt-br")

    # Texto que deseja converter
    texto = input("Digite o texto que deseja converter para áudio: ")

    # Converte texto para áudio usando gTTS
    tts = gTTS(text=texto, lang=idioma_selecionado)

    # Salva o áudio em um arquivo mp3
    tts.save("audio_gtts.mp3")

    print(f"Áudio gerado e salvo como 'audio_gtts.mp3' no idioma {idioma_selecionado}.")


def escolher_pyttsx3():
    # Inicializa o engine de texto para fala usando pyttsx3
    engine = pyttsx3.init()

    # Lista todas as vozes disponíveis
    voices = engine.getProperty('voices')

    # Exibe as vozes e suas propriedades
    print("Vozes disponíveis para pyttsx3:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} - {voice.languages}, ID: {voice.id}")

    # Escolhe uma voz
    opcao_voz = int(input("Digite o número da voz que deseja usar: "))

    # Configura a voz escolhida
    engine.setProperty('voice', voices[opcao_voz].id)

    # Texto que deseja converter
    texto = input("Digite o texto que deseja converter para áudio: ")

    # Ajusta a velocidade de fala (opcional)
    velocidade = int(input("Digite a velocidade de fala (padrão: 150): ") or 150)
    engine.setProperty('rate', velocidade)

    # Ajusta o volume (opcional, entre 0.0 e 1.0)
    volume = float(input("Digite o volume de 0.0 a 1.0 (padrão: 1.0): ") or 1.0)
    engine.setProperty('volume', volume)

    # Converte texto em áudio usando pyttsx3
    engine.say(texto)

    # Executa o processo de fala
    engine.runAndWait()

    print(f"Áudio gerado e executado com a voz selecionada.")


def main():
    print("Escolha qual biblioteca você deseja usar:")
    print("1. gTTS (Google Text-to-Speech)")
    print("2. pyttsx3 (Offline e Múltiplas Vozes)")

    opcao = input("Digite o número da sua escolha: ")

    if opcao == "1":
        escolher_gtts()
    elif opcao == "2":
        escolher_pyttsx3()
    else:
        print("Opção inválida. Escolha entre 1 ou 2.")


if __name__ == "__main__":
    main()
