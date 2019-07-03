from vocalist.linguist import Linguist
from vocalist.listener import Listener
from vocalist.extractor import Extractor

if __name__ == '__main__':
    listener = Listener()
    extractor = Extractor(listener.output_q)
    linguist = Linguist(extractor.output_q)
    extractor.observe()
    listener.listen()
