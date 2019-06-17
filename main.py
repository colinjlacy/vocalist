import speech_recognition as sr
import os

# TODO: set up strategy abstraction
def setup_recognizer(strategy="sphinx"):
    r = sr.Recognizer()
    return r


def fetch_audio_file(audio_recognizer, path="audio-files/harvard.wav"):
    rel_path = os.path.join(os.getcwd(), path)
    src = sr.AudioFile(rel_path)
    with src as source:
        audio_file = audio_recognizer.record(source)
    return audio_file


if __name__ == '__main__':
    print(sr.__version__)
    recognizer = setup_recognizer()
    audio = fetch_audio_file(recognizer)
    text = recognizer.recognize_google(audio)
    print(text)
