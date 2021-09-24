from BasicConfigMenu import ShowBasicConfigurationMenu
from InterfaceVlanMenu import ShowInterfacesAndVlanConfigurationMenu
from Streamer import StreamReceivedPacketAmount

running = True

while running:
    
    print("1. Basic config")
    print("2. Interface / Vlan config")
    print("3. Watch packet amount")
    print("4. Exit the program")
    
    menuNumber = int(input("\n"))
    
    if menuNumber == 1:
        ShowBasicConfigurationMenu()
    elif menuNumber == 2:
        ShowInterfacesAndVlanConfigurationMenu()
    elif menuNumber == 3:
        print("Streaming packets coming in, use CTRL + C to stop the loop")
        StreamReceivedPacketAmount()
    else:
        running = False