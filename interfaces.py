### intrafaces

class iPayment:
    def payment(self):
        raise NotImplementedError
    
    class NotEnoughCash(Exception):
        pass

class iDrinkable:
    def make_sip(self):
        raise NotImplementedError

    class Empty(Exception):
        pass

class iDrink:
    def drink(self):
        raise NotImplementedError