print("Welcome to SmartShop Store")
print("For exiting type 'bye' /n")
while True:
    user= input("You: ").lower()
    if user in ["hii","hello","hey"]:
        print("Bot: Namaste!! How can i help you?")

    elif user in ["timing","open"]:
        print("Bot: Our store is open from 9:00 AM to 9:00 PM")

    elif user in ["items","products"]:
        print("Bot: We have mobiles,laptops,T.V. and other electronics accessories")

    elif user in ["thanks","thank you"]:
        print("Bot: You are welcome!!")

    elif user in ["payment"]:
        print("Bot: We accept cash, credit/debit cards and UPI payments")
        
    elif user in ["order"]:
        print("Bot: Please enter your order ID to check the status")    

    elif user in ["contact"]:
        print("Bot: You can contact us at 1234567890 or email us at support@smartshop.com")

    elif user == "bye":
        print("Bot: Thanks for visiting our store")
        break

    else:
        print("Bot: I did't understand it")