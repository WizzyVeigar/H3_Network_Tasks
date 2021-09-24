from BasicConfigs import ChangeHostName, ChangeBanner, ChangeSecret

def ShowBasicConfigurationMenu():
    print("What would you like to do?")
    print("1. Change hostname")
    print("2. Change banner")
    print("3. Change secret password")
    
    choice = int(input())
    
    if choice == 1:
        newName = input("What is the new hostname?\n")
        print(ChangeHostName(newName))        
    elif choice == 2:
        newBanner = input("What is the new banner?\n")
        print(ChangeBanner( newBanner))
    elif choice == 3:
        newSecret = input("What is the new password?\n")
        print(ChangeSecret(newSecret))
    else:
        print("Invalid option")