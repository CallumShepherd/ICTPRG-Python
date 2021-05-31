def GetIPAddress():
    isValid = False
    userIP = input("Enter your IP address: ")
    IPList = userIP.split(".")
    IPListLength = len(IPList)
    for octet in IPList:
        if IPListLength == 4:
            if octet.isdigit():
                if int(octet) > -1 and int(octet) < 256:
                    isValid = True
                else:
                    isValid = False
                    print("Invalid input: please enter integers that are between 0 and 255 inclusive.")
                    break
            else:
                isValid = False
                print("Invalid input: please enter integers.")
                break
        else:
            isValid = False
            print("Invalid input: please enter exactly four octets.")
            break
    if isValid == True:
        print(f"Your IP address ({userIP}) is valid.")

GetIPAddress()