def GetEmailAddress():
    # Variables
    isValid = False
    userEmail = input("Enter your email address: ")
    emailList = userEmail.split("@")
    
    # Conditions for email validation
    # if email has exactly one "@" symbol (delimiter)
    if userEmail.count("@") == 1:
        # if email has one or more full stop delimiters
        if userEmail.count(".") > 0:
            # if email username and domain name respectively are between 2 and 32 characters long 
            i = 0
            while i < len(emailList):
                if len(emailList[i]) > 1 and len(emailList[i]) < 33:
                    isValid = True
                    i += 1
                else:
                    isValid = False
                    break
        else:
            isValid = False
    else:
        isValid = False
    
    # Print statements
    if isValid:
        print("Email is valid.")
        print(f"Email: {userEmail}")
    else:
        print("Email is not valid.")

GetEmailAddress()