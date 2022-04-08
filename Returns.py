import time
class Returns:

    def __init__(self):
        self.orders = {1: "iPhone 13 64GB", 2: "Nvidia RTX 3080", 3: "Playstation 5"}
        self.facilities = ["Kelowna", "Edmonton", "Toronto"]
        self.shipping = ["Canada Post", "Purolator", "UPS"]


    def Return_Process(self):
        print("Welcome to our automated return service!")
        time.sleep(1.2)
        while True:
            try:
                time.sleep(2)
                orderid = int(input("May I please have your order ID?"))
                if 1 <= orderid <= 3:
                    time.sleep(2)
                    print("Thank you so much! The order ID you have selected is " + str(orderid))
                    break
                else:
                    time.sleep(2)
                    print("Invalid order ID.")
            except ValueError:
                time.sleep(2)
                print("Order ID must be an integer.")

        time.sleep(2)
        print("The product you wish to return is " + self.orders[orderid])
        time.sleep(2)
        reasoning = input("Is there any reason you wish to return " + self.orders[orderid])
        time.sleep(2)
        print("I'm sorry to hear that you're unsatisfied with the product.")
        time.sleep(2)
        while True:
            time.sleep(2)
            facility = str(input("Please choose the facility that is closest to you (" + ", ".join(self.facilities) + "):"))
            if facility.lower() == "kelowna":
                time.sleep(2)
                facility = 0
                print("Thank you for choosing the " + self.facilities[facility] + " facility!")
                break
            elif facility.lower() == "edmonton":
                time.sleep(2)
                facility = 1
                print("Thank you for choosing the " + self.facilities[facility] + " facility!")
                break
            elif facility.lower() == "toronto":
                time.sleep(2)
                facility = 2
                print("Thank you for choosing the " + self.facilities[facility] + " facility!")
                break
            else:
                time.sleep(2)
                print("Invalid facility.")

        time.sleep(2)
        while True:
            time.sleep(2)
            creditOrRefund = str(input("Would you like in-store credit or a refund for your return? (credit/refund)"))
            if creditOrRefund.lower() == "credit":
                time.sleep(2)
                creditOrRefund = True
                email = str(input("May I please have your email?"))
                time.sleep(2)
                print("Thank you! The in-store credit will appear in your account shortly.")
                break
            elif creditOrRefund.lower() == "refund":
                time.sleep(2)
                creditOrRefund = False
                email = str(input("May I please have your email?"))
                time.sleep(2)
                print("Thank you! A refund will be issued to the default payment method on your account.")
                break
            else:
                time.sleep(2)
                print("Invalid response.")

        time.sleep(2)
        while True:
            time.sleep(2)
            shipform = str(input("We're almost done! Would you like to complete the quick shipping form now or later? (now/later)"))
            if shipform.lower() == "now":
                time.sleep(2)
                self.Ship_Progress(facility, email, creditOrRefund)
                break
            elif shipform.lower() == "later":
                time.sleep(2)
                print("Your return request has been processed!")
                time.sleep(2)
                print("An email confirmation along with the shipping form has been emailed to " + email)
                time.sleep(2)
                print("Thank you for using our automated return service!")
                break
            else:
                time.sleep(2)
                print("Invalid response.")




    def Ship_Progress(self, facility, email, creditOrRefund):
        print("Thank you for choosing to fill out the shipping form now!")
        time.sleep(2)
        print("This form is quick and easy, and also gives you instructions on how to ship your product.")
        time.sleep(2)
        while True:
            time.sleep(2)
            preferredshipping = str(input("What is your preferred postal service ("+", ".join(self.shipping) + "):"))
            if preferredshipping.lower() == "canada post":
                time.sleep(2)
                preferredshipping = 0
                print("Thank you for choosing Canada Post!")
                break
            elif preferredshipping.lower() == "purolator":
                time.sleep(2)
                preferredshipping = 1
                print("Thank you for choosing Purolator!")
                break
            elif preferredshipping.lower() == "ups":
                time.sleep(2)
                preferredshipping = 2
                print("Thank you for choosing UPS!")
                break
            else:
                time.sleep(2)
                print("Invalid response.")

        time.sleep(2)
        print("In order to ship your product to us, please find an appropriately sized box to ship it in.")
        time.sleep(3)
        print("The box should be able to fit comfortably in the box, along with protection (i.e packing peanuts, bubble wrap)")
        time.sleep(3)
        print("After securing the product inside the box, you must attach a shipping label to it.")
        time.sleep(3)
        print("A " + self.shipping[preferredshipping] + " shipping label has been sent to " + email + " addressed to the " + self.facilities[facility] + " facility.")
        time.sleep(3)
        print("Once the shipping label has been secured onto the package, please go to your nearest " + self.shipping[preferredshipping] + " and ship it out.")
        time.sleep(3)
        if creditOrRefund == True:
            print("Once the tracking number has updated on our end, the in-store credit will be shown in your account balance shortly.")
        elif creditOrRefund == False:
            print("Once the tracking number has updated on our end, the refund will be issued to your card shortly.")
        time.sleep(3)
        print("That concludes the shipping form.")
        time.sleep(3)
        print("Thank you for using our automated return service!")


if __name__ == '__main__':
    retbot = Returns()
    retbot.Return_Process()










