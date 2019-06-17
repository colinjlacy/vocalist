import speech_recognition as sr


# TODO: set up strategy abstraction
def setup_recognizer(strategy="sphinx"):
    r = sr.Recognizer()
    return r.recognize_sphinx


if __name__ == '__main__':
    print(sr.__version__)
    recognizer = setup_recognizer()
