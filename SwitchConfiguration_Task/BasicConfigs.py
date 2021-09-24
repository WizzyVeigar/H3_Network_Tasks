from ConnectionGetter import CreateConnection
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException
from InterfaceObj import InterfaceObj

def ChangeHostName(hostname):
    connection = CreateConnection()
    try:
        commands = ["hostname "]
        connection.send_config_set(commands[0]+hostname)
        return "Was successfully changed" 
    except NetMikoAuthenticationException:
        return "Something went wrong with the command"
    except NetMikoTimeoutException:
        return "Connection Timed out"
    finally:
        connection.disconnect()
        
        
def ChangeBanner(bannerText):
    connection = CreateConnection()
    try:
        commands = ["banner #"]
        connection.send_config_set(commands[0] + bannerText + "#")
        return "Was successfully changed" 
    except NetMikoAuthenticationException:
        return "Something went wrong with the command"
    except NetMikoTimeoutException:
        return "Connection Timed out"
    finally:
        connection.disconnect()

def ChangeSecret(password):
    connection = CreateConnection()
    try:
        commands = ["enable secret "]
        connection.send_config_set(commands[0] + password)
        return "Was successfully changed" 
    except NetMikoAuthenticationException:
        return "Something went wrong with the change secret command"
    except NetMikoTimeoutException:
        return "Connection Timed out"
    finally:
        connection.disconnect()
        
def GetInterfaces():
    connection = CreateConnection()
    comm = "sh ip int brief"
    interfaces = []
    try:
        output = connection.send_command(comm, use_textfsm=True)
        for interface in output:
            inter = InterfaceObj(interface["intf"],interface["ipaddr"],interface["status"],interface["proto"])
            if "Vlan" not in inter.name:
                interfaces.append(inter)
            
    except NetMikoTimeoutException:
        print("Connection Timed out")
    except NetMikoAuthenticationException:
        print("Access denied: Authentication failed")
    finally:
        connection.disconnect()
        return interfaces
    
def OpenCloseInterface(interface):
    connection = CreateConnection()
    try:
        comms = ['int ' + interface.name]
        
        # print(interface.status)
        
        if "up" in interface.status:
            comms.append("shutdown")
            connection.send_config_set(comms, cmd_verify=False)
        else:
            comms.append("no shut \n")
            connection.send_config_set(comms, cmd_verify=False)
    except:
        print("Error occured in OpenCloseInterface")
    finally:
        connection.disconnect()
        
def SetIp(interface, ip, subnet):
    connection = CreateConnection()
    # print(ip)
    # print(subnet)   
    comms = ["int " + interface.name, " ip add " + ip + " " + subnet]
    
    try:
        connection.send_config_set(comms)
    except:
        print("Something went wrong")
    finally:
        connection.disconnect()
        
    