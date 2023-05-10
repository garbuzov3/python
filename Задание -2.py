from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)

    def get_type(self):
        return "Пальто"


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_consumption(self):
        return round(2 * self.height + 0.3, 2)

    def get_type(self):
        return "Костюм"


coat = Coat("Пальто", 46)
suit = Suit("Костюм", 170)

print(coat.get_type())
print(coat.fabric_consumption)

print(suit.get_type())
print(suit.fabric_consumption)
