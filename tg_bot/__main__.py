from multiprocessing import Process

from .tg_bot import TG_UBOT
from .tg_bot import TG_BOT


def func1():
    TG_UBOT().run()


def func2():
    TG_BOT().run()


if __name__ == "__main__":
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join()
    p2.join()
