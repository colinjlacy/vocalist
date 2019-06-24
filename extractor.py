from queue import Queue
from threading import Thread


class Extractor:

    def __init__(self, q):
        self.__input_q = q
        self.output_q = Queue()
        self.__transcribe_thread = Thread(target=self.__watch_q)
        self.__transcribe_thread.setDaemon(True)
        self.__run = False

    def observe(self):
        self.__run = True
        self.__transcribe_thread.start()

    def ignore(self):
        self.__run = False

    def __watch_q(self):
        while self.__run:
            text = self.__input_q.get(True)
            print(text)
