from vocalist.listener import Listener
from vocalist.extractor import Extractor
from threading import Thread


def print_output(q):
    while True:
        text = q.get(True)
        print(text)


def start_output_thread(q):
    output_thread = Thread(target=print_output, args=(q,))
    output_thread.setDaemon(True)
    output_thread.start()


if __name__ == '__main__':
    listener = Listener()
    extractor = Extractor(listener.output_q)
    start_output_thread(extractor.output_q)
    extractor.observe()
    listener.listen()
