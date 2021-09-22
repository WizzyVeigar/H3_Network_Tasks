from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException 
from InterfaceObj import InterfaceObj


connection = ConnectHandler(
    device_type="cisco_ios",
    host="10.10.1.2",
    username="Cisco",
    password="Class",
    secret="Class")

def ChangeHostName(connection, hostname):
    try:
        commands = ["hostname "]
        connection.enable()
        connection.send_config_set(commands[0]+hostname)
        return "Was successfully changed" 
    except NetMikoAuthenticationException:
        return "Something went wrong with the command"
    except NetMikoTimeoutException:
        return "Connection Timed out"
    finally:
        connection.disconnect()
        
        
def ChangeBanner(connection, bannerText):
    try:
        commands = ["banner #"]
        connection.enable()
        connection.send_config_set(commands[0] + bannerText + "#")
        return "Was successfully changed" 
    except NetMikoAuthenticationException:
        return "Something went wrong with the command"
    except NetMikoTimeoutException:
        return "Connection Timed out"
    finally:
        connection.disconnect()

def ChangeSecret(connection, password):
    try:
        commands = ["enable secret "]
        connection.enable()
        connection.send_config_set(commands[0] + password)
        return "Was successfully changed" 
    except NetMikoAuthenticationException:
        return "Something went wrong with the command"
    except NetMikoTimeoutException:
        return "Connection Timed out"
    finally:
        connection.disconnect()
        


def ShowBasicConfigurationMenu(connection):
    print("What would you like to do?")
    print("1. Change hostname")
    print("2. Change banner")
    print("3. Change secret password")
    print("4. See all interfaces")
    
    choice = int(input())
    
    if choice == 1:
        newName = input("What is the new hostname?\n")
        print(ChangeHostName(connection, newName))        
    elif choice == 2:
        newBanner = input("What is the new banner?\n")
        print(ChangeBanner(connection, newBanner))
    elif choice == 3:
        newSecret = input("What is the new password?\n")
        print(ChangeSecret(connection, newSecret))
    elif choice == 4:
        ShowInterfaceConfigurationMenu(connection)
    else:
        print("no")
        
        
def GetSwitchInterfaces(connection):
    comm = "sh ip int brief"
    interfaces = []
    try:
        connection.enable()
        output = connection.send_command(comm, use_textfsm=True)
        for interface in output:
            inter = InterfaceObj(interface["intf"],interface["ipaddr"],interface["status"],interface["proto"])
            interfaces.append(inter)
            
    except NetMikoTimeoutException:
        print("Connection Timed out")
    except NetMikoAuthenticationException:
        print("Access denied: Authentication failed")
    finally:
        connection.disconnect()
        return interfaces


def ShowInterfaceConfigurationMenu(connection):
    interfaces = GetSwitchInterfaces(connection)
    print("#        Name        status      Proto")
    for interface in interfaces:
        print(str(interfaces.index(interface)) + ".      "+ interface.name + "       "+ interface.status + "      ", interface.proto)
    
    
ShowBasicConfigurationMenu(connection)