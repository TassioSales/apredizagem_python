import time
import numpy as np
import sounddevice as sd

# Dicionário que mapeia caracteres para código Morse
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '  # Espaço em branco
}


def convert_to_morse(text):
    morse_text = []
    for char in text:
        char_upper = char.upper()
        if char_upper in morse_code:
            morse_text.append(morse_code[char_upper])
    return ' '.join(morse_text)


def play_morse_sound(morse_text):
    dot_duration = 100  # Duração do ponto em milissegundos
    dash_duration = 300  # Duração do traço em milissegundos
    silence_duration = 100  # Duração do silêncio entre os símbolos em milissegundos
    volume = 0.5  # Volume do som

    # Definir a função para gerar um sinal sonoro
    def generate_tone(frequency, duration):
        t = np.linspace(0, duration / 1000, int(duration * 44100 / 1000), False)
        return np.sin(2 * np.pi * frequency * t)

    for symbol in morse_text:
        if symbol == '.':
            tone = generate_tone(700, dot_duration)
        elif symbol == '-':
            tone = generate_tone(700, dash_duration)
        elif symbol == ' ':
            time.sleep(0.5)  # Pausa entre as palavras
            continue
        else:
            continue

        sd.play(volume * tone, 44100)
        sd.wait()

        # Pausa entre os símbolos
        sd.play(np.zeros(int(silence_duration * 44100 / 1000)), 44100)
        sd.wait()


if __name__ == "__main__":
    user_text = input("Digite o texto que deseja converter para código Morse: ")
    morse_text = convert_to_morse(user_text)
    print("Texto em código Morse:", morse_text)
    play_morse_sound(morse_text)
