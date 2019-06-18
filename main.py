import speech_recognition as sr
import os

STRATEGY_MAP = {
    "sphinx": "recognize_sphinx",
    "bing": "recognize_bing",
    "google": "recognize_google",
    "google_cloud": "recognize_google_cloud",
    "houndify": "recognize_houndify",
    "ibm": "recognize_ibm",
    "wit": "recognize_wit"
}

STRATEGY_LIST = ('sphinx', 'bing', 'google', 'google_cloud', 'houndify', 'ibm', 'wit')


class Listener:

    def __init__(self, strategy="google", credentials=None):
        self.AVAILABLE_STRATEGIES = STRATEGY_LIST
        self.__set_strategy(strategy)
        self.credentials = credentials
        self.mic = sr.Microphone()

    def __set_strategy(self, chosen_strategy):
        self.recognizer = sr.Recognizer()
        self.transcribe = self.recognizer.__getattribute__(STRATEGY_MAP[chosen_strategy])

    def __activate(self):
        with self.mic as source:
            audio_input = self.recognizer.listen(source)
        return audio_input

    def __parse(self, audio_input):
        try:
            return self.transcribe(audio_input)
        except sr.UnknownValueError:
            return None

    def __print(self, speech_text):
        try:
            assert speech_text is not None
            print(speech_text)
        except AssertionError:
            self.__notify_error("There was a problem", "Could not process your speech into text")

    def __notify_error(self, title, err_text):
        os.system("""
        osascript -e 'display notification "{}" with title "{}"'
        """.format(err_text, title))

    def listen(self):
        audio = self.__activate()
        text = self.__parse(audio)
        self.__print(text)


if __name__ == '__main__':
    l = Listener()
    l.listen()
