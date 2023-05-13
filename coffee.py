from interfaces import iDrinkable

class Coffee(iDrinkable):
    def __init__(self) -> None:
        self._value = 50.0

    def make_sip(self):
        if not self.isEmpty() and self._value >= 10:
            self._value -= 10
            return 10
        raise self.Empty("Cup is empty!")

    def isEmpty(self):
        if self._value > 0:
            return False
        return True