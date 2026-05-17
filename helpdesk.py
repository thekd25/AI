print("......Helpdesk......\n")
print("Answer question in yes or no\n")

problem = input("Is you computer not starting ?\n").lower()

if problem=="yes":
    power=input("Is the power cable connected properly ?\n").lower()
    if power=="no":
        print("connect power cable and restart it")
    else:
        ram= input("Are you hear any beep sound from your PC ?\n").lower()
        if ram=="yes":
            print("This is ram insert issue, re-insert ram and check it")
        else:
            print("Solution: Contact hardware support technician.")

else:
    internet=input("Is there any internet issue ?\n").lower()
    if internet=="yes":
        router=input("Is router connected properly ?\n").lower()
        if router=="no":
            print("Connect it")
        else:
            print("Contact with ISP")
    else:
        software=input("Is software not working ?\n").lower()
        if software=="yes":
            print("Re-Install it and then check")
        else:
            print("Problem not identified. Contact Help Desk Support")

print("Thank you for using our helpdesk service")