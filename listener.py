import queue
import threading

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
        self.__available_strategies = STRATEGY_LIST
        self.__set_strategy(strategy)
        self.__credentials = credentials
        self.__run = False
        self.__spoken_q = queue.Queue()
        self.output_q = queue.Queue()
        try:
            self.mic = sr.Microphone()
        except AttributeError:
            raise AttributeError("You'll need to install PyAudio first: https://people.csail.mit.edu/hubert/pyaudio/")

    def __set_strategy(self, chosen_strategy):
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 0.5
        try:
            strategy = STRATEGY_MAP[chosen_strategy]
            self.transcribe = self.recognizer.__getattribute__(strategy)
        except KeyError:
            raise KeyError("You'll need to select an available strategy: {}.  Note that the default is `google`.".format(self.__available_strategies))

    def __activate(self):
        try:
            assert self.mic is not None
            with self.mic as source:
                sounds = self.recognizer.listen(source)
                self.__spoken_q.put(sounds)
            while self.__run:
                self.__activate()
        except AssertionError:
            raise NameError("Could not find a suitable microphone.")

    def __parse(self):
        while self.__run:
            audio_input = self.__spoken_q.get(True)
            try:
                speech_text = self.transcribe(audio_input)
                self.output_q.put(speech_text)
            except sr.UnknownValueError:
                self.__notify_error("There was a problem", "Could not process your speech into text")

    def __notify_error(self, title, err_text):
        os.system("""
        osascript -e 'display notification "{}" with title "{}"'
        """.format(err_text, title))

    def listen(self):
        self.__run = True
        parse_thread = threading.Thread(target=self.__parse)
        parse_thread.setDaemon(True)
        parse_thread.start()
        self.__activate()

    def stop(self):
        self.__run = False
