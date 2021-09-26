# class Guitar:
#     def play(self):
#         print("playing the guitar")
#
# def play_instrument(instrument):
#     return instrument.play()
#
# guitar = Guitar()
# play_instrument(guitar)
from abc import ABC, abstractmethod





class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


def play_instrument(instrument: Instrument):
    return instrument.play()

class Piano:
    def play(self):
        print("playing the piano")

piano = Piano()
play_instrument(piano)
