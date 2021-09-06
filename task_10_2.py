from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc(self):
        pass

class Coat(Clothes):

    @property
    def calc(self):
        return round((self.param / 6.5) + 0.5)

class Suit(Clothes):

    @property
    def calc(self):
        return round((2 * self.param) + 0.3)

suit = Suit(23)
coat = Coat(20)

print(suit.calc)
print(coat.calc)
print(suit.calc + coat.calc)