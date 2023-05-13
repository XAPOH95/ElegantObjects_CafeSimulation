from interfaces import iPayment
from coffee import Coffee
from customer import Customer

class Cafe(iPayment):
    price_of_coffee = 5.0
    def __init__(self, customer:"Customer") -> None:
        print(f"Cafe employee says: 'Greeting, dear customer!'")
        self._customer = customer

    def Main(self):
        print(f"Cafe employee says: 'Please, make payment'")

        if self.payment():
            print(f"Cafe employee says: 'Thank you for purchase, I will bring coffee in a moment!'")
            coffee = self.make_coffee()
            
            self._drink_process(coffee)
            self._offer_another_one()

        else:
            print(f"Customer says: 'Seems like I dont have cash, goodbye!'")

    def payment(self):
        try:
            self._customer.payment(self.price_of_coffee)
            return True
        except self._customer.NotEnoughCash as exception:
            return False

    def make_coffee(self):
        return Coffee()

    def _drink_process(self, coffee:Coffee):
        print(f"Customer sits and starts to drink coffee")
        while not coffee.isEmpty():
            try:
                sip = coffee.make_sip()
                self._customer.drink(sip)
            except coffee.Empty as exception:
                print("Customer says: 'Waiter, my cup is empty, bring another one!")
                self.Main()

    def _offer_another_one(self):
        print(f"Cafe employee says: 'Another one?'")
        if self._customer.still_thirsty():
            print(f"Customer says: 'Yes, I would like to drink another one'")
            self.Main()
        else:
            print(f"Cafe says: 'No thanks, I gotta go'")