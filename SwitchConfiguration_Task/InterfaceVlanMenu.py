from BasicConfigs import OpenCloseInterface, SetIp
from SwitchConfiguration import GetSwitchVlans, SetPortMode, SetVlanOnInterface
from BasicConfigs import GetInterfaces

def ShowInterfacesAndVlanConfigurationMenu():
    interfaces = []
    print("1. Show all interfaces")
    print("2. Configure interface")
    print("3. Show all Vlans")
    print("4. Configure Vlan")
    
    
    choice = int(input("\n"))    
    interfaces = GetInterfaces()
    
    if choice == 1:
            print("ID        Name        status      Proto")
            for interface in interfaces:
                print(str(interfaces.index(interface) + 1) + ".      "+ interface.name + "       "+ interface.status + "      ", interface.proto)

    elif choice == 2:
        #Minus 1 so we can also get the first/last one
        intNum = int(input("What interface would you like to configure? (use ID)\n")) - 1 
        if intNum < len(interfaces) and len(interfaces) > 0:
            print("1. Open / Close interface")
            print("2. Set port mode")
            print("3. Set Vlans")
                
            choice = int(input("\n"))
                
            if choice == 1:
                OpenCloseInterface(interfaces[intNum])
            elif choice == 2:
                SetPortMode(interfaces[intNum], input("Switch to trunk(1) or access(2)\n"))
            elif choice == 3:
                SetVlanOnInterface(interfaces[intNum], input("What is the vlan id?\n"))
        else:
            print("Interfaces length is 0")
            
    elif choice == 3:     
        vlans = GetSwitchVlans()
        print("ID      Name    IP          Status")
        for vlan in vlans:
            print(str(vlans.index(vlan) + 1) + ".      " + vlan.name + "   " + vlan.ipAdd + "   " + vlan.status)
    
    elif choice == 4:
        vlans = GetSwitchVlans()
        vlanId = int(input("Id of the vlan you want to configure\n"))
        
        for vlan in vlans:
            if str(vlanId) in vlan.name:
                vlanToConfig = vlan
        
        print("1. Open / Close Vlan")
        print("2. Set Ip Address")
        
        choice = int(input("\n"))
            
        if choice == 1:
            OpenCloseInterface(vlanToConfig)
        elif choice == 2:
            ip = input("What is the ip address?\n")
            subnet = input("What is the subnet mask?\n")
            SetIp(vlanToConfig, ip, subnet)