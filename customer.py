from interfaces import iDrink, iPayment

class Customer(iDrink, iPayment):
    def __init__(self, cash:float) -> None:
        self._thirst = 100.0
        self._cash = cash

    def still_thirsty(self):
        if self._thirst < 30:
            return False
        else:
            return True

    def drink(self, value:float):
        if self.still_thirsty():
            self._thirst -= value

    def payment(self, bill:float):
        if self._cash > 0 and self._cash >= bill:
            self._cash -= bill
            return bill
        raise self.NotEnoughCash("Payment denied")

