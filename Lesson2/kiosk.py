import random

def main():

    np = kiosk()

    print("Hello! Welcome!")
    np.additem(input("Please enter an item: "))
    while not(np.newTransaction() == "D"):
        np.additem(input("Please enter another item: "))
    np.gettotal()
    np.takepayment(input("Please enter a payment type: "))
    np.givechange()
    np.finalizetrans()


class kiosk:

    def __init__(self, entered_amount=0, total=0, items=[],prices=[]):

        self.items = items
        self.prices = prices
        self.total = total
        self.entered_amount = entered_amount

    def newTransaction(self):
        if input("Will that be all for today? y/n") == "y":
            return "D"

    def additem(self, item):
        self.items.append(item)
        price = random.randint(100, 5000)/100
        self.prices.append(price) if input(f"A {item}, that'll be ${price}, is that ok? y/n") == "y" else print("Ok! Removed from list!")
    
    def gettotal(self):
        self.total = sum(self.prices)
        print(f"Your total today is ${self.total}")

    def takepayment(self, pay_type):
        self.entered_amount = int(input(f"Please enter an amount using {pay_type} to pay your total of ${self.total}: "))
        if not(self.entered_amount >= self.total):
            while not(self.entered_amount >= self.total):
                self.entered_amount = int(input(f"Please enter enough using {pay_type} to pay your total of ${self.total}: "))
    
    def givechange(self):
        print(f"Thank you! Your change is {int(self.total) - self.entered_amount}")

    def finalizetrans(self):
        print(""" Heres your reciept:

########################################### 
      
      """)

        for i in range(len(self.items)):
            print(f"{self.items[i]} --------------- ${self.prices[i]}")
        print(f"""TOTAL: {self.total}

###########################################""")


    

    

    

main()