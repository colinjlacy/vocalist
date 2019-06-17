import speech_recognition as sr


def setup_recognizer():
    r = sr.Recognizer()
    return r


def fetch_audio(audio_recognizer):
    src = sr.Microphone()
    with src as source:
        # audio_recognizer.adjust_for_ambient_noise(source)
        audio_file = audio_recognizer.listen(source)
    return audio_file


if __name__ == '__main__':
    print(sr.__version__)
    recognizer = setup_recognizer()
    audio = fetch_audio(recognizer)
    # TODO: set up strategy abstraction
    text = recognizer.recognize_google(audio)
    print(text)
