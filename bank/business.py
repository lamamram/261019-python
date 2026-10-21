# les imports inter packages sont calculés depuis le programme principal
from bank.actors import Client

class Account:

    def __init__(self, balance: float, overdraft: float, client: Client) -> None:
      self.__balance = balance
      self.__overdraft = overdraft
      self.client = client

    def withdraw(self, amount: float) -> None:
      if amount < 0:
        print(f"Transaction refusée: {amount} négatif")
      elif amount > self.__balance + self.__overdraft:
        print(f"Transaction refusée: {amount} fonds insuffisants")
      else:
        self.__balance -= amount
        print(f"Transaction acceptée")

    # méthode de type getter (retourne un attribut privé)
    def get_balance(self) -> float:
      return self.__balance

    def set_balance(self, new_balance: float) -> float:
      if new_balance < 0:
        print("Transaction refusée: valeur négative")
      self.__balance = new_balance

    def get_client_full_name(self):
      return self.client.get_full_name()