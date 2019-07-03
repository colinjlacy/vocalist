from queue import Queue
from threading import Thread
from code_domain_emissary.handlers import app as nlp


class Linguist:

    def __init__(self, q):
        self.__input_q = q
        self.output_q = Queue()
        self.__translation_thread = Thread(target=self.__input_q)
        self.__translation_thread.setDaemon(True)
        self.__run = False

    def process(self):
        # kick off a thread that sends the input_q data to nlp
        pass
