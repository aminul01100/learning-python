"""
we will create a payment system for the users who will have multiple options to pay
- card 
- paypay
- cash

functionalities:
    - provide options to the users
    - process the payment based on the user choice
    - generate a receipt (show with printing a message) for the payment
"""
from abc import ABC, abstractmethod
from enum import Enum

class PaymentOption(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class Card(PaymentOption):
    def __init__(self):
        self.card_number = ""
        self.cvv = ""

    def check_card_validity(self):
        # logic to check card validity
        return True

    def check_funds(self, amount):
        # logic to check if the card has sufficient funds
        return True

    def take_card_details(self):
        self.card_number = input("Enter your card number: ")
        self.cvv = input("Enter your card CVV: ")

    def pay(self, amount):
        self.take_card_details()

        if not self.check_card_validity():
            print("Invalid card details.")
            return False

        if not self.check_funds(amount):
            print("Insufficient funds.")
            return False
        # logic to process the card payment

        print(f"Processing card payment of amount {amount} with card number {self.card_number} and cvv {self.cvv}")
        print("Payment successful. Generating receipt...")
        print(f"Receipt: Paid {amount} using Card ending with {self.card_number[-4:]}")


class Cash(PaymentOption):

    def process_cash(self, amount):
        # logic to process cash payment
        # check the amount is valid, give change if needed, etc.
        return True

    def pay(self, amount):
        if not self.process_cash(amount):
            print("Invalid cash payment.")
            return False
        print(f"Processing cash payment of amount {amount}")
        print("Payment successful. Generating receipt...")
        print(f"Receipt: Paid {amount} in cash.")

class PayPay(PaymentOption):
    pass




PaymentOptions = {
    "1": Card,
    "2": Cash,
    "3": PayPay # we can implement this class similarly to Card and Cash
}
PaymentOptionsNames = ["1. Card", "2. Cash", "3. PayPay"]


def get_payment_option(user_choice):
    if user_choice in PaymentOptions:
        return PaymentOptions[user_choice]()
    else:
        print("Invalid payment method selected.")
        return None

print("Payment system is ready to use, please choose your payment method:")
for option in PaymentOptionsNames:
    print(option)

user_choice = input("Enter the payment method: ")


payment_option = get_payment_option(user_choice)

if payment_option:
    amount = float(input("Enter the amount to pay: "))
    payment_option.pay(amount)
else:
    print("Payment failed due to invalid payment method.")