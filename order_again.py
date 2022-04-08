import time
class OrderAgain:
    def __init__(self):
        self.orders = {1: "iPhone 13 64GB", 2: "Nvidia RTX 3080", 3: "Playstation 5"}
        self.prices = {1: 999, 2: 2999, 3: 599}
        self.facilities = ["Kelowna", "Edmonton", "Toronto"]
        self.shipping = ["Canada Post", "Purolator", "UPS"]
    
    def order_again_chat(self):
        print("Welcome to our automated order again service!")
        print(f"It looks like you have ordered {len(self.orders)} items.")
        p = ""
        for i,j in self.orders.items():
            p += str(i)
            p += ": "
            p += j
            p += ", "
        p = p[:-2]
        print(f"They are {p}.")

        on = ""
        while True:
            try:
                on = int(input(f"Please tell me which item you want to order again? (An integer between 1 and {len(self.orders)}): "))
                if on >= 1 and on <= len(self.orders):
                    print(f"You are going to reorder the {self.orders[on]} and the price is ${self.prices[on]}. We are glad you love it!")
                    break
                else:
                    print(f"The order number you provided ({on}) is invalid, please input again!")
            except:
                print("Invalid input, please input an integer as your order number.")
        
        pay = ""
        while True:
            pay = input("Please tell me the payment method you want to use (check/credit): ")
            pay = pay.lower().strip()
            if pay == "check" or pay == "credit":
                print(f"You decided to use {pay} as the payment method of this order. No problem!")
                break
            else:
                print(f"Sorry, we do not support the {pay} payment method you selected, please use either \'check\' or \'credit\'.")
        
        f = ""
        while True:
            try:
                f = int(input(f"Please tell me which facility you want your order to ship from (An integer between 0 and {len(self.facilities)-1}): "))
                if f >= 0 and f < len(self.facilities):
                    print(f"You decided to ship your order from {self.facilities[f]}. Wise choice!")
                    break
                else:
                    print(f"The facility number you provided ({f}) is invalid, please input again!")
            except:
                print("Invalid input, please input an integer as your selected facility.")

        address = ""
        address = input("Please input your address to receive your order: ")
        print(f"Your address is {address}. we will deliver it to your address as soon as possible.")

        c = ""
        while True:
            try:
                c = int(input(f"Please tell me which carrier you want to use (An integer between 0 and {len(self.shipping)-1}): "))
                if f >= 0 and f < len(self.shipping):
                    print(f"You decided to use the {self.shipping[f]}. We will do that!")
                    break
                else:
                    print(f"The carrier number you provided ({f}) is invalid, please input again!")
            except:
                print("Invalid input, please input an integer as your selected carrier.")
        
        print("\nThis is your detail:")
        print(f"Order item: {self.orders[on]}.")
        print(f"Order price: {self.prices[on]}.")
        print(f"Shipping facility: {self.facilities[f]}.")
        print(f"Payment method: {pay}.")
        print(f"Selected carrier: {self.shipping[c]}.")
        print(f"Deliever address: {address}.\n")

        print("Thank you for order with us again! See you later!")

             
