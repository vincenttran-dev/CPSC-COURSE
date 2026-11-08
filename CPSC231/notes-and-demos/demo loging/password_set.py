# Vincent Tran (30313622)

#Data base:
passw = []
account = []


#Password
special_character = "!@#$%^&*()-_+=?"

spe = False
num = False

while spe == False or num == False:

    password = input("Please enter your password: ")

    spe = False
    num = False

    for character in password:
        if character.isdigit():
            num = True
        elif character in special_character:
            spe = True

        # Explain what this password is missing
    if spe == False and num == False:
        print("You need a special character and a number.")
    elif spe == False:
            print("You need a special character.")
    elif num == False:
            print("You need a number.")
            
repass = input("Please enter your password again:")
while repass != password:
    repass = input("\t\tIncorrect! \n\t Please enter your password again:")
passw.append(repass)

    
    
