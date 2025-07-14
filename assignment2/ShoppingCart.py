class ShoppingCart:

    def __init__(self):
       self.items = []

    def add_item(self, item_name: str, qty: int, unit_price: float):
       self.item_name = item_name
       self.qty = qty
       self.unit_price = unit_price

       self.items.append((item_name, qty, unit_price)) #This creates a tuple

    def remove_item(self, item_name: str):
       for item in self.items:
           if item[0] == item_name:
               self.items.remove(item)

    def calculate_total(self) -> float:

       total = 0

       for name, qty, price in self.items:
           total += qty * price

       return total

    def summary(self):

       print("Cart content")
       for name, qty, price in self.items:
           print(f"{name}: {qty} @ Ksh {price:.3f}") #This is a formatted string ie, you can change the format of a string
       print(f"Total: Ksh {self.calulate_total:():.3f}")


def add_item(name, quantity, price):
    pass


if __name__ == "__main__":
   cart: add_item("kiwi",69, 70.8) # type: ignore
   cart: add_item("apple", 45, 31.4) # type: ignore
   cart: add_item("grape", 60, 89.2) # type: ignore

   print(">>> Ordinary Cart<<<")
   cart.summary()









# def numbers(*num: int): #putting * before num makes it possible to put multiple items in a list, without errors
#     return int
# print(numbers(1,2,3,4,5))
#
#
#
# obj: ShoppingCart = ShoppingCart()
# obj2:ShoppingCart = ()
#
# print(obj.area(7))
# print(obj2.area(7.7))
