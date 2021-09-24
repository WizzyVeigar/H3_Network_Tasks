from ConnectionGetter import CreateConnection
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException
from InterfaceObj import InterfaceObj

        
def GetPortMode(interface):
    connection = CreateConnection()
    comm = "show interface " + interface.name + " switchport"
    
    try:
        output = connection.send_command(comm)
        if "Administrative Mode: trunk" in output:
            return "trunk"
        elif "Administrative Mode: static access" in output:
            return "access"
        else:
            return "access"
    except:
        print("Something went wrong with setting the port mode")
    finally:
        connection.disconnect()
        
def GetSwitchVlans():
    connection = CreateConnection()
    comm = "sh ip int brief"
    interfaces = []
    try:
        output = connection.send_command(comm, use_textfsm=True)
        for vlan in output:
            inter = InterfaceObj(vlan["intf"], vlan["ipaddr"], vlan["status"], vlan["proto"])
            if "Vlan" in inter.name:
                interfaces.append(inter)    
                
    except NetMikoTimeoutException:
        print("Connection Timed out")
    except NetMikoAuthenticationException:
        print("Access denied: Authentication failed")
    finally:
        connection.disconnect()
        return interfaces
        
def SetPortMode(interface, modeToChangeTo):
    connection = CreateConnection()
    comms = ["int " + interface.name]
    try:
        if "trunk" or "1" in modeToChangeTo:
            comms.append("switchport trunk encapsulation dot1q")
            comms.append("switchport mode trunk")
        else:
            comms.append("switchport mode access")        
        
        connection.send_config_set(comms)
        print("port has been set")
    except:
        print("Setting the port mode failed!")
    finally:
        connection.disconnect()
        
def SetVlanOnInterface(interface, vlanId):
    comms = ["int " + interface.name]
    try:
        mode = GetPortMode(interface)
        if "access" in mode:
            comms.append("switchport access vlan " + vlanId)
        elif "trunk" in mode:
            comms.append("switchport trunk allowed vlan " + vlanId)  
            
        for command in comms:
            print(command)
        connection = CreateConnection()
        connection.send_config_set(comms)
    except:
        print("Couldn't complete the command, something went wrong")
    finally:
        connection.disconnect()
