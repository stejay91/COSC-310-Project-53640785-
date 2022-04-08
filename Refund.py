def refund():
    print("Please provide your order Number")
    orderNumber = input()
    if orderNumber !="":
        print("Is the package delivered?Y/N")
        received_check = input()
        if received_check == "Y":
                print("Is the item broken or stolen? broken/stolen")
                package_status= input()
                if package_status=="broken":
                    print("Please provide the picture of the damaged item")
                    picture_prove = input()
                    if picture_prove!="":
                        print("We have approved your refund request! Your money will refund to your account soon")
                elif package_status=="stolen":
                    print("You money has been refunded to your account!")
        elif received_check=="N":
            print("we will contact the delivering company and will return your fund to your account!")
    else:
        print("the order number you have inputted is not in our system, please input again")
    return"Thanks"

if __name__ == '__main__':
    refund()

