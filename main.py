import speech_recognition as sr
import os


def setup_recognizer():
    r = sr.Recognizer()
    return r


def fetch_audio(audio_recognizer):
    # requires C-lib PortAudio, more info here: https://realpython.com/python-speech-recognition/#installing-pyaudio
    src = sr.Microphone()
    with src as source:
        # audio_recognizer.adjust_for_ambient_noise(source)
        audio_file = audio_recognizer.listen(source)
    return audio_file


def recognize_audio(audio):
    try:
        # TODO: set up strategy abstraction
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return None


def print_speech(speech_text):
    try:
        assert speech_text is not None
        print(speech_text)
    except AssertionError:
        notify_error("There was a problem", "Could not process your speech into text")


def notify_error(title, err_text):
    os.system("""
    osascript -e 'display notification "{}" with title "{}"'
    """.format(err_text, title))


if __name__ == '__main__':
    print(sr.__version__)
    recognizer = setup_recognizer()
    audio = fetch_audio(recognizer)
    text = recognize_audio(audio)
    print_speech(text)
